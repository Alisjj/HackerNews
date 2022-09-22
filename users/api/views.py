from .serializers import PasswordResetSerializer, PasswordChangeSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from rest_framework import permissions
from django.conf import settings


from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils.encoding import smart_bytes, smart_str, force_str, DjangoUnicodeDecodeError
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.contrib.sites.shortcuts import get_current_site
from django.urls import reverse
from django.core.mail import send_mail

from users.models import User


class CustomPasswordResetView(generics.GenericAPIView):
    permission_classes = (permissions.AllowAny, )
    serializer_class = PasswordResetSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)

        email = request.data['email']
        if User.objects.filter(email=email).exists():
            user=User.objects.get(email=email)
            uidb64 = urlsafe_base64_encode(smart_bytes(user.id))
            token=PasswordResetTokenGenerator().make_token(user)
            current_site = get_current_site(request=request).domain
            relativeLink = reverse('password_reset_confirm', kwargs={'uidb64':uidb64, 'token':token})
            absurl = 'http://'+ 'localhost:3000' + relativeLink
            email_body = "heyy " + absurl
            data = {
                'email_body': email_body,
                'to_email': user.email,
                'email_subject': 'Reset your password'
            } 
            send_mail(
                subject="You are invited to be an agent",
                message=email_body,
                from_email=getattr(settings, 'DEFAULT_FROM_EMAIL'),
                recipient_list=[user.email],
            )

        return Response({'detail':'Reset Password Email has been sent'}, status=status.HTTP_200_OK)


class PasswordResetConfirmView(generics.GenericAPIView):
    permission_classes = (permissions.AllowAny, )
    def get(self, request, uidb64, token):
        try:
            id = smart_str(urlsafe_base64_decode(uidb64))
            user = User.objects.get(id=id)

            if not PasswordResetTokenGenerator().check_token(user, token):
                return Response({'error': 'token is invalid or expired'}, status=status.HTTP_401_UNAUTHORIZED)

            return Response({'success': True, 'message': 'Valid Creadentials', 'uidb64': uidb64,'token': token}, status=status.HTTP_200_OK)

        except DjangoUnicodeDecodeError as identifier:
            return Response({'error': 'token is invalid or expired'}, status=status.HTTP_401_UNAUTHORIZED)


class PasswordResetChangeView(generics.GenericAPIView):
    serializer_class = PasswordChangeSerializer
    permission_classes = (permissions.AllowAny,)

    def patch(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response({'message': 'New password has been set'}, status=status.HTTP_200_OK)