from django.contrib import admin
from store.models.products import *

admin.site.register(Products)
admin.site.register(Image)
admin.site.register(Category)
admin.site.register(CategoryGender)
admin.site.register(CategorySize)
admin.site.register(CategoryColor)
