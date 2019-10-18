from django.db import models
from django.shortcuts import reverse


class Profile(models.Model):
    user = models.OneToOneField('auth.user', on_delete=models.CASCADE,
        null=True)
    created = models.DateField(auto_now=True)
    email = models.EmailField(blank=True, default="", max_length=254)
    photo = models.ImageField(upload_to='profiles')
    date_of_birth = models.DateField(blank=True, null=True)
    bio = models.TextField(blank=True, default="")


    def __str__(self):
        return self.user.username

    def get_absolute_url(self):
        return reverse("profile-details", kwargs={"pk": self.pk})
    