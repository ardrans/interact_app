from django.shortcuts import render, redirect
from django.http import JsonResponse
from .forms import RegisterForm
from django.core.exceptions import ValidationError
from .models import MyModel
import hashlib
from utils.utils import *



def create_user(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password_validation(password)
        if not password_validation():
            raise ValidationError('incorrect password format')
        confirm_password = request.POST.get('confirm_password')
        if not password == confirm_password:
            raise ValidationError('mismatch in password')
        if not name or not email or not password:
            raise ValidationError('required field is missing')
        password = hashlib.md5(password.encode()).hexdigest()

        MyModel.objects.create(name=name, email=email, password=password)
        return JsonResponse({'Success':True,'message':'You have successfully signed up'})
    else:
        return JsonResponse({'Success':False,'message':'Something went wrong'})

 def verify_email():
             key = request.args.get('key')
             if not key:
                 raise ValidationError('Key is missing')




