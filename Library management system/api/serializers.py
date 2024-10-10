from rest_framework import serializers
from base.models import Authors,Genre,Books

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model=Authors
        fields="__all__"
        
class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model=Genre
        fields="__all__"
        
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model=Books
        fields="__all__"