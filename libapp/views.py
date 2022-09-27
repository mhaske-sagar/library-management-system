from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from libapp.models import Book, Userdata

from libapp.serilizer import Userdataserilizer,Bookserilizer

@api_view(["POST"])
def register(request):
    client=request.data
    try:
        usersfromdb=Userdata.objects.get(email=client["email"])
        if usersfromdb.email==client["email"]:
            response=Response({"user already present"})
            return response
    except Userdata.DoesNotExist:
        usersfromdb=None
        Userdata.objects.create(fname=client["fname"],lname=client["lname"],pass1=client["pass1"],pass2=client["pass2"],email=client["email"])
        response=Response({"successful"})
        return response
            #serializer=Userdataserilizer(data=request.data)
            #if serializer.is_valid():
                #serializer.save()
            #return Response(serializer.data)


@api_view(["POST"])
def login(request):
    userfromclient=request.data
    try:
        usersfromdb=Userdata.objects.get(email=userfromclient["email"])
    
        if usersfromdb.email==userfromclient["email"] and usersfromdb.pass1==userfromclient["pass1"]:
            response=Response({"login"})
        
            return response
    except Userdata.DoesNotExist:
        userfromdb=None 
        response=Response({"not exit"})
        return response
        

@api_view(["POST"])
def add(request):
    serializer=Bookserilizer(data=request.data)
    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)
@api_view(["GET"])
def get(request,id):
    userfromclient=request.data
    userfromdb=Book.objects.get(id=id)
    serializer=Bookserilizer(userfromdb)
    return Response(serializer.data)
@api_view(["PUT"])
def update(request):
    userfromclient=request.data
    userfromdb=Book.objects.get(id=userfromclient['id'])
    serializer=Bookserilizer(userfromdb,data=userfromclient,partial=False)
    if serializer.is_valid():
        serializer.save()
    return Response()

@api_view(["DELETE"])
def delete(request,id):
    userfromclient=request.data
    
    Book.objects.filter(id=id).delete()
    response=Response("data deleted")
    return  response
@api_view(["GET"])
def getall(request):
    
    userfromdb=Book.objects.all()
    serializer=Bookserilizer(userfromdb,many=True)
    return Response(serializer.data)
