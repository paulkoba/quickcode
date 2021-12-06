import os
import re
from .models import TestCase, Problem, Result
from pathlib import Path


def test_submission(source, problem_id):
    dir_name = os.path.dirname(source.file.path)
    os.mkdir(dir_name + '/tests')

    tests = TestCase.objects.all().filter(problem=problem_id)

    cumulative_time_limit = 5

    for el in tests:
        cumulative_time_limit += el.execution_limit
        with open(dir_name + '/tests/' + str(el.id), 'w') as f:
            f.write(el.input)

    if source.language == "1":
        os.popen(str(Path(dir_name).parent.parent.absolute()) + '/ugc/safe-execute-cpp.sh '
                 + str(source.id) + ' ' + str(cumulative_time_limit)).read()

    if source.language == "2":
        os.popen(str(Path(dir_name).parent.parent.absolute()) + '/ugc/safe-execute-python.sh '
                 + str(source.id) + ' ' + str(cumulative_time_limit)).read()

    correct_answers = True
    timed_out = False

    if open(dir_name + '/output/compilation-result').read() != '0\n':
        source.result = Result.COMPILATION_ERROR
        source.save()
        return

    for el in tests:
        f1 = open(dir_name + '/output/' + str(el.id)).read()

        formatted1 = re.sub(r'\s+', ' ', f1).strip()
        formatted2 = re.sub(r'\s+', ' ', el.output).strip()

        if formatted1 != formatted2:
            correct_answers = False

        time_file_contents = open(dir_name + '/output/' + str(el.id) + '-time').read()
        if time_file_contents == '':
            timed_out = True
            break

        execution_time = 0

        try:
            execution_time = float(time_file_contents)
        except ValueError:
            correct_answers = False

        if execution_time > el.execution_limit:
            timed_out = True

    if correct_answers and not timed_out:
        source.result = Result.SUCCESS
    else:
        source.result = Result.TIMEOUT if timed_out else Result.WRONG

    source.save()
