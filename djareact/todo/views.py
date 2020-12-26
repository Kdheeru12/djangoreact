import re
from django.shortcuts import get_object_or_404, render,redirect
from django.contrib.auth.models import User,auth
from django.http import HttpResponse,JsonResponse
from rest_framework import serializers
from .serializers import TodoSerializer
from rest_framework.parsers import JSONParser
from .models import Todo
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.
@api_view(['GET'])
def hello(request):
    a = {
        'hhhhh'
    }
    return Response(a)
@api_view(['POST'])
def create(request):
    serializer = TodoSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)  
@api_view(['GET'])
def todos(request):
    todo = Todo.objects.all()
    serializer = TodoSerializer(todo,many=True)
    return Response(serializer.data)
@api_view(['Delete'])
def delete(request,id):
    todo = Todo.objects.get(id=id)
    todo.delete()
    return Response(request.data)

# @api_view(['POST'])
# def update(request,id):
#     instance = get_object_or_404(Todo,id=id)
#     serializer = TodoSerializer(instance=instance,data=request.data or None)
#     print(request.data)
#     print(serializer)
#     if serializer.is_valid():
#         serializer.save()
#     return Response(serializer.data) 

@api_view(['POST'])
def taskUpdate(request, pk):
	task = Todo.objects.get(id=pk)
	serializer = TodoSerializer(instance=task, data=request.data)

	if serializer.is_valid():
		serializer.save()

	return Response(serializer.data)


