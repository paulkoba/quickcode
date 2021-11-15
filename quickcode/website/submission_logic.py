import os
import re
from .models import TestCase, Problem, Result
from pathlib import Path


def test_submission(source, problem_id):
    dir_name = os.path.dirname(source.file.path)
    os.mkdir(dir_name + '/tests')

    tests = TestCase.objects.all().filter(problem=problem_id)

    for el in tests:
        with open(dir_name + '/tests/' + str(el.id), 'w') as f:
            f.write(el.input)

    os.popen(str(Path(dir_name).parent.parent.absolute()) + '/ugc/safe-execute.sh ' + str(source.id)).read()

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

        execution_time = float(time_file_contents)

        if execution_time > el.executionLimit:
            timed_out = True

    source.result = Result.SUCCESS if correct_answers else Result.WRONG
    if timed_out:
        source.result = Result.TIMEOUT

    source.save()
