from django.db.models import query
from django.shortcuts import get_object_or_404, render
from django.http import JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import generics, serializers,status,authentication
from rest_framework.views import APIView
from .serializers import GetUser, RegisterSerializer
from rest_framework.permissions import IsAuthenticated,BasePermission, SAFE_METHODS
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import viewsets
from rest_framework.decorators import action
from .models import User

# Create your views here.
@api_view(('GET',))
def hello(request):
    return  Response('Item succsesfully delete!')
class PostWritePermission(BasePermission):
    message = 'editing only for users'
    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        return obj.id == request.user.id


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


class BlacklistTokens(APIView):
    def post(self,request):
        try:
            refresh_token = request.data["refresh_token"]
            print(refresh_token)
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response(status=status.HTTP_200_OK)
        except Exception as e:
            print(e)
            return Response(status=status.HTTP_400_BAD_REQUEST)


class Users(viewsets.ModelViewSet):
    serializer_class = RegisterSerializer
    queryset = User.objects.all()
    authentication_classes =(authentication.TokenAuthentication,)
    permission_classes = (PostWritePermission,)
    # def get_queryset(self):
    #     user = self.request.user.id
    #     # return get_object_or_404(User,id=user)
    #     return User.objects.filter(id=user)

class GETUSER(generics.ListAPIView):
    serializer_class = GetUser
    authentication_classes =(authentication.TokenAuthentication,)
    # permission_classes = [IsAuthenticated]
    def get_queryset(self):
        user = self.request.user.id
        print(user)
        # return get_object_or_404(User,id=user)
        return User.objects.filter(id=user)



