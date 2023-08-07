from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=100)

    # Need to add image
    cover = models.ImageField(null=True, blank=True)

    author = models.CharField(max_length=100)
    read_date = models.DateField()
    rating = models.PositiveSmallIntegerField()
    review = models.TextField(max_length=2000)

    def __str__(self):
        return self.title