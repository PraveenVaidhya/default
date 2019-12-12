from django.shortcuts import render
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils import six


# Create your views here.
def index(request):
    j= six.text_type(2) + six.text_type(34343) + six.text_type()
    return render(request,'index.html')