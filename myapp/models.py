from django.db import models



class Pet(models.Model):
    SEX_CHOICES=[{'M','Male'},{'F','Female'}]
    name=models.CharField(max_length=30)
    submitter=models.CharField(max_length=100)
    species=models.CharField(max_length=30)
    breed=models.CharField(max_length=30,null=True)
    description=models.TextField()
    sex=models.CharField(max_length=12,choices=SEX_CHOICES,blank=True)
    submission_date=models.DateTimeField()
    age=models.IntegerField(null=True)
    vaccinations=models.ManyToManyField('Vaccine',blank=True)
    
    def __str__(self):
        return self.name
    
    
class Vaccine(models.Model):
    name=models.CharField(max_length=30)
    
    def __str__(self):
        return self.name