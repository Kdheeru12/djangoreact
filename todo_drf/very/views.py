from django.db.models import query
from django.shortcuts import get_object_or_404, render
from django.http import JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import generics, serializers,status
from rest_framework.views import APIView
from .serializers import BlogSerializers, RegisterSerializer
from .models import Blog
from rest_framework.permissions import IsAuthenticated,BasePermission, SAFE_METHODS
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import viewsets
from rest_framework.decorators import action
# Create your views here.

# copied and pasted in views

# class Register(APIView):
#     def post(self,request):
#         serializer = RegisterSerializer(data=request.data)
#         print(request.data)
#         print(serializer.is_valid())
#         if serializer.is_valid():
#             newuser = serializer.save()
#             if newuser:
#                 return Response(status=status.HTTP_201_CREATED)
            
#         return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


# class BlacklistTokens(APIView):
#     def post(self,request):
#         try:
#             refresh_token = request.data["refresh_token"]
#             print(refresh_token)
#             token = RefreshToken(refresh_token)
#             token.blacklist()
#             return Response(status=status.HTTP_200_OK)
#         except Exception as e:
#             print(e)
#             return Response(status=status.HTTP_400_BAD_REQUEST)










@api_view(('GET',))
def hello(request):
    return  Response('Item succsesfully delete!')
class PostWritePermission(BasePermission):
    message = 'editing only for users'
    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        return obj.user == request.user


# Replacing by viewsets
    
# class BlogList(generics.ListCreateAPIView):
#     #permission_classes=[IsAuthenticated]
#     queryset = Blog.objects.all()
#     serializer_class = BlogSerializers
# class BlogDetail(generics.RetrieveUpdateDestroyAPIView,PostWritePermission):
#     permission_classes = [PostWritePermission]
#     queryset = Blog.objects.all()
#     serializer_class = BlogSerializers

# ViewSets and methods

# def list(self, request):
#     pass

# def create(self, request):
#     pass

# def retrieve(self, request, pk=None):
#     pass

# def update(self, request, pk=None):
#     pass

# def partial_update(self, request, pk=None):
#     pass

# def destroy(self, request, pk=None):
#     pass

# class BlogList(viewsets.ViewSet):
#     permission_classes =[IsAuthenticated]
#     queryset = Blog.objects.all()
#     def list(self,request):
#         serializer_class = BlogSerializers(self.queryset,many=True)
#         return Response(serializer_class.data)      
#     def retrieve(self, request, pk=None):
#         query = get_object_or_404(Blog,pk=pk)
#         serializer_class = BlogSerializers(query)
#         return Response(serializer_class.data)

# using modelviewsets

class BlogList(viewsets.ModelViewSet):
    serializer_class = BlogSerializers
    
    def get_queryset(self):
        return Blog.objects.all()
        
    def get_object(self,queryset=None,**kwargs):
        item = self.kwargs.get('pk')
        query = get_object_or_404(Blog,slug=item)
        return query



