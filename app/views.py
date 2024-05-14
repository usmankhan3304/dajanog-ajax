from django.shortcuts import render,HttpResponse
from django.http import JsonResponse
from django.forms import model_to_dict
from .models import *
from django.core import serializers
# Create your views here.
def home(request):
    officeform=OfficeForm
    empform=EmployeeForm
    context={
        'officeform':officeform,
        'empform':EmployeeForm
    }

    return render(request,'app/index.html',context=context)


def officeCrud(request):
    if request.method == 'POST':
        form = OfficeForm(request.POST)
        if form.is_valid():
            instance = form.save()
            # Convert model instance to dictionary
            instance_dict = model_to_dict(instance)
            return JsonResponse({'data': instance_dict, 'message': 'Data saved successfully.'})
        else:
            errors = form.errors.as_json()
            return JsonResponse({'error': errors}, status=400)
    else:
        return JsonResponse({'error': 'Invalid request method.'}, status=400)
def empCrud(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            instance = form.save()
            # Convert model instance to dictionary
            instance_dict = model_to_dict(instance)
            return JsonResponse({'data': instance_dict, 'message': 'Data saved successfully.'})
        else:
            errors = form.errors.as_json()
            return JsonResponse({'error': errors}, status=400)
    else:
        return JsonResponse({'error': 'Invalid request method.'}, status=400)
def getoffices(request):
    offices=Office.objects.all()
    data=serializers.serialize('json',offices)
    return JsonResponse(data,safe=False)