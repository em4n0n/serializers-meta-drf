from rest_framework import Response
from rest_framework.decorators import api_view
from .models import MenuItem
from .serializers import MenuItemSerializer
# Create your views here.
@api_view()
def menu_items(request):
    items = MenuItem.objects.all
    serialized_item = MenuItemSerializer(items, many=True)
    return Response(serialized_item.data)

def single_item(request, id):
    item = MenuItem.objects.get(pk=id)
    serialized_item = MenuItemSerializer(item)
    return Response(serialized_item.data)