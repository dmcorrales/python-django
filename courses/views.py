from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from.models import Course, Lesson

def course_list(request):
    courses = Course.objects.all()
    return render(request, 'courses/course_list.html', {'courses': courses})

def course_detail(request,pk):
    #courses = Course.objects.get(pk=pk)
    courses = get_object_or_404(Course, pk=pk)
    return render(request, 'courses/course_detail.html', {'course': courses})


def lesson_detail(request,course_pk, lesson_pk):
    lessons = get_object_or_404(Lesson, course_id=course_pk, pk=lesson_pk)
    return render(request,'courses/lesson_detail.html', {'lesson': lessons})

