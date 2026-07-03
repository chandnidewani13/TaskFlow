from rest_framework.decorators import api_view

from rest_framework.response import Response

from .models import Project, Task

from .serializers import (

ProjectSerializer,

TaskSerializer
)


@api_view(['GET'])

def project_api(request):

    projects = Project.objects.all()

    serializer = ProjectSerializer(

        projects,

        many=True
    )

    return Response(serializer.data)


@api_view(['GET'])

def task_api(request):

    tasks = Task.objects.all()

    serializer = TaskSerializer(

        tasks,

        many=True
    )

    return Response(serializer.data)