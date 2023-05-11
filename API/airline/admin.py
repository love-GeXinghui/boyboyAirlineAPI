from django.contrib import admin
from .models import Flight
from .models import Order
from .models import Passenger

admin.site.register(Flight)
admin.site.register(Order)
admin.site.register(Passenger)

# Register your models here.
