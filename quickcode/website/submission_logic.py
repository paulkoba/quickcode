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

    succeeded = True

    for el in tests:
        f1 = open(dir_name + '/output/' + str(el.id)).read()

        formatted1 = re.sub(r'\s+', ' ', f1).strip()
        formatted2 = re.sub(r'\s+', ' ', el.output).strip()

        if formatted1 != formatted2:
            succeeded = False

    source.result = Result.SUCCESS if succeeded else Result.FAIL
    source.save()
