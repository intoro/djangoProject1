from django.contrib import admin

from .models import Listing

class ListingAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'is_published', 'price', 'realtor', 'city', 'state')
    list_display_links = ('id', 'title')
    list_filter = ('realtor',)
    list_editable = ('is_published', 'price')
    list_per_page = 25
    search_fields = ('title', 'descriptions', 'address', 'city', 'state', 'zipcode')

admin.site.register(Listing, ListingAdmin)
