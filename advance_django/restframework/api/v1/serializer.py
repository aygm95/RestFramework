from rest_framework import serializers

class postSerializer(serializers.Serializer):
    title=serializers.CharField(maxlength=250)