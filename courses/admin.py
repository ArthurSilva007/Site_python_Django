from django.contrib import admin
from .models import Home, About, Contact, ContactMessage

@admin.register(Home)
class HomeAdmin(admin.ModelAdmin):
    list_display = ('id','title')
    
@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'subject')

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'address')
    

# Register your models here.
