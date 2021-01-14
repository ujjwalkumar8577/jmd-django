from django.contrib import admin
from home.models import Contact,Order,Party

class ContactAdmin(admin.ModelAdmin):
    list_display = ('sno','name','email','timestamp')

class OrderAdmin(admin.ModelAdmin):
    list_display = ('sno','shopname','address','i1','i2','i3','i4','i5','timestamp')

class PartyAdmin(admin.ModelAdmin):
    list_display = ('sno','area','name','contact')

# Register your models here.
admin.site.register(Contact, ContactAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(Party, PartyAdmin)


