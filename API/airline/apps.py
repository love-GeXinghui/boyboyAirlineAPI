from django.apps import AppConfig


class AirlineConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "airline"

class paymentMethodConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "paymentMethod"

class bookingstatusMethodConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "bookingStatus"

class bookingflightMethodConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "bookingflight"

class payforbookingMethodConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "payforbooking"

class finalizebookingMethodConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "finalizebooking"


class cancelbookingMethodConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "cancelbooking"
