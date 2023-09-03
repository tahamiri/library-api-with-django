from django.shortcuts import render
from rest_framework.views import APIView
from .models import Book
from .serializers import BookSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from rest_framework.pagination import LimitOffsetPagination
from .permissions import IsOwnerOrReadOnly


class BookReview(APIView, LimitOffsetPagination):
    
    #permission_classes = [IsAuthenticated,]
    
    def get(self, request):
        books = Book.objects.all()
        self.count = self.get_count(books)
        results = self.paginate_queryset(books, request, view=self)
        srz_data = BookSerializer(instance=results, many=True)
        return self.get_paginated_response(srz_data.data)


class BookCreate(APIView):

    permission_classes = [IsAuthenticated,]

    def post(self, request):
        srz_data = BookSerializer(data=request.data)
        if srz_data.is_valid():
            srz_data.save()
            return Response(srz_data.data, status=status.HTTP_201_CREATED)
        return Response(srz_data.errors, status=status.HTTP_400_BAD_REQUEST)
    

class BookUpdate(APIView):

    permission_classes = [IsAuthenticated,IsOwnerOrReadOnly]

    def put(self, request, pk):
        book = Book.objects.get(id=pk)
        self.check_object_permissions(request, book)
        srz_data = BookSerializer(instance=book, data=request.data, partial=True)
        if srz_data.is_valid():
            srz_data.save()
            return Response(srz_data.data, status=status.HTTP_200_OK)
        return Response(srz_data.errors, status=status.HTTP_400_BAD_REQUEST)
    

class BookDelete(APIView):

    permission_classes = [IsAuthenticated,IsOwnerOrReadOnly]

    def delete(self, request, pk):
        book =  Book.objects.get(pk=pk)
        book.delete()
        return Response({"message":"book deleted"}, status=status.HTTP_200_OK)