import uuid
from django.db import models
from django.utils.translation import gettext_lazy as _


LANGUAGE = (
    (1, _("CPP")),
    (2, _("Python"))
)

class Problem(models.Model):
    """Model representing a problem."""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text='Unique ID for this particular problem')
    name = models.CharField(max_length=255, help_text='Problem name')
    description = models.TextField()

    def __str__(self):
        return str(self.name)


class TestCase(models.Model):
    """Model representing a test case for a particular problem."""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text='Unique ID for this particular problem')
    input = models.TextField()
    output = models.TextField()
    problem = models.ForeignKey(Problem, on_delete=models.CASCADE)
    execution_limit = models.IntegerField()


def location(instance, filename):
    return '/'.join(['submissions', str(instance.id), 'submission'])


class Result(models.TextChoices):
    SUCCESS = 'S', _('Successful')
    TIMEOUT = 'T', _('Time Limit Exceeded')
    WRONG = 'W', _('Wrong Answer')
    UNKNOWN = 'U', _('Unknown')
    FAIL = 'F', _('Failed')
    COMPILATION_ERROR = 'C', _('Compilation Error')


class Submission(models.Model):
    """Model representing a submission for a particular problem."""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text='Unique ID for this particular submission')
    problem = models.ForeignKey(Problem, on_delete=models.CASCADE)

    file = models.FileField(upload_to=location)

    result = models.CharField(max_length=1,
                              choices=Result.choices,
                              default=Result.UNKNOWN, )

    submissionTime = models.DateTimeField(auto_now=True)

    language = models.CharField(max_length=1, choices=LANGUAGE, default=1)


class SubmissionResultTestCase(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    submissionID = models.ForeignKey(Submission, on_delete=models.CASCADE)
