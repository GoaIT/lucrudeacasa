from django.db import models
from django.urls import reverse

# Create your models here.
class School(models.Model):
    name = models.CharField(max_length=256)
    principal = models.CharField(max_length=256)
    location = models.CharField(max_length=256)

    def __str__(self):
        return self.name
    # in momentul in care creezi un obiect nou in baza de date
    # te ajuta la DetailView cand ii spui ca dupa creeze sa se duca pe pagina obiectului creat
    # l-am folosit aici pentru ca in tabela asta am creat un nou obiect   
    def get_absolute_url(self):
        return reverse("cbv_app:detail",kwargs={'pk':self.pk})

class Student(models.Model):
    name = models.CharField(max_length=256)
    age = models.PositiveIntegerField()
    school = models.ForeignKey(School,related_name='students',on_delete=models.CASCADE)

    def __str__(self):
        return self.name
