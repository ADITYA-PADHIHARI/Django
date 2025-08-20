from django.http import HttpResponse
from django.shortcuts import render

def homepage(request):
    data={
        'title': 'Welcome to MyTech',
        'bdata':  ' Welcome',
        'clist': ['Python', 'Django', 'JavaScript', 'React'],
        'student_details': [
            {'name': 'Alice', 'age': 20, 'course': 'Python'},
            {'name': 'Bob', 'age': 22, 'course': 'Django'},
            {'name': 'Charlie', 'age': 23, 'course': 'JavaScript'}
        ]
    }
    return render(request, "index.html", data)
def aboutus(request):
    return HttpResponse("<b>We are a tech company<b>")
def course(request):
    return HttpResponse("We offer a variety of courses")
def coursedetails(request,courseid):
    return HttpResponse(courseid)