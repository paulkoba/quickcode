import os
from .models import TestCase
from pathlib import Path


def test_submission(source, problem_id):
    dir_name = os.path.dirname(source.file.path)
    os.mkdir(dir_name + '/tests')

    tests = TestCase.objects.all().filter(problem=problem_id)

    for el in tests:
        with open(dir_name + '/tests/' + str(el.id), 'w') as f:
            f.write(el.input)

    os.popen(str(Path(dir_name).parent.parent.absolute()) + '/ugc/safe-execute.sh ' + str(source.id))
