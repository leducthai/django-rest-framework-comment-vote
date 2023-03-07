from rest_framework import serializers
from rest_framework.response import Response

def no_fuck_in_comment(value):
    if 'fuck' in value.lower():
        raise serializers.ValidationError("be polite bro !")