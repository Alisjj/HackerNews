from rest_framework import serializers
from dj_rest_auth.registration.serializers import RegisterSerializer
from django.db import transaction
from rest_framework.exceptions import AuthenticationFailed
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils.encoding import smart_bytes, smart_str, force_str, DjangoUnicodeDecodeError
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.contrib.auth import get_user_model

from django.conf import settings

User = get_user_model()

class CustomRegistration(RegisterSerializer):
    full_name = serializers.CharField(max_length=120)

    @transaction.atomic
    def save(self, request):
        user = super().save(request)
        user.full_name = self.data.get('full_name')
        user.save()
        return user

class CustomUserDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'pk',
            'username',
            'email',
            'full_name',
        )
        read_only_fields = ('pk', 'email', 'profile_link', 'referral_url')
    

class PasswordResetSerializer(serializers.Serializer):
    email = serializers.EmailField(min_length=3)

    class Meta:
        fields = ('email')

class PasswordChangeSerializer(serializers.Serializer):
    password = serializers.CharField(min_length=4, write_only=True)
    token = serializers.CharField(min_length=4, write_only=True)
    uidb64 = serializers.CharField(min_length=2 , write_only=True)

    class Meta:
        fields=(
            'password',
            'token',
            'uidb64'
        )

    def validate(self, attrs):
        try:
            password = attrs.get('password')
            token = attrs.get('token')
            uidb64 = attrs.get('uidb64')

            id = force_str(urlsafe_base64_decode(uidb64))
            user = User.objects.get(id=id)

            if not PasswordResetTokenGenerator().check_token(user, token):
                # return Response({'error': 'token is invalid or expired'}, status=status.HTTP_401_UNAUTHORIZED)
                raise AuthenticationFailed('Password Reset link is invalid', 401)

            user.set_password(password)
            user.save()

            return (user)

        except Exception as e:
            raise AuthenticationFailed('Password Reset link is invalid', 401)

        # return super().validate(attrs)

