from django.shortcuts import render
from rest_framework import viewsets
from .models import Student
from .serializers import StudentSerializer
from rest_framework.authentication import SessionAuthentication
from .custompermissions import MyPermission

# Create your views here.
'''ModelViewSet class creates CRUD API behind the scene without defining 
create(), get(), update() and delete() methods,'''
class StudentModelViewSet(viewsets.ModelViewSet):
    # queryset = model_name.objects.all(), Here queryset is keyword
    queryset = Student.objects.all()
    # Here, serializer_class is a keyword
    serializer_class = StudentSerializer

    '''Add SessionAuthentication to this API. If successfully autheticated,
    it provides the following credentials:
    request.user will be Django user instance
    request.auth will be None.
    Unauthenticated responses that are denied permission will result in
    in HTTP 403 Forbidden response. '''
    authentication_classes = [SessionAuthentication] 
    # Apply custom permission
    permission_classes = [MyPermission]
