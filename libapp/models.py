from django.db import models

# Create your models here.
class Userdata(models.Model):
    fname=models.CharField(max_length=20)
    lname=models.CharField(max_length=20)
    pass1=models.CharField(max_length=15)
    pass2=models.CharField(max_length=15)
    email=models.EmailField(primary_key=True)

    def __str__(self):
        return "{},{},{},{},{}".format(self.fname,self.lname,self.pass1,self.pass2,self.email)
    class Meta:
        db_table='userdata'

class Book(models.Model):
    id=models.IntegerField(primary_key=True)
    name=models.CharField(max_length=30)
    author=models.CharField(max_length=30)

    def __str__(self):
        return "{},{},{}".format(self.id,self.name,self.author)

    class Meta:
        db_table="book"
