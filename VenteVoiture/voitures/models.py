from django.db import models
from django import forms
# Create your models here.


from django.db import models
from django.core.validators import MinValueValidator,MaxValueValidator
# Create your models here.


#Classe voiture
class Voiture(models.Model):
    class Mark(models.TextChoices):
        PEOGOT='PEOGEOT'
        RENAULT='RENAULT'
        RANGE_ROVER='RR'

    name=models.fields.CharField(max_length=50)
    mark=models.fields.CharField(choices=Mark.choices,max_length=10)
    model=models.fields.CharField(max_length=50)
    price=models.fields.IntegerField()
    available:models.fields.BooleanField(default=True)
    year_created=models.fields.IntegerField(
        validators=[MinValueValidator(2010),MaxValueValidator(2022)])
    image=models.fields.CharField(null=True,blank=True,max_length=500)



class VoitureForm(forms.ModelForm):
    class Meta:
        model=Voiture
        fields= '__all__'
      

#Classe des Utilsateurs
class User(models.Model):
    firstname=models.fields.CharField(max_length=50)
    lastname=models.fields.CharField(max_length=50)
    email=models.fields.CharField(max_length=50)
    pasword=models.fields.CharField(max_length=50)