from django.db import models

class MyModel:
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100)


    class Meta:
        managed = False
        db_table = 'Users'



