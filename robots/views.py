from rest_framework import generics
from .models import Robot
from .serializers import RobotSerializer
from django.shortcuts import render
from django.http import HttpResponse
from .models import Robot
from openpyxl import Workbook
import csv

class RobotListCreateView(generics.ListCreateAPIView): # Api-endpoint с помощью django_rest_framework 
    queryset = Robot.objects.all()
    serializer_class = RobotSerializer

def downloadRobotsPage(req): # Скачивание данные на файле excl
    robot = Robot.objects.all()
    response = HttpResponse(robot , content_type='application/vnd.ms-excel;charset=utf-8')
    response['Content-Disposition'] = 'attachment; filename="robots.xls"'

    writer = csv.writer(response)
    writer.writerow(['Модель', 'Версия', 'Количество за неделю'])
    for robot in robot:
        writer.writerow([robot.model, robot.version, robot.quantity])

    return response