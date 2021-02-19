from django.db.models import query
from django.shortcuts import get_object_or_404, render
from django.http import JsonResponse
from rest_framework import response

from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import generics, serializers,status
from rest_framework.views import APIView
from .serializers import BlogSerializers, RegisterSerializer,GroceriesSerializer
from .models import Blog,Groceries
from rest_framework.permissions import IsAuthenticated,BasePermission, SAFE_METHODS
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import viewsets
from rest_framework.decorators import action 
from rest_framework import filters
from rest_framework.pagination import PageNumberPagination
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
    
# class BlogList(generics.ListAPIView):
#     #permission_classes=[IsAuthenticated]
#     queryset = Blog.objects.all()
    
#     serializer_class = BlogSerializers
    
# class BlogDetail(generics.RetrieveUpdateDestroyAPIView,PostWritePermission):
#     permission_classes = [PostWritePermission]
#     queryset = Blog.objects.all()
#     serializer_class = BlogSerializers

#     def get_object(self,queryset=None,**kwargs):
#         item = self.kwargs.get('pk')
#         query = get_object_or_404(Blog,slug=item)
#         return query


# using django filters pypi
# class BlogFilter(filters.FilterSet):
#     class Meta:
#         model = Blog
#         fields = ['slug','id']


# # using drf filters
# class ProductList(generics.ListAPIView):
#     queryset = Blog.objects.all()
#     serializer_class = BlogSerializers
#     filter_backends = [filters.SearchFilter]
#     search_fields = ['^slug']


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
#     queryset = Blog.objects.all()
    
#     permission_classes_by_action = {'list': [IsAuthenticated],
#                                     'create':[IsAuthenticated]}
#     def list(self,request):
#         serializer_class = BlogSerializers(self.queryset,many=True)
#         return Response(serializer_class.data)      
#     def retrieve(self, request, pk=None):
#         query = get_object_or_404(Blog,slug=pk)
#         serializer_class = BlogSerializers(query)
#         return Response(serializer_class.data)
#     def create(self,request):
#         serializer_class =BlogSerializers(data=request.data)
#         if serializer_class.is_valid():
#             serializer_class.user = request.user
#             print(serializer_class.user)
#             serializer_class.save()
#         else:
#             return Response(serializer_class.error_messages)
#         return Response(serializer_class.data)
#     def update(self,request,pk=None):
#         serializer_class =BlogSerializers(data=request.data)
#         if serializer_class.is_valid():
#             serializer_class.user = request.user
#             print(serializer_class.user)
#             serializer_class.save()
#         else:
#             return Response(serializer_class.error_messages)
#     def get_permissions(self):
#         try:
#             # return permission_classes depending on `action` 
#             return [permission() for permission in self.permission_classes_by_action[self.action]]
#         except KeyError: 
#             # action is not set return default permission_classes
#             return [permission() for permission in self.permission_classes]

# using modelviewsets

class BlogList(viewsets.ModelViewSet):
    serializer_class = BlogSerializers
    
    def get_queryset(self):
        permission_class = [IsAuthenticated]
        return Blog.objects.all()
        
    def get_object(self,queryset=None,**kwargs):
        item = self.kwargs.get('pk')
        query = get_object_or_404(Blog,slug=item)
        return query

# class GroceriesList(viewsets.ModelViewSet):
#     serializer_class = GroceriesSerializer
#     filter_backends = [filters.SearchFilter]
#     search_fields = ['^title','^description']
#     ordering_fields = ['price']
#     pagination_class = PageNumberPagination
#     def get_queryset(self):
#         queryset = Groceries.objects.all()
#         price = self.request.query_params.get('price', None)
#         if price is not None:
#             queryset = queryset.filter(price=price)
#         return queryset
class GroceriesList(generics.ListAPIView):
    queryset = Groceries.objects.all()
    serializer_class = GroceriesSerializer
    pagination_class=PageNumberPagination
    filter_backends = [filters.SearchFilter,filters.OrderingFilter]
    search_fields = ['^title','^description']
    filterset_fields = ['price']
    ordering_fields = ['price','created']

    # ordering_fields = ['price']

