from django.contrib import admin
from django.urls import path, include
from recreacao.views import RecreacaoViewSet, CardViewSet, UserViewSet, KidViewSet, ListaCardView, ListaKidView, ListaCardsDeUmRecreacaoView
from rest_framework import routers
from django.conf import settings
from django.conf.urls.static import static
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions

schema_view = get_schema_view(
    openapi.Info(
        title="API da Recreação",
        default_version='v1',
        description="Recreação - Cataratas Park Hotel",
        terms_of_service="#",
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

admin_router = routers.DefaultRouter()
admin_router.register('recreacao', RecreacaoViewSet, basename="recreacao")
admin_router.register('card', CardViewSet, basename="card")
admin_router.register('user', UserViewSet, basename="user")
admin_router.register('kid', KidViewSet, basename="criancas")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),

    path('api/v1/card/', ListaCardView.as_view(), name='list_card'),
    path('api/v1/kid/', ListaKidView.as_view(), name='list_kid'),
    path('api/v1/cadastro-kids/', KidViewSet.as_view({'post': 'create'}), name='cadastro_kids'),

    path('api/v2/login/', UserViewSet.as_view({'post': 'login'}), name='login'),
    path('api/v2/user/', UserViewSet.as_view({'post': 'create'}), name='cadastro_colaborador'),
    path('api/v2/', include(admin_router.urls)),

    path('api/v1/recreacao/<int:pk>/card/', ListaCardsDeUmRecreacaoView.as_view(), name='list_recreacao_card'),
    path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
