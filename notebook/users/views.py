# # # views.py
# # from rest_framework import generics, status
# # from rest_framework.response import Response
# # from rest_framework.views import APIView
# # from rest_framework.permissions import AllowAny
# # from django.contrib.auth import get_user_model
# # from .serializers import CustomUserRegistrationSerializer
# # from rest_framework_simplejwt.views import TokenObtainPairView

# # class CustomUserRegistrationView(generics.CreateAPIView):
# #     queryset = get_user_model().objects.all()
# #     serializer_class = CustomUserRegistrationSerializer
# #     permission_classes = (AllowAny,)

# # class CustomTokenObtainPairView(TokenObtainPairView):
# #     pass
# from rest_framework import generics, permissions, status
# from rest_framework.response import Response
# from rest_framework.authtoken.views import ObtainAuthToken
# from rest_framework.authtoken.models import Token
# from django.contrib.auth.tokens import default_token_generator
# from django.contrib.auth import get_user_model
# from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
# from django.utils.encoding import force_bytes, force_text
# from django.core.mail import send_mail
# from .serializers import *

# User = get_user_model()

# class CustomUserCreate(generics.CreateAPIView):
#     queryset = User.objects.all()
#     serializer_class = CustomUserSerializer
#     permission_classes = [permissions.AllowAny]

#     def perform_create(self, serializer):
#         user = serializer.save()
#         token, created = Token.objects.get_or_create(user=user)
#         return user

# class CustomAuthToken(ObtainAuthToken):
#     def post(self, request, *args, **kwargs):
#         serializer = self.serializer_class(data=request.data, context={'request': request})
#         serializer.is_valid(raise_exception=True)
#         user = serializer.validated_data['user']
#         token, created = Token.objects.get_or_create(user=user)
#         return Response({
#             'token': token.key,
#             'user_id': user.pk,
#             'email': user.email
#         })

# class PasswordResetRequest(generics.CreateAPIView):
#     serializer_class = PasswordResetSerializer
#     permission_classes = [permissions.AllowAny]

#     def perform_create(self, serializer):
#         email = serializer.validated_data['email']
#         try:
#             user = User.objects.get(email=email)
#         except User.DoesNotExist:
#             return
#         uid = urlsafe_base64_encode(force_bytes(user.pk))
#         token = default_token_generator.make_token(user)
#         token = token.decode("utf-8")
#         reset_link = f"https://example.com/password-reset-confirm/{uid}/{token}/"

#         send_mail(
#             subject=_("Password Reset Request"),
#             message=reset_link,
#             from_email="noreply@example.com",
#             recipient_list=[email],
#         )
