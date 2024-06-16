from django.shortcuts import render
from django.http import HttpResponse

#import DRF views 
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.authentication import SessionAuthentication, BasicAuthentication,TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import authenticate
#


#import models and serializers
from .models import UploadMedia
from .serializers import upload_img_gallery_serializer
import logging
# Create your views here.

class health_api(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    
    def get(self, request):
        try:
            return Response({'msg': 'API server working'}, status=status.HTTP_200_OK)
        except:
            return Response({'msg': 'API server is not working'}, status=status.HTTP_400_BAD_REQUEST)





        
class UploadImgGallery(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        user = request.user
        data = request.data
        data['upload_user'] = user.id

        serializer = upload_img_gallery_serializer(data=data)
        
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Image Gallery Saved'}, status=status.HTTP_201_CREATED)
        
        # Handle case when serializer is not valid
        return Response(status=status.HTTP_400_BAD_REQUEST)

