from rest_framework import serializers
from recreacao.models import Recreacao, Card, Kid, KidCard
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password

class UserSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'confirm_password']
        extra_kwargs = {'password': {'write_only': True}}

    def validate(self, data):
        password = data.get('password')

        # Remove a validação de senha
        # try:
        #     validate_password(password)
        # except ValidationError as e:
        #     raise serializers.ValidationError({"password": e.messages})

        if data.get('password') != data.get('confirm_password'):
            raise serializers.ValidationError("As senhas não coincidem")

        username = data.get('username')
        if not username:
            raise serializers.ValidationError("O username é obrigatório")
        if '@' not in username:
            raise serializers.ValidationError("O username deve conter @")

        email = data.get('email')
        if email and not email.strip():
            raise serializers.ValidationError("O email não pode ser vazio")

        return data

    def create(self, validated_data):
        validated_data.pop('confirm_password', None)
        user = User(
            username=validated_data['username'],
            email=validated_data['email'].strip() if validated_data.get('email') else None,
            password=make_password(validated_data['password'])
        )
        user.save()
        return user

class RecreacaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recreacao
        fields = '__all__'

class CardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Card
        fields = '__all__'

class ListaCardsDeUmRecreacaoSerializer(serializers.ModelSerializer):
    recreacao_nome = serializers.ReadOnlyField(source='recreacao.nome')

    class Meta:
        model = Card
        fields = '__all__'

class KidSerializer(serializers.ModelSerializer):
    class Meta:
        model = Kid
        fields = '__all__'

    def create(self, validated_data):
        existing_kid = Kid.objects.filter(
            nome=validated_data['nome'],
            numeroApartamento=validated_data['numeroApartamento']
        ).first()

        if existing_kid:
            raise serializers.ValidationError(
                "Criança já cadastrada com este nome e número de apartamento."
            )

        return Kid.objects.create(**validated_data)
    
#---------------------------------------------------------------------------------------------------------
class KidCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = KidCard
        fields = '__all__'