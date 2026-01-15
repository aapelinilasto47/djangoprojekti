from rest_framework import serializers
from .models import Varastot, Tuote
from django.contrib.auth.models import User


class TuoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tuote
        fields = '__all__'

class VarastotSerializer(serializers.ModelSerializer):

    tuote_tiedot = TuoteSerializer(source='ean_koodi', read_only=True)

    class Meta:
        model = Varastot
        fields = ['varasto_id', 'ean_koodi', 'kayttaja', 'sijainti', 'määrä', 'ostopäivä', 'viimeinen_käyttöpäivä', 'tuote_tiedot']


class UserSerializer(serializers.Serializer):
    password = serializers.CharField(write_only=True)
    username = serializers.CharField(required=True)
    email = serializers.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'password', 'email']

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        return user