from rest_framework.viewsets import ModelViewSet
from .models import Score
from .serializers import ScoreSerializer

class ScoreViewSet(ModelViewSet):
    queryset = Score.objects.all().order_by("-id")
    serializer_class = ScoreSerializer

# Create your views here.
