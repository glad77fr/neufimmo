from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from autoslug import AutoSlugField
from django.urls import reverse
from django.utils.text import slugify
from tinymce.models import HTMLField
from ckeditor.fields import RichTextField


# Create your models here.
class Promoteur(models.Model):
    nom = models.CharField(max_length=40)
    description = models.TextField(max_length=1000)

    def __str__(self):
        return self.nom

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    avatar_img = models.ImageField(null=True, blank=True, upload_to="images/")

    @receiver(post_save, sender=User)
    def update_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)
        instance.profile.save()

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()

class Programme(models.Model):
    LIVRAISON_STATUTS = ((1, "En commercialisation"), (2, "En construction"), (3, "Terminé"))
    promoteur = models.ForeignKey(Promoteur, on_delete=models.CASCADE)
    nom = models.CharField(max_length=40)
    description = models.CharField(max_length=500, blank=True, null=True)
    date_livraison_ini = models.DateField("Date de livraison initiale")
    date_livraison_act = models.DateField("Date de livraison prévue", blank=True, null=True)
    statut = models.IntegerField(choices=LIVRAISON_STATUTS)
    slug = AutoSlugField(populate_from='nom', always_update=True, max_length=255, editable=True, blank=True)
    owner = models.ManyToManyField(User, through="Reservation")

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

# class Building(models.Model):
#     building_name = models.CharField(max_length=50)
#     programme = models.ForeignKey(Programme, on_delete=models.CASCADE)
#     #street = models.CharField(max_length=200)
#     #city_code = models.IntegerField()
#
#     def __str__(self):
#         return self.building_name

class Reservation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    programme = models.ForeignKey(Programme, on_delete=models.CASCADE)
    # building = models.ForeignKey(Building, on_delete=models.CASCADE)
    subscription_date = models.DateField(auto_now_add=True)
    app_ref = models.CharField(max_length=50)

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
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    content = RichTextField(blank=True, null=True)
    #content = models.TextField(max_length=3000)
    post_at = models.DateTimeField(auto_now_add=True)
    slug = AutoSlugField(populate_from='title', always_update=True, max_length=255, editable=True, blank=True)
    post_image = models.ImageField(null=True, blank=True, upload_to="images/")

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            # Newly created object, so set slug
            self.slug = slugify(self.slug)
        super().save(*args, **kwargs)

class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    post_at = models.DateTimeField(auto_now_add=True)
    content = models.TextField(max_length=1500, blank=True, null=True)
