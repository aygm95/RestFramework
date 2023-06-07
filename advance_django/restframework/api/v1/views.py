from rest_framework.decorators import api_view , permission_classes
from rest_framework.response import Response    
from .serializer import PostSerializer
from rest_framework.permissions import IsAuthenticated,IsAuthenticatedOrReadOnly
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView

from advance_django.models import Comments


# @api_view(["GET","POST"])
# @permission_classes([IsAuthenticated])
# def postList(request):
#     if request.method =="GET":
#         comment=Comments.objects.all()
#         # comment=get_object_or_404(Comments,pk=id)
#         post_serializer=PostSerializer(comment,many=True)
#         return Response(post_serializer.data)
#     elif request.method== "POST":
#         serializer=PostSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(request.data)
         


"""  class based API view   """ 
class PostListApi(APIView):
    """ retreveing list of post"""

    permission_classes=[IsAuthenticatedOrReadOnly]
    serializer_class=PostSerializer

    def get(self,request):
        comment=Comments.objects.all()
        post_serializer=PostSerializer(comment,many=True)
        return Response(post_serializer.data)
                 
    """ creating post with provided data"""
    def post(self, request):
        serializer=PostSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(request.data)



@api_view(["GET","PUT","Delete"])
def postDetail(request,id):
    comment=get_object_or_404(Comments,pk=id)    
    if request.method =="GET":
        serializer=PostSerializer(comment)
        return Response(serializer.data)
    elif request.method == "PUT":
        serializer=PostSerializer(comment,data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    elif request.method == "DELETE":
        comment.delete()
        return Response({"data" :"data delete successfully"},status=204)