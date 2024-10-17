from rest_framework import Response
from rest_framework.decorators import api_view
from .models import MenuItem

# Create your views here.
@api_view()
def menu_items(request):
    items = MenuItem.objects.all
    return Response(items.values())