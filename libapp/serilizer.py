
from rest_framework import serializers

from libapp.models import Userdata,Book

class Userdataserilizer(serializers.ModelSerializer):
    fname=serializers.CharField()
    lname=serializers.CharField()
    pass1=serializers.CharField()
    pass2=serializers.CharField()
    email=serializers.EmailField()

    class Meta:
        model=Userdata
        fields=("__all__")

class Bookserilizer(serializers.ModelSerializer):
    id=serializers.IntegerField()
    name=serializers.CharField()
    author=serializers.CharField()

    class Meta:
        model=Book
        fields=("__all__")
