from django.db import models
from django.db import connection

if connection.connection:
    print('MySQL database is connected')
else:
    print('MySQL database is not connected')

class MyModel(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100)


    class Meta:
        managed = False
        db_table = 'Users'

class Post(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=255)
    content = models.TextField()
    created_by = models.ForeignKey(MyModel, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        managed = True
        db_table = 'Posts'







