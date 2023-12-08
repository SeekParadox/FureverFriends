from django.core.validators import RegexValidator
from django.db import models


class Animal(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=256)
    breed = models.CharField(max_length=30)
    color = models.CharField(max_length=50)
    age = models.IntegerField(null=False)


class Adopter(models.Model):
    email = models.CharField(max_length=70, primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    number = models.CharField(validators=[RegexValidator(
        regex='^.{10}$', message='Length has to be 10', code='nomatch'
    )], blank=True)
    street = models.CharField(max_length=95)
    city = models.CharField(max_length=36)
    zip = models.CharField(max_length=10)


class Animal_adoption(models.Model):
    id = models.ForeignKey('Animal', on_delete=models.CASCADE)
    person = models.ForeignKey('Adopter', on_delete=models.CASCADE)
    adoption_date = models.DateField()

    class Meta:
        unique_together = (("id", "person"),)


class Animal_vaccine(models.Model):
    id = models.ForeignKey("Animal", on_delete=models.CASCADE)
    name = models.CharField(max_length=256)
    dose = models.CharField(max_length=256)
    admin_date = models.DateField()

    class Meta:
        unique_together = (("id", "name"),)
