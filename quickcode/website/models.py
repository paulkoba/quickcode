from django.db import models
import uuid


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
