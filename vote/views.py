from django.shortcuts import render
from rest_framework.views import APIView
from .models import vote
from .serializers import vote_serializer
from rest_framework.response import Response


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
        v_type = str(request.data['t']) 
        if not pd or not user:
            return Response({"missing" : "missing s.t !!"}, status=400)
        check = vote.objects.filter(user_id= user, pd_id=pd)
        if v_type == '0' or v_type == 'False':
            if not check:
                return Response({"invlid": "you haven't voted for the product!"} , status=400)
            else:
                check.delete()
                return Response({"status" : f"deleted your vote for product id {pd}"} , status= 200)

        else:
            if not check:
                serializer = vote_serializer(data=request.data)
                serializer.is_valid()
                serializer.save()
                return Response(serializer.data)
            else:
                return Response({"invlid": "you have already voted for the product!"} , status=400)
    
detail_vote = detailVote.as_view()