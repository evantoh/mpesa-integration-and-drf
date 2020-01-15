from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from django.http import HttpResponse


from rest_framework.views import APIView
from .models import  MwendaShop
from .serializers import ShopSerializer

from .permissions import IsAdminOrReadOnly

# Create your views here.
class MwendaList(APIView):
    # handling get method
    def get(self, request, format=None):
        all_objs = MwendaShop.objects.all()
        serializers = ShopSerializer(all_objs, many=True)
        return Response(serializers.data)

    # handling post request
    def post(self, request, format=None):
        serializers = ShopSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
    permission_classes = (IsAdminOrReadOnly,)

# get objects by id's
class MwendaDescription(APIView):
    permission_classes = (IsAdminOrReadOnly,)
    def get_single_item(self, pk):
        try:
            return MwendaShop.objects.get(pk=pk)
        except MwendaShop.DoesNotExist:
            return HttpResponse('object you are searching for Does not exist')

            # get single object
    def get(self, request, pk, format=None):
        item = self.get_single_item(pk)
        serializers = ShopSerializer(item)
        return Response(serializers.data)
        # update single object
    def put(self, request, pk, format=None):
        item = self.get_single_item(pk)
        serializers = ShopSerializer(item, request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
        else:
            return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        item = self.get_single_item(pk)
        item.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
