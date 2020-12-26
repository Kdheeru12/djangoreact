from django.db import models
from django.db.models import fields
from rest_framework import serializers
from .models import Blog,User

class BlogSerializers(serializers.ModelSerializer):
    class Meta:
        model=Blog
        fields = ['title','content',"categories",'user','id']

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('email','username','password')
        extra_kwargs = {'password':{'write_only':True}}
    def create(self, validated_data):
        password = validated_data.pop('password',None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance