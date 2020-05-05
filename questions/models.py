from django.db import models

# Create your models here.

TYPE_CHOICES = (
    ('multiple', 'Multiple choices'),
    ('single', 'Single choice')
)


class Question(models.Model):
    name = models.CharField(max_length=250)
    publish_at = models.DateTimeField()
    type = models.CharField(max_length=50, choices=TYPE_CHOICES)

    def __str__(self) -> str:
        return self.name


class Answer(models.Model):
    name = models.CharField(max_length=250)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.name
