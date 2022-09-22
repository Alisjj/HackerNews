import uuid
from rest_framework.generics import ListAPIView, CreateAPIView, DestroyAPIView, UpdateAPIView
from rest_framework.permissions import AllowAny
from newsList.models import Item
from .serializers import ItemSerializer
from rest_framework.response import Response
from rest_framework import status

class ItemListView(ListAPIView):
    permission_classes = (AllowAny,)
    serializer_class = ItemSerializer
    queryset = Item.objects.all()

class CommentList(ListAPIView):
    permission_classes = (AllowAny, )
    serializer_class = ItemSerializer
    queryset = Item.objects.filter(type="comment")

class NewsCreateView(CreateAPIView):
    serializer_class = ItemSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        id = str(uuid.uuid4())[:10]
        i = serializer.save(by=request.user.username, id=id)
        self.perform_create(i)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

class ItemUpdate(UpdateAPIView):
    serializer_class = ItemSerializer

    def get_queryset(self):
        return Item.objects.filter(fetched=False)

class ItemDestroy(DestroyAPIView):
    serializer_class = ItemSerializer

    def get_queryset(self):
        return Item.objects.filter(fetched=False)