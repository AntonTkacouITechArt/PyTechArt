from django.core.validators import MaxValueValidator
from django.db import models

# Create your models here.
from django.urls import reverse


class Student(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)
    surname = models.CharField(max_length=50, null=False,
                               blank=False)
    b_day = models.DateField(null=False, blank=False)

    def __str__(self):
        return f'{self.name} {self.surname}'

    def get_absolute_url(self):
        return reverse('student_detail', kwargs={'pk': self.pk})


class Teacher(models.Model):
    RANKS = (
        ('pg', 'postgraduate'),
        ('as', 'assistant'),
        ('dc', 'docent'),
        ('pr', 'professor')
    )
    name = models.CharField(max_length=50, null=False, blank=False)
    surname = models.CharField(max_length=50, null=False, blank=False)
    rank = models.CharField(max_length=2, choices=RANKS, default='pg', )

    def __str__(self):
        return f'{self.name} {self.surname} {self.rank}'

    def get_absolute_url(self):
        return reverse('teacher_detail', kwargs={'pk': self.pk})


class Mark(models.Model):
    date = models.DateField()
    teacher = models.ForeignKey(
        Teacher,
        on_delete=models.PROTECT,
        related_name='teacher_relate',
        related_query_name='teacher_filter'
    )
    student = models.ForeignKey(
        Student,
        on_delete=models.CASCADE,
        related_name='student_relate',
        related_query_name='student_filter',
    )
    mark = models.PositiveIntegerField(default=0, validators=[MaxValueValidator(10)], null=False, blank=False)

    def __str__(self):
        return f"""student: {self.student.name} {self.student.surname} ->
         marks: {self.mark} -> teacher: {self.teacher.name} {self.teacher.surname}
          {self.teacher.rank}"""
