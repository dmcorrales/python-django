from django.shortcuts import render
from django.http import HttpResponse

from.models import Course

def course_list(request):
    courses = Course.objects.all()
    return render(request, 'courses/course_list.html', {'courses': courses})

def course_detail(request,pk):
    courses = Course.objects.get(pk=pk)
    return render(request, 'courses/course_detail.html', {'course': courses})
