from django.shortcuts import render
from rest_framework.views import APIView
from user_module.models import Item
from user_module.serializers import ItemSerializer
from rest_framework.response import Response
from rest_framework import status

# Create your views here.

class ItemView(APIView):

  def get(self, request):

    data = {
      "item_data":ItemSerializer(Item.objects.order_by("-created_at"), many=True).data  
    }

    return Response(data, status=status.HTTP_200_OK)

  def post(self, request):

    data = {
      "description":request.data["description"]
    }

    item_data = ItemSerializer(data=data)

    if item_data.is_valid():

      item_data.save()

      return Response(item_data.data, status=status.HTTP_201_CREATED)
    else:
      return Response(item_data.errors, status=status.HTTP_400_BAD_REQUEST)
  
class ItemViewUpdate(APIView):

  def get(self, request):

    data = {
      "item_data":ItemSerializer(Item.objects.get(pk=request.GET.get("id")), many=False).data  
    }

    return Response(data, status=status.HTTP_200_OK)

  def put(self, request):

    data = {
      "description":request.data["description"]
    }

    update_item_data = Item.objects.get(pk=request.data["id"])
    
    item_data = ItemSerializer(update_item_data, data=data, partial=True)

    if item_data.is_valid():

      item_data.save()

      return Response(item_data.data, status=status.HTTP_201_CREATED)
    else:
      return Response(item_data.errors, status=status.HTTP_400_BAD_REQUEST)
  
  def delete(self, request):

    item_data = Item.objects.get(pk=request.data["id"])
    
    item_data.delete()

    return Response(status=status.HTTP_200_OK)