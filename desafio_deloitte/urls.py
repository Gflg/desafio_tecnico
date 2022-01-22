from django.contrib import admin
from django.urls import path, include
from servicos.views import ServicoViewSet
from posts.views import PostViewSet
from integrantes.views import IntegranteViewSet
from rest_framework import routers

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="API Agência Cronos",
        default_version='v1',
        description="Uma API desenvolvida para o case técnico da Agência Cronos",
        contact=openapi.Contact(email="gflgon@gmail.com"),
        license=openapi.License(name="Licença para Desenvolvimento"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

router = routers.DefaultRouter()
router.register(r'servicos', ServicoViewSet)
router.register(r'posts', PostViewSet)
router.register(r'integrantes', IntegranteViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path("redoc", schema_view.with_ui('redoc',
                                      cache_timeout=0), name='schema-redoc'),
]
