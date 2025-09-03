from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class RegisterSerializer(serializers.ModelSerializer):
    name = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['name', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def validate_email(self, value):
        email = value.strip().lower()
        if User.objects.filter(email__iexact=email).exists():
            raise serializers.ValidationError("Email already registered.")
        return email

    def create(self, validated_data):
        name = validated_data.pop('name').strip()
        email = validated_data.pop('email').strip().lower()
        password = validated_data.pop('password')

        # use email as username (so login works with email)
        user = User.objects.create_user(username=email, email=email, password=password)

        # split name into first and last
        parts = name.split(' ', 1)
        user.first_name = parts[0]
        if len(parts) > 1:
            user.last_name = parts[1]
        user.save()

        return user


class EmailTokenObtainPairSerializer(TokenObtainPairSerializer):
    """Login with email instead of username."""

    def validate(self, attrs):
        email = self.initial_data.get('email')
        if email:
            attrs['username'] = email
        return super().validate(attrs)

    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['email'] = user.email
        token['name'] = user.get_full_name() or user.username
        return token
