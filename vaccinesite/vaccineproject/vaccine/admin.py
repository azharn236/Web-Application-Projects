from django.contrib import admin
from.models import Person

# Register your models here.
class PersonAdmin(admin.ModelAdmin):
    list_display = ['name', 'gender', 'age', 'date_of_birth', 'mobile_no', 'created', 'updated',]
    list_editable = ['gender', 'age', 'date_of_birth', 'mobile_no',]
    list_per_page = 20
admin.site.register(Person, PersonAdmin)