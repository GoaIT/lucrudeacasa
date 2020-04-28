from django.db import models

class Entry(models.Model):
    entry_id = models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    text = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return 'Entry #{}'.format(self.pk)
    
    class Meta:
        verbose_name_plural = 'entries' #ceea ce se va vedea in Admin ca si plural al tabelei create

class Simple(models.Model):
    simple_id = models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    text = models.CharField(max_length=25)
    number = models.IntegerField()
    url = models.URLField()

    def __str__(self):
        return self.url

class AccessRecord(models.Model):
    name = models.ForeignKey(Simple, on_delete=models.CASCADE)
    date = models.DateField()

    def __str__(self):
        return str(self.date)
    
class Languages(models.Model):
    language_id = models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    name = models.CharField(max_length=15,null=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = 'languages'

class Framework(models.Model):
    framework_id = models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    name = models.CharField(max_length=15)
    language = models.ForeignKey(Languages,on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Movies(models.Model):
    movie_id = models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    name = models.CharField(max_length=15)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'movies'

class Actors(models.Model):
    actor_id = models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    name = models.CharField(max_length=15)
    movies = models.ManyToManyField(Movies)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = 'actors'

###### PROCEDURA DE ADAUGARE IN SHELL ACTORI SI FILME #######
# from exemple_app.models import Movies, Actors
# green  = Movies(name='Green')     //instanta de film
# green.save()                      //salvam instanta
# air  = Movies(name='Air')         //alta instanta de film  
# air.save()
# vasile = Actors(name='Vasile')    //instanta de actor
# vasile.save()
# maria.movies.add(air)             //adaugam pe Maria ca a jucat in filmul Air
# vasile.movies.create(name='Red')  //creem un nou film "Red" si adaugam pe Vasile in el
