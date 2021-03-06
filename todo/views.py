from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import viewsets
from django.http import HttpResponse
from .serializers import TodoSerializer
from rest_framework import status
from rest_framework import permissions
from django.forms.models import model_to_dict
from .models import Todo
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status
from rest_framework.decorators import api_view

# # Create your views here.
@api_view(['GET', 'POST', 'DELETE'])
def todos_list(request):
    if request.method == 'GET':
        serializer_class = TodoSerializer
        queryset = Todo.objects.all()
        dates = []
        response = {}
        todos={}
        line = []
        for i in queryset:
            d = str(i.date_created)
            if d not in dates:
                dates.append(d)
            for date in dates:
                for k in queryset:
                    kdate=str(k.date_created)
                    if kdate == date:
                        to_dict=model_to_dict(k)
                        line.append(to_dict)
                todos[date]=line.copy()
                line.clear()
            response["dates"]=dates
            response['todos']=todos
        return JsonResponse(response, safe=False)
    
    elif request.method == 'POST':
        todo_data = JSONParser().parse(request)
        todo_serializer = TodoSerializer(data=todo_data)
        if todo_serializer.is_valid():
            todo_serializer.save()
            return JsonResponse(todo_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(todo_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # elif request.method == 'DELETE':
    #     count = Todo.objects.all().delete()
    #     return JsonResponse({'message': '{} Todos were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'PUT', 'DELETE'])
def todo_detail(request, todo_id):
    try: 
        todo = Todo.objects.get(pk=todo_id) 
    except Todo.DoesNotExist: 
        return JsonResponse({'message': 'The todo does not exist'}, status=status.HTTP_404_NOT_FOUND) 
 
    if request.method == 'GET': 
        todo_serializer = TodoSerializer(todo) 
        return JsonResponse(todo_serializer.data) 
 
    elif request.method == 'PUT': 
        todo_data = JSONParser().parse(request) 
        todo_serializer = TodoSerializer(todo, data=todo_data) 
        if todo_serializer.is_valid(): 
            todo_serializer.save() 
            return JsonResponse(todo_serializer.data) 
        return JsonResponse(todo_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
 
    elif request.method == 'DELETE': 
        todo.delete() 
        return JsonResponse({'message': 'Todo was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
    



        

