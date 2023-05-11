from django.urls import path
from . import views

urlpatterns = [
    path('boyboy/findflight/', views.findflight.as_view()),
    path('boyboy/paymentMethod/', views.paymentMethod.as_view()),
    path('boyboy/bookingStatus/', views.bookingStatus.as_view()),
    path('boyboy/bookflight/', views.bookflight.as_view()),
    path('boyboy/payforbooking/', views.payforbooking.as_view()),
    path('boyboy/finalizebooking/', views.finalizebooking.as_view()),
    path('boyboy/cancelbooking/', views.cancelbooking.as_view()),
    ]
