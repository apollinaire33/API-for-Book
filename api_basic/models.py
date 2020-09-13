from django.db import models



class Book(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=100)
    author_name = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    


    def __str__(self):
        return self.title


