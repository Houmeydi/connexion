from django.db import models
from django.urls import reverse

class produit(models.Model):
    nom=models.CharField(max_length=100)
    slug=models.SlugField(max_length=120)
    prix=models.FloatField(default=0)
    stock=models.IntegerField(default=0)
    description=models.TextField(blank=True)
    image=models.ImageField(upload_to="produits",blank=True, null=True)
    
    def __str__(self) :
        return self.nom
    def get_absolute_url(self):
        return reverse("produit1" ,kwargs={"slug": self.slug})
    