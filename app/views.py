from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import EmployeeModel
from .my_rest_api import EmployeeSerializer
class MyEmployee(APIView):
    def get(self,request):
        qs=EmployeeModel.objects.all()
        emp=EmployeeSerializer(qs,many=True)
        return Response(emp.data)