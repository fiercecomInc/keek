from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required


def exam(request):
    return render(request, 'exam/exam.html')
