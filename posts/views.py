from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import authentication
from rest_framework import permissions
from posts.models import Posts
from posts.serializers import PostSerializer


class PostViewSet(viewsets.ModelViewSet):
    queryset = Posts.objects.all()
    serializer_class = PostSerializer
    authentication_classes = [authentication.SessionAuthentication,
                              authentication.TokenAuthentication]
    permission_classes = (permissions.IsAdminUser,)

    def get_permissions(self):
        if self.request.method in ['PUT', 'DELETE']:
            return [permissions.IsAdminUser()]
        return [permissions.IsAuthenticated()]