from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET','POST'])
def index(request):
    if request.method=='GET':
        request_data=["get"]
        return Response(data=request_data, status=status.HTTP_200_OK)
    elif request.method=='POST':
        request_data=["POST"]
        return Response(data=request_data, status=status.HTTP_200_OK)
