from rest_framework import serializers
from .models import Flight, Order, Passenger, Payment_method

class FlightSerializer(serializers.ModelSerializer):
    flight_num = serializers.CharField(source='flight_id')
    arrive_date = serializers.CharField(source='arrival_date')
    arrive_time = serializers.CharField(source='arrival_time')
    class Meta:
        model = Flight
        fields = ('flight_num', 'airline', 'departure_date', 'departure_time', 'arrive_date', 'arrive_time',
                  'flight_price', 'seat_number', 'departure', 'arrival')

class paymentMethodSerializer(serializers.ModelSerializer):
    payment_platform = serializers.CharField(source='payment_platform')
    class Meta:
        model = Payment_method
        fields = ['payment_platform']