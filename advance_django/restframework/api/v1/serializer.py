from rest_framework import serializers
from advance_django.models import Comments
# class PostSerializer(serializers.Serializer):
#     title=serializers.CharField()
#     email=serializers.EmailField()

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model=Comments
        fields=['title','email']