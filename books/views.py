from django.shortcuts import render
from rest_framework.views import APIView
from .models import Book
from .serializers import BookSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status


class BookReview(APIView):
    
    permission_classes = [IsAuthenticated,]
    
    def get(self, request):
        books = Book.objects.all()
        srz_data = BookSerializer(instance=books, many=True)
        return Response(srz_data.data, status=status.HTTP_200_OK)


class BookCreate(APIView):

    permission_classes = [IsAuthenticated,]

    def post(self, request):
        srz_data = BookSerializer(data=request.data)
        if srz_data.is_valid():
            srz_data.save()
            return Response(srz_data.data, status=status.HTTP_201_CREATED)
        return Response(srz_data.errors, status=status.HTTP_400_BAD_REQUEST)
    

class BookUpdate(APIView):

    permission_classes = [IsAuthenticated,]

    def put(self, request, pk):
        book = Book.objects.get(id=pk)
        srz_data = BookSerializer(instance=book, data=request.data, partial=True)
        if srz_data.is_valid():
            srz_data.save()
            return Response(srz_data.data, status=status.HTTP_200_OK)
        return Response(srz_data.errors, status=status.HTTP_400_BAD_REQUEST)
    

class BookDelete(APIView):

    permission_classes = [IsAuthenticated,]

    def delete(self, request, pk):
        book =  Book.objects.get(pk=pk)
        book.delete()
        return Response({"message":"book deleted"}, status=status.HTTP_200_OK)