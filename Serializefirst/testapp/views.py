from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from rest_framework.renderers import JSONRenderer
from .models import Student
from .serializers import StudentSerializer

def student_detail(request,pk):
    stu=Student.objects.get(id=pk)
    print(stu)
    serialized=StudentSerializer(stu)
    print(serialized)
    print(serialized.data)

    json_data=JSONRenderer().render(serialized.data)
    return HttpResponse(json_data,content_type='application/json')
    # return JsonResponse(serialized.data)

def student_list(request):
    stu=Student.objects.all()
    print(stu)
    serialized=StudentSerializer(stu, many=True)
    print(serialized)
    print(serialized.data)

    # json_data=JSONRenderer().render(serialized.data)
    # return HttpResponse(json_data,content_type='application/json')
    return JsonResponse(serialized.data,safe=False)

