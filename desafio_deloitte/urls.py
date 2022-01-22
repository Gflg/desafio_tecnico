from django.contrib import admin
from django.urls import path, include
from servicos.views import ServicoViewSet
from posts.views import PostViewSet
from integrantes.views import IntegranteViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'servicos', ServicoViewSet)
router.register(r'posts', PostViewSet)
router.register(r'integrantes', IntegranteViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
]
