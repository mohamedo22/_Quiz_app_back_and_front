from django.shortcuts import render , redirect , HttpResponseRedirect
from .models import *
from datetime import *
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
def index(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        check = "false"
        try:
            user = students.objects.get(email=email, password=password)
            if user:
                check = "true"
                send_mail("New log in" , "There is a new log in success to your account in 'Quiz app'" , settings.EMAIL_HOST_USER , [email], fail_silently=False)
                return render(request, 'home.html')
        except students.DoesNotExist:
                check = "false"
                send_mail("New log in" , "There is a new log in Failed to your account in 'Quiz app'" , settings.EMAIL_HOST_USER , [email], fail_silently=False)
                return render(request, 'Log_in_student.html', {'check': check})
    return render(request, 'Log_in_student.html')