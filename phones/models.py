import autoslug
from django.db import models




class Phone(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    price = models.PositiveIntegerField(blank=True, null=True)
    image = models.URLField()
    release_date = models.DateField()
    lte_exists = models.BooleanField()
    slug = models.SlugField(name)



    # def __str__(self):
    #     return f'{self.name}, {self.price}: {self.image}'

    # pass
