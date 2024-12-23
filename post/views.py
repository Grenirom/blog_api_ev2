from rest_framework.viewsets import ModelViewSet
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.decorators import action

from comments.serializers import CommentSerializer

from .serializers import PostSerializer
from .models import Post
from .permissions import IsOwner

class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def get_permissions(self):
        if self.request.method in ['GET', 'POST']:
            return [permissions.IsAuthenticated()]
        if self.request.method in ['PUT', 'PATCH', 'DELETE']:
            return [permissions.IsAdminUser(), IsOwner()]
    
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    @action(detail=True, methods=['POST'])
    def comment(self, request, pk=None):
        post = self.get_object()
        serializer = CommentSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(post=post, owner=request.user)
        return Response('Успешно добавлено', status=201)
    