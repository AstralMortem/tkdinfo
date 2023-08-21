from django.http import HttpResponse
from django.shortcuts import render
from .forms import CustomUserCreationForm,TokenForm
from django.conf import settings
from .models import APIToken
from .serializers import *
from rest_framework import mixins
from rest_framework import generics
from rest_framework.exceptions import ValidationError, NotFound, AuthenticationFailed
from rest_framework.views import APIView
from rest_framework.response import Response
# Create your views here.

def index(request):
    return render(request, 'index.html', {"title": "Knowledge Base"})


def docs(request):
    belt = Regulation.objects.get(belt__kupslug="9-kup")
    belt = RegulationSerializer(belt).data
    return render(request, 'docs.html', {'belt': belt, "title": 'API'} )


def register(request):  
    if request.method == 'POST':  
        form = CustomUserCreationForm(request.POST)  
        if form.is_valid():  
            form.save()  
    else:  
        form = CustomUserCreationForm()  
    context = {  
        'form':form,
        'title': 'Sign Up'

    }  
    return render(request, 'register.html', context)  


def profile(request):
    try:
        token = APIToken.objects.get(user=request.user)
    except:
        token = None
    return render(request, 'registration/profile.html' ,{'token':token, 'title': 'Profile'})

def obtain_token(request):
    if request.method == 'POST':  
        data = {
            'user': request.user,
            'name': request.POST.get('name')
        }
        form = TokenForm(data=data)  
        if form.is_valid():  
            form.save()
            token = APIToken.objects.get(user=request.user)
            return HttpResponse(f"<p class='title'><span class='tag'>{token.token}</span></p>")
    elif request.method == 'DELETE':
        token = APIToken.objects.get(user=request.user)
        token.delete()
        return HttpResponse("<p class='title'>Успішно видалено</p>")
    else:  
        form = TokenForm()  
    context = {  
        'form':form  
    }  
    return render(request, 'token.html', context)  


class SecurePatch(object):
    def list(self, request, *args, **kwargs):
        try:
            token = APIToken.objects.get(token=kwargs.get('token'))
            return super().list(request, *args, **kwargs)
        except:
            raise AuthenticationFailed(
                {'error': "Invalid token"})
        
    def get(self, request, *args, **kwargs):
        try:
            token = APIToken.objects.get(token=kwargs.get('token'))
            return super().get(request, *args, **kwargs)
        except:
            raise AuthenticationFailed(
                {'error': "Invalid token"})

        


class VolumesList(SecurePatch,generics.ListAPIView ):
    queryset = Volume.objects.all()
    serializer_class = VolumeSerializer

    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
    
class VolumeDetail(SecurePatch, generics.ListAPIView):
    queryset = Page.objects.all()
    serializer_class = PageLinkSerializer

    def list(self, request, *args, **kwargs):
        qs = self.get_queryset()
        qs = qs.filter(tom__tom=kwargs.get('tom'))
        self.queryset = qs
        return super().list(request, *args, **kwargs)
    
class PageDetail(SecurePatch, APIView):
    def get(self, request, *args, **kwargs):
        try:
            page = Page.objects.get(tom__tom=kwargs.get('tom'), page=kwargs.get('page'))
            return Response(PageSerializer(page).data)
        except:
            raise NotFound({'error': 'Page not found'})
        
        

class BeltList(SecurePatch, generics.ListAPIView):
    queryset = Belt.objects.all()
    serializer_class = BeltSerializer

class RegulationView(SecurePatch, APIView):
    def get(self, request, *args, **kwargs):
        try:
            page = Regulation.objects.get(belt__kupslug=kwargs.get("kupslug"))
            return Response(RegulationSerializer(page).data)
        except:
            raise NotFound({'error': 'Page not found'})