from django.urls import path
from .views import postList,postDetail

app_name="api-v1"

urlpatterns = [
    path('post/',postList,name='postList'),
    path('post/<id>/',postDetail,name='postDetail'),
]