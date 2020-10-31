from django.contrib import admin

# Register your models here.
from .models import BookModel, OurUser

admin.site.register(BookModel)
admin.site.register(OurUser)