from django.shortcuts import render
from django.http import JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import generics,status
from rest_framework.views import APIView
from .serializers import BlogSerializers, RegisterSerializer
from .models import Blog
from rest_framework.permissions import IsAuthenticated,BasePermission, SAFE_METHODS

# Create your views here.
@api_view(('GET',))
def hello(request):
    return  Response('Item succsesfully delete!')
class PostWritePermission(BasePermission):
    message = 'editing only for users'
    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        return obj.user == request.user

class BlogList(generics.ListCreateAPIView):
   # permission_classes = [IsAuthenticated]
    queryset = Blog.objects.all()
    serializer_class = BlogSerializers
class BlogDetail(generics.RetrieveUpdateDestroyAPIView,PostWritePermission):
    permission_classes = [PostWritePermission]
    queryset = Blog.objects.all()
    serializer_class = BlogSerializers
class Register(APIView):
    def post(self,request):
        serializer = RegisterSerializer(data=request.data)
        print(request.data)
        print(serializer.is_valid())
        if serializer.is_valid():
            newuser = serializer.save()
            if newuser:
                return Response(status=status.HTTP_201_CREATED)
            
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


