from django.contrib import admin

# Register your models here.
from .models import Customer
from .models import Contact

admin.site.register(Customer)

admin.site.register(Contact)