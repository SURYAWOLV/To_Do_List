from .serializers import TodoSerializer
from rest_framework import viewsets
from .models import Todo

class Todoviewset(viewsets.ModelViewSet):
    queryset = Todo.objects.all().order_by('-created_at')
    serializer_class =TodoSerializer
