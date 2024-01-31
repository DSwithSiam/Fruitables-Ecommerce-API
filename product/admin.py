from django.contrib import admin
from product.models import *

# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

class AdditionalAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(Product)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Additional, AdditionalAdmin)
admin.site.register(Review)
admin.site.register(Rateing)