from django.shortcuts import render
from django.http import JsonResponse 
import json 
from django.views.decorators.csrf import csrf_exempt

students =[]
@csrf_exempt
def student_api(request):
    if request.method =='GET':
        return JsonResponse(students , safe=False)
    if request.method =='POST':
        data =json.loads(request.body)
        
        if not data.get('name')or not data.get('email'):
            return JsonResponse({
                'message':'All fields required'
            }, status = 400)
            
        students.append(data)
        
        return JsonResponse({
            'message':'student added',
            'data':data
        },status = 201)

# Create your views here.
