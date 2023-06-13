from rest_framework import serializers
from .models import MyModel, Post
class InteractSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyModel
        fields = ["name", "email", "password"]

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'
