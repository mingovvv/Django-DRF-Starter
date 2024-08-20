from rest_framework.decorators import api_view
from rest_framework.response import Response

from app.models import BlogPost


# Create your views here.

@api_view(['GET'])
def test_api(request):
    return Response({'message': 'Hello, Welcome DRF World'})