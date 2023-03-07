from django.shortcuts import render
from rest_framework import generics
from .models import comment
from .serializers import comment_serializer
from rest_framework.response import Response

# Create your views here.
class CommentListCreateApiView(
    generics.ListCreateAPIView,):
    queryset = comment.objects.all()
    serializer_class = comment_serializer

    def get_queryset(self , *args , **kwargs):
        qs = super().get_queryset(*args , **kwargs)
        pd = self.request.GET.get('pd')
        if pd:
            qs = qs.filter(pd_id=pd)

        return qs
    
    def perform_create(self, serializer):
        if serializer.is_valid(raise_exception=True):
            serializer.save()
        return Response({"invalid":"bad word in comment or bad request"})

comment_list_create = CommentListCreateApiView.as_view()



