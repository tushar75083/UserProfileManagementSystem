from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import UserProfile
from .serializers import UserProfileSerializer


# Create your views here.

# Get All List and Create View
# /api/profiles/
@api_view(['GET','POST'])
def user_profile_list(request):
    if request.method == "GET":
        # retrive all records
        # serialization
        profiles=UserProfile.objects.all()
        serializer=UserProfileSerializer(profiles, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    elif request.method == "POST":
        # create new user profile
        # deserialization
        serializer=UserProfileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        


# Get by Id,Update,Delete View
# /api/profiles/<id>/
@api_view(['GET','PUT','PATCH','DELETE'])
def user_profile_detail(request,pk):
    try:
        profile=UserProfile.objects.get(pk=pk)
    except UserProfile.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    # get single profile => serialization
    if request.method == "GET":
        serializer=UserProfileSerializer(profile)
        return Response(serializer.data)
    
    # complete update => deserialization
    elif request.method == "PUT":
        serializer = UserProfileSerializer(profile, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # partial update => deserialization
    elif request.method == "PATCH":
        serializer = UserProfileSerializer(profile, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    # delete single profile => deserialization
    elif request.method == "DELETE":
        profile.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

