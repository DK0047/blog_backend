
from django.shortcuts import render
from rest_framework import viewsets
from .serializer import BlogSerializer, UserSerializer 
from .models import Blog
from django.http import JsonResponse
from django.http.response import HttpResponse
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import  render, redirect
from rest_framework.decorators import api_view
from django.contrib.auth.hashers import make_password
from django.http import HttpResponse


class Blog_detailsview(viewsets.ModelViewSet):
    serializer_class =BlogSerializer 
    queryset = Blog.objects.all()  

    def get(self,request,*args,**kwargs):
        articles = Blog.objects.all()
        serializer =BlogSerializer (articles,many=True)
        return JsonResponse(serializer.data, safe = False)

    @csrf_exempt
    def post(self,request,*args,**kwargs):
        data = JSONParser().parse(request.data)
        print (request.data)
        serializer =BlogSerializer (data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status = 201)
        return JsonResponse(serializer.errors, status = 400)


class Detailblog(viewsets.ModelViewSet):
    def get_object(pk):
        
        try:
            return Blog.object.get(pk=pk)

        except Blog.DoesNotExist:
            return HttpResponse(status=404)

    def get(self,request,*args,**kwargs):
        blog=self. get_object(kwargs['blog_id'])
        serializer = BlogSerializer(blog)
        return JsonResponse(serializer.data)

    @csrf_exempt
    def put(self,request,*args,**kwargs):   
        blog=self.get_object(kwargs['blog_id'])
        serializer =BlogSerializer(blog,request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors,status =400)

    #@csrf_exempt
    def delete(self,request,*args,**kwargs):
        blog=self.get_object(kwargs['blog_id'])
        blog.delete()
        return HttpResponse(status=204)  

@csrf_exempt   
@api_view(['POST'])
def login(request):
    user=auth.authenticate(username=request.data['username'],password=request.data['password'])
    if user is not None:
        auth.login(request,user) 
        return HttpResponse('Login in successfully')  
    else: 
        return HttpResponse(status=401)  
        
@csrf_exempt   
@api_view(['POST'])
def signup(request):
    if User.objects.filter(username=request.data['username']).exists():
        return HttpResponse('user name exists') 
    else:
        request.data['password']=make_password(request.data['password'])
        userserializer=UserSerializer(data=request.data)
        if userserializer.is_valid():
            userserializer.save()
            return JsonResponse(userserializer.data, status = 201)
        return JsonResponse(userserializer.errors, status = 400)

def post(self,request,*args,**kwargs):
    image=request.data['cover']   
    return HttpResponse({'messages':'Image created'},status=200)     


        
    
    



