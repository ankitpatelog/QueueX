from rest_framework.views import APIView
from .serializers import UserSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from django.contrib.auth import get_user_model
User = get_user_model()

class Register(APIView):
    # we can use generics for less line of code
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = UserSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()   # create() called here
            return Response(serializer.data,status=status.HTTP_201_CREATED,)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def get(self,request):
        user = User.objects.all()
        serializer = UserSerializer(user , many=True)
        return Response(serializer.data)
    
