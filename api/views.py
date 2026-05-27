from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import LocationSerializer

@api_view(['POST'])
def save_location(request):
 print(request.data)
 serializer=LocationSerializer(data=request.data)
 if serializer.is_valid():
  serializer.save()
  return Response({"status":"saved"})
 return Response(serializer.errors,status=400)