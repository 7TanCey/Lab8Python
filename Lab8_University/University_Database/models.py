from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Student(models.Model):
    id = models.AutoField(primary_key=True)
    surname = models.CharField(max_length=30)
    name = models.CharField(max_length=30)
    patronymic = models.CharField(max_length=30)
    address = models.CharField(max_length=50)
    phone = models.CharField(max_length=10)
    course = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(4)])
    faculty = models.CharField(max_length=50)
    grup = models.CharField(max_length=10)
    headman = models.BooleanField()

    def __str__(self):
        return self.surname

    class Meta:
        verbose_name = 'Студент'
        verbose_name_plural = 'Студенти'


class Subject(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    hours = models.IntegerField()
    semesters = models.IntegerField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Предмет'
        verbose_name_plural = 'Предмети'


class Exam(models.Model):
    id = models.AutoField(primary_key=True)
    date = models.DateField()
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    grade = models.IntegerField(validators=[MinValueValidator(2), MaxValueValidator(5)])

    def __str__(self):
        return self.subject

    class Meta:
        verbose_name = 'Екзамен'
        verbose_name_plural = 'Екзамени'
