from rest_framework.views import APIView
from .models import vote
from .serializers import vote_serializer
from rest_framework.response import Response
from rest_framework import generics

# Create your views here.
class detailVote(APIView):

    def get(self , request, *args , **kwargs):
        pd_id = request.GET.get('pd')
        query = vote.objects.all()
        if pd_id:
            query = vote.objects.filter(pd_id = pd_id)
        data = vote_serializer(query , many= True).data
        return Response(data)
    
    def post(self , request , *args , **kwargs):
        user = request.data['user_id']
        pd = request.data['pd_id']
        if not pd or not user:
            return Response({"missing" : "missing s.t !!"}, status=400)
        check = vote.objects.filter(user_id= user, pd_id=pd)
        if not check:
            serializer = vote_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response({"status": "you just vote for this product"})
        else:
            check.delete()
            return Response({"status": "you just unvote this product"})
    
detail_vote = detailVote.as_view()

        
