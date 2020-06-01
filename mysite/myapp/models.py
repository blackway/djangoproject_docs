from django.db import models


class Person(models.Model):
    SHIRT_SIZES = (
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
    )
    name = models.CharField(max_length=60)
    shirt_size = models.CharField(max_length=1, choices=SHIRT_SIZES)


class Musician(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    instrument = models.CharField(max_length=100)


class Album(models.Model):
    artist = models.ForeignKey(Musician, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    release_date = models.DateField()
    num_starts = models.IntegerField()


# class Runner(models.Model):
#     MedalType = models.TextChoices('MedalType', 'GOLD SILVER BRONZE')
#     name = models.CharField(max_length=60)
#     medal = models.CharField(blank=True, choices=MedalType.choices, max_length=10)


class Fruit(models.Model):
    name = models.CharField(max_length=100, primary_key=True)


class Manufacturer(models.Model):
    pass


class Car(models.Model):
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
    

