from rest_framework.views import APIView
from rest_framework.response import Response
from .models import User
from .serializers import UserRegisterSerializer, UserUpdateSerializer
from rest_framework import status
from rest_framework.permissions import IsAuthenticated


class UserRegister(APIView):
    def post(self, request):
        ser_data = UserRegisterSerializer(data= request.POST)
        if ser_data.is_valid():
            ser_data.create(ser_data.validated_data)
            return Response(ser_data.data, status=status.HTTP_201_CREATED)
        return Response(ser_data.errors, status=status.HTTP_400_BAD_REQUEST)


class UserReview(APIView):

    permission_classes = [IsAuthenticated,]

    def get(self, reauest):
        users = User.objects.all()
        ser_data = UserRegisterSerializer(instance=users, many=True)
        return Response(ser_data.data, status=status.HTTP_200_OK)


class UserUpdate(APIView):

    permission_classes = [IsAuthenticated,]

    def put(self, request, pk):
        user = User.objects.get(id=pk)
        ser_data = UserUpdateSerializer(instance=user, data=request.POST, partial=True)
        if ser_data.is_valid():
            ser_data.save()
            return Response(ser_data.data, status=status.HTTP_200_OK)
        return Response(ser_data.errors, status=status.HTTP_400_BAD_REQUEST)
    

class UserDelete(APIView):

    permission_classes = [IsAuthenticated,]
    
    def delete(self, request, pk):
        user = User.objects.get(pk=pk)
        user.delete()
        return Response({"message":"user deleted"}, status=status.HTTP_200_OK)



