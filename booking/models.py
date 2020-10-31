from django.db import models
from tinymce import HTMLField
from django.conf import settings
from django.urls import reverse

class OurUser(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,
                on_delete=models.CASCADE)
    
    def __str__(self):
        return self.user.username



class BookModel(models.Model):
    ouruser = models.ForeignKey(OurUser, on_delete=models.PROTECT)
    name = models.CharField(max_length=144)
    email = models.EmailField()
    phone = models.CharField(max_length=22)
    pickup = models.CharField(max_length=200)
    content = HTMLField(blank=True, null=True)
    destination = models.CharField(max_length=200)
    date = models.DateTimeField(auto_now=False, auto_now_add=False)


    class Meta:
        pass

    def __str__(self):
        return self.name


    def get_absolute_url(self):
        return reverse('booking:book-detail', kwargs={
            'pk': self.pk
        })

    def get_update_url(self):
        return reverse('booking:book-update', kwargs={
            'pk': self.pk
        })

    def get_delete_url(self):
        return reverse('booking:book-delete', kwargs={
            'pk': self.pk
        })
