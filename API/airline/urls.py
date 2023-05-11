from django.urls import path
from . import views

urlpatterns = [
    path('airline/', views.findflight.as_view()),
    path('paymentMethod/', views.paymentMethod.as_view()),
    path('bookingStatus/', views.bookingStatus.as_view()),
    path('bookflight/', views.bookflight.as_view()),
    path('payforbooking/', views.payforbooking.as_view()),
    path('finalizebooking/', views.finalizebooking.as_view()),
    path('cancelbooking/', views.cancelbooking.as_view()),
    ]

