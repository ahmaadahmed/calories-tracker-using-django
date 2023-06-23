from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from myapp.models import Food, Consume
import jwt, datetime
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.exceptions import AuthenticationFailed
from .models import Food, Consume
from .serializers import FoodSerializer, ConsumeSerializer

# Create your views here.
@login_required
def home(request):
    return render(request, "registration/success.html", {})
 
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username = username, password = password)
            login(request, user)
            #return redirect('home')
            return render(request, "registration/new_data.html")
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})


def new_data(request):
    if request.method == "POST":
        name = request.POST['name']
        carbs = request.POST['carbs']
        protein = request.POST['protein']
        fats = request.POST['fats']
        calories = request.POST['calories']        
        food = Food(name=name, carbs=carbs, protein=protein, fats=fats, calories=calories)
        food.save()
        return render(request, "registration/new_data_added.html")

#3.1 GET POST
@api_view(['GET','POST'])
def food_list(request):
    # GET
    if request.method == 'GET':
        food_obj = Food.objects.all()
        serializer = FoodSerializer(food_obj, many=True)
        return Response(serializer.data)
    # POST
    elif request.method == 'POST':
        serializer = FoodSerializer(data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status= status.HTTP_201_CREATED)
        return Response(serializer.data, status= status.HTTP_400_BAD_REQUEST)

#3.2 GET PUT DELETE
@api_view(['GET','PUT','DELETE'])
def food_pk(request, pk):
    try:
        food_obj = Food.objects.get(pk=pk)
    except Food.DoesNotExists:
        return Response(status=status.HTTP_404_NOT_FOUND)
    # GET
    if request.method == 'GET':
        serializer = FoodSerializer(food_obj)
        return Response(serializer.data)
        
    # PUT
    elif request.method == 'PUT':
        serializer = FoodSerializer(food_obj, data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)
    # DELETE
    if request.method == 'DELETE':
        food_obj.delete()
        return Response(status= status.HTTP_204_NO_CONTENT)
    

#4.1 GET POST
@api_view(['GET','POST'])
def food_consumed_list(request):
    # GET
    if request.method == 'GET':
        companies = Consume.objects.all()
        serializer = ConsumeSerializer(companies, many=True)
        return Response(serializer.data)
    # POST
    elif request.method == 'POST':
        serializer = ConsumeSerializer(data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status= status.HTTP_201_CREATED)
        return Response(serializer.data, status= status.HTTP_400_BAD_REQUEST)

#4.2 GET PUT DELETE
@api_view(['GET','PUT','DELETE'])
def food_consumed_pk(request, pk):
    try:
        Consumed_food = Consume.objects.get(pk=pk)
    except Consume.DoesNotExists:
        return Response(status=status.HTTP_404_NOT_FOUND)
    # GET
    if request.method == 'GET':
        serializer = ConsumeSerializer(Consumed_food)
        return Response(serializer.data)
        
    # PUT
    elif request.method == 'PUT':
        serializer = ConsumeSerializer(Consumed_food, data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)
    # DELETE
    if request.method == 'DELETE':
        Consumed_food.delete()
        return Response(status= status.HTTP_204_NO_CONTENT)