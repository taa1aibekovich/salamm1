from django.db import models


class TodoList(models.Model):
    name = models.CharField(max_length=62)
    price = models.IntegerField(default=0)
    description = models.TextField()
    quantity = models.IntegerField()
    files = models.ImageField(null=True, blank=True)
    is_completed = models.BooleanField(default=False)
    category = models.CharField(max_length=100)
    author = models.CharField(max_length=100)


    def __str__(self):
        return self.name




