from django.shortcuts import render

# Create your views here.

class ItemApiView(generics.ListAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer