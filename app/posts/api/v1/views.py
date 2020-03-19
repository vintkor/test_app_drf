from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import ListAPIView
from .serializers import PostSerializer, LikeSerializer
from posts.models import Post, Like
from rest_framework.decorators import action
from posts.servises import LikeService
from posts.filters import PostAnalyticFilter
from django_filters import rest_framework as filters


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


class AnalyticsAPIView(ListAPIView):
    queryset = Like.objects.all()
    filter_backends = (filters.DjangoFilterBackend,)
    filter_class = PostAnalyticFilter

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        data = [
            {
                'total': queryset.count(),
            }
        ]

        return Response(data)
