from django.urls import path
from .views import postDetail,PostListApi

app_name="api-v1"

urlpatterns = [
    path('post/',PostListApi.as_view(),name='postList'),
    # path('post/',postList,name='postList'),
    path('post/<id>/',postDetail,name='postDetail'),
]