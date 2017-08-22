# -*- coding: utf-8 -*-
from django.contrib import admin
from TestModel.models import Test, Contact, Tag

# Register your models here.
admin.site.register([Test, Contact, Tag])

"""
# add只显示name和email
class ContactAdmin(admin.ModelAdmin):
    fields = ('name', 'email')

admin.site.register(Contact, ContactAdmin)
admin.site.register([Test, Tag])"""