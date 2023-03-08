from django.urls import path, include
from rest_framework import routers
from api.views import CommentViewSet, GroupViewSet, FollowViewSet, PostViewSet

router = routers.DefaultRouter()
router.register('posts', PostViewSet)
router.register('groups', GroupViewSet)
router.register('follow', FollowViewSet)
router.register(
    r'^posts/(?P<post_id>\d+)/comments',
    CommentViewSet,
    basename='comment'
)
urlpatterns = [
    path('', include(router.urls)),
    path('', include('djoser.urls.jwt')),
]
