from django.contrib.auth import authenticate, login
from rest_framework.response import Response
from rest_framework import status, viewsets, generics, filters
from rest_framework.views import APIView
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework_simplejwt.tokens import RefreshToken
from .models import Recreacao, Card, Kid, User, KidCard
from .serializers import RecreacaoSerializer, CardSerializer, KidSerializer, ListaCardsDeUmRecreacaoSerializer, UserSerializer, KidCardSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

    def login(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            refresh = RefreshToken.for_user(user)
            return Response({
                'token': str(refresh.access_token),
                'access': str(refresh.access_token),
                'message': 'Login successful'
            }, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Credenciais inválidas'}, status=status.HTTP_401_UNAUTHORIZED)

class RecreacaoViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Recreacao.objects.all()
    serializer_class = RecreacaoSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ['nome']
    search_fields = ['nome']
    pagination_class = None
    permission_classes = [IsAuthenticated]

class CardViewSet(viewsets.ModelViewSet):
    queryset = Card.objects.all()
    serializer_class = CardSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ['nome']
    search_fields = ['nome']
    pagination_class = None
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save()
        print(f'Card cadastrado com sucesso pelo usuário {self.request.user.username}.')

    def perform_update(self, serializer):
        serializer.save()
        print(f'Card atualizado com sucesso pelo usuário {self.request.user.username}.')

    def perform_destroy(self, instance):
        instance.delete()
        print(f'Card excluído com sucesso pelo usuário {self.request.user.username}.')

class KidViewSet(viewsets.ModelViewSet):
    queryset = Kid.objects.all()
    serializer_class = KidSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ['nome']
    search_fields = ['nome']
    pagination_class = None

    def get_permissions(self):
        if self.action == 'create':
            self.permission_classes = [AllowAny]
        else:
            self.permission_classes = [IsAuthenticated]
        return super().get_permissions()

    def perform_create(self, serializer):
        serializer.save()
        print('Criança cadastrada com sucesso.')

    def perform_update(self, serializer):
        serializer.save()
        print(f'Criança atualizada com sucesso pelo usuário {self.request.user.username}.')

    def perform_destroy(self, instance):
        instance.delete()
        print(f'Criança excluída com sucesso pelo usuário {self.request.user.username}.')

class ListaCardsDeUmRecreacaoView(generics.ListAPIView):
    serializer_class = ListaCardsDeUmRecreacaoSerializer
    pagination_class = None
    permission_classes = [AllowAny]

    def get_queryset(self):
        pk = self.kwargs.get('pk')
        if pk is not None:
            queryset = Card.objects.filter(recreacao_id=pk)
            return queryset
        else:
            return Card.objects.none()

class ListaRecreacaoView(generics.ListAPIView):
    queryset = Recreacao.objects.all()
    serializer_class = RecreacaoSerializer
    permission_classes = [AllowAny]

class ListaCardView(generics.ListAPIView):
    queryset = Card.objects.all()
    serializer_class = CardSerializer
    permission_classes = [AllowAny]

class ListaKidView(generics.ListAPIView):
    queryset = Kid.objects.all()
    serializer_class = KidSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ['nome']
    filterset_fields = ['nome']
    permission_classes = [IsAuthenticated]

#---------------------------------------------------------------------------------------------------------
class KidCardViewSet(viewsets.ModelViewSet):
    queryset = KidCard.objects.all()
    serializer_class = KidCardSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save()
        print(f'Criança cadastrada na brincadeira com sucesso.')