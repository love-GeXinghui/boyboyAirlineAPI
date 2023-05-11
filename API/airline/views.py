import json
import random
import urllib
from urllib import request

from django.db.models import Count
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import serializers
from .models import Flight, Order, Passenger, Payment_method
from django.views.decorators.http import require_GET
from django.http import JsonResponse
from .serializers import FlightSerializer, paymentMethodSerializer
import requests
from django.http import HttpRequest
# Create your views here.

class findflight(APIView):
    @staticmethod
    def get(request):
        if request.method == 'GET':
            """
            """
            req = request.query_params.dict()
            departure = req['departure']
            arrival = req['arrival']
            departure_date = req['departure_date']
            flights = Flight.objects.filter(
                departure=departure,
                arrival=arrival,
                departure_date=departure_date,
            )
            Data = {
                "code":"200",
                "msg":"successful"
            }

            serializer = FlightSerializer(flights, many=True)
            Data["data"] = serializer.data[0]
            return JsonResponse(Data, safe=False)
        elif request.method == 'POST':
            Data = {
                "code": "503",
                "msg": "错了哥们，这是get, 你怎么还用POST呢"
            }
            return JsonResponse(Data, safe=False)

class paymentMethod(APIView):
    @staticmethod
    def get(request):
        """
        """
        method = Payment_method.objects.values_list()
        list = []
        print(method)
        for i in method:
            str = i[1]
            list.append(str)

        Data = {
            "code": "200",
            "msg": "successful"
        }

        Data["data"] =[{"payment_platform": list}]
        return JsonResponse(Data, safe=False)

class bookingStatus(APIView):
    @staticmethod
    def get(request):
        """
        """
        req = request.query_params.dict()

        order_id = Order.objects.get(
            order_id=req['order_id'],
        )
        flight = order_id.flight_id
        flights = Flight.objects.filter(flight_id=flight)

        Data = {
            "code": "200",
            "msg": "successful"
        }
        serializer = FlightSerializer(flights, many=True)
        list =  serializer.data[0]
        list['order_id'] = order_id.order_id
        list['payment_status'] = order_id.payment_status
        list['ticket_time'] = order_id.ticket_time
        list.update({'flight_id': list.pop('flight_num')})
        del list["airline"]
        del list["seat_number"]

        Data["data"] = list

        return JsonResponse(Data, safe=False)

class bookflight(APIView):
    @staticmethod
    def post(request):


        temp = []
        tt = []
        data = json.loads(request.body)
        flight_num = data.get("flight_num")
        passenger_name = data["passenger_name"]
        order_id = data.get('order_id')
        order_price = data.get('order_price')
        ticket_time = data.get('ticket_time')
        payment_status = data.get('payment_status')

        AID = random.randint(1, 999999)

        list_length = len(passenger_name)

        flights = Flight.objects.get(flight_id=flight_num)
        set = flights.seat_number
        flights.seat_number = set - list_length
        flights.save()
        order_id.flight_id = flight_num
        order_id.save()

        for item in passenger_name:
            new_Passenger = Passenger.objects.create(passenger_name = item)
            temp.append(new_Passenger.pk)


        print(temp)

        new_Order = Order.objects.create(order_id=order_id, AID=AID, order_price=order_price,
                                         ticket_time=ticket_time, payment_status=payment_status,
                                         )
        new_Order.passenger_id.set(temp)


        Data = {
            "code": "200",
            "msg": "successful",
            "data": {"booking_status": "booking successful"}
        }
        return JsonResponse(Data, safe=False)



class finalizebooking(APIView):
    @staticmethod
    def post(request):
        data = json.loads(request.body)
        key1 = data.get("key")
        order_id = data.get("order_id")


        order_id = Order.objects.get(order_id=order_id)
        key2 = order_id.key
        if key2 == key1 :
            Data = {
                "code": "200",
                "msg": "successful",
                "data":  {"payment_status":"1"}
            }
            return JsonResponse(Data, safe=False)



class payforbooking(APIView):
    @staticmethod
    def post(request):
        data = json.loads(request.body)
        payment_platform = data.get("payment_platform")
        order_id = data.get("order_id")


        order_id = Order.objects.get(order_id=order_id)
        order_id.paymet_platform =  payment_platform



        url = 'http://bamboo.pythonanywhere.com/invoice/'
        data = {
            "orderId":order_id.order_id,
            "AID" : order_id.AID,
            "totalAmount": order_id.order_price,
            "airline":"boyboy"
        }

        # data = {
        #     "orderId": 1,
        #     "AID" : 1,
        #     "totalAmount": 100,
        #     "airline":"airline1"
        # }
        headers = {'Content-Type': 'application/json'}
        json_data = json.dumps(data)
        response = requests.post(url, data=json_data, headers=headers)

        response_data = json.loads(response.text)
        print(response_data)
        gainData = response_data["data"]
        PID = gainData["PID"]
        key = gainData["key"]
        price = gainData["totalAmount"]

        print(order_id)
        print(PID)
        print(key)
        print(order_id.PID)
        order_id.PID = PID
        print(order_id.PID)
        print( order_id.key)
        order_id.key = key
        print(price)
        order_id.payment_status = "1"
        order_id.order_price = price
        print(price)
        order_id.save()
        list  = {}
        list["AID"] = order_id.order_id
        list["PID"] = PID
        list["order_price"] = order_id.order_price
        list["order_id"] = order_id.order_id
        Data = {
            "code": "200",
            "msg": "successful",
            "data": list
        }
        return JsonResponse(Data, safe=False)


class cancelbooking(APIView):
    @staticmethod
    def post(request):
        data = json.loads(request.body)
        payment_platform = data.get("payment_platform")
        order_id = data.get("order_id")
        print(order_id)
        order_id = Order.objects.get(order_id=order_id)
        order_id.payment_status = "2"
        order_id.save()

        flights = Flight.objects.get(flight_id=order_id.flight_id)

        passenger = Order.objects.filter(order_id=order_id.order_id).annotate(num_passengers=Count('passenger_id'))
        for n in passenger:
            print(n.order_id)
            flights.seat_number += n.order_id

        flights.save()
        print(flights.seat_number)
        Data = {
            "code": "200",
            "msg": "successful",
            "data": {"cancel":"cancel successful"}
        }
        return JsonResponse(Data, safe=False)



