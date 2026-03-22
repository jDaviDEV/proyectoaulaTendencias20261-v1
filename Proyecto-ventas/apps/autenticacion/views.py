from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializer import LoginSerializer
from drf_yasg.utils import swagger_auto_schema
 
class LoginView(APIView):
 
    @swagger_auto_schema(
        request_body=LoginSerializer,  
        operation_description="Endpoint para autenticación de usuarios"
    )
    def post(self, request):
 
        serializer = LoginSerializer(data=request.data)
 
        if serializer.is_valid():
            user = serializer.validated_data['user']
 
            return Response({
                "message": "Login exitoso"
            }, status=status.HTTP_200_OK)
 
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)