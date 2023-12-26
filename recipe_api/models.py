from django.db import models

class material(models.Model):
    name = models.CharField('name',max_length=20)
    recipes = models.ManyToManyField('recipe',blank=True)
    def __str__(self):
        return self.name
class recipe(models.Model) :
    name = models.CharField('name', max_length=20)
    review = models.CharField('review',max_length=100)
    describtion = models.TextField('describtion')
    enerjy = models.IntegerField('enerjy')
    materials = models.ManyToManyField(material,blank=True)
    def __str__(self):
        return self.name