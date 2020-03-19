from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from .serializers import PostSerializer, LikeSerializer
from posts.models import Post
from rest_framework.decorators import action
from posts.servises import LikeService


class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    @action(detail=True, methods=['POST'])
    def like(self, request, pk):
        like, is_created = LikeService.like(pk, request.user)
        serializer = LikeSerializer(like)
        data = {'is_new': is_created}
        data.update(serializer.data)
        return Response(data)

    @action(detail=True, methods=['POST'])
    def unlike(self, request, pk):
        LikeService.unlike(pk, request.user)
        return Response()

    @action(detail=True, methods=['GET'])
    def analytics(self, request, pk):
        queryset = LikeService.analytics(pk)
        serializer = LikeSerializer(queryset, many=True)
        return Response(serializer.data)
