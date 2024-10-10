from django.db import models

# Create your models here.
class Authors(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=200)
    bio=models.TextField(null=True,blank=True)
    
class Genre(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=200)
    
class Books(models.Model):
    id=models.AutoField(primary_key=True)
    title=models.CharField(max_length=200)
    author_id=models.ForeignKey(Authors, on_delete= models.CASCADE)
    genre_id=models.ForeignKey(Genre, on_delete= models.CASCADE)
    published_date=models.DateTimeField(auto_now_add=True)