from rest_framework.decorators import api_view
from rest_framework.response import Response    
from .serializer import postSerializer
from ...models import Comments

@api_view()
def postList(request):
    return Response('ok')

@api_view()
def postDetail(request,id):
    comment=Comments.objects.ger(pk=id)
    return Response(comment)

