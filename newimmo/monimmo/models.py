from django.db import models
from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from autoslug import AutoSlugField
from django.urls import reverse
from django.utils.text import slugify

# Create your models here.
class Promoteur(models.Model):
    nom = models.CharField(max_length=40)
    description = models.TextField(max_length=1000)

    def __str__(self):
        return self.nom

class Programme(models.Model):
    LIVRAISON_STATUTS = ((1, "En commercialisation"), (2, "En construction"), (3, "Terminé"))
    promoteur = models.ForeignKey(Promoteur, on_delete=models.CASCADE)
    nom = models.CharField(max_length=40)
    description = models.CharField(max_length=500, blank=True, null=True)
    date_livraison_ini = models.DateField("Date de livraison initiale")
    date_livraison_act = models.DateField("Date de livraison prévue", blank=True, null=True)
    statut = models.IntegerField(choices=LIVRAISON_STATUTS)
    slug = AutoSlugField(populate_from='nom', always_update=True, max_length=255, editable=True, blank=True)

    def get_absolute_url(self):
        return reverse('detail_programme',
                       args=[self.slug, self.pk])

    def get_absolute_url_themes(self):
        return reverse('consult_themes',
                       args=[self.slug, self.pk])

    def __str__(self):
        return self.nom

    def save(self, *args, **kwargs):
        if self.date_livraison_act is None:
            self.date_livraison_act = self.date_livraison_ini
        super().save(*args, **kwargs)

class Topic(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=200)
    slug = AutoSlugField(populate_from='title', always_update=True, max_length=255, editable=True, blank=True)
    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            # Newly created object, so set slug
            self.slug = slugify(self.slug)
        super().save(*args, **kwargs)

class Subject(models.Model):
    programme = models.ForeignKey(Programme, on_delete=models.CASCADE)
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    title = models.CharField(max_length=50, blank=True, null=True)
    content = models.TextField(max_length=1500, blank=True, null=True)
    post_at = models.DateTimeField(auto_now_add=True)
    slug = AutoSlugField(populate_from='title', always_update=True, max_length=255, editable=True, blank=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            # Newly created object, so set slug
            self.slug = slugify(self.slug)
        super().save(*args, **kwargs)


class Post(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    post_at = models.DateTimeField(auto_now_add=True)
    content = models.TextField(max_length=1500, blank=True, null=True)

