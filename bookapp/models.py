from django.db import models

# Create your models here.


class Book(models.Model):
    book_name = models.CharField(max_length=255, null=False)
    author_name = models.CharField(max_length=255, null=False)
    publisher = models.CharField(max_length=255, null=False)
    price = models.IntegerField(null=False)

    def __str__(self):
        return "{}".format(self.title)
