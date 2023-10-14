# # views.py
# from rest_framework import generics, status
# from rest_framework.response import Response
# from rest_framework.views import APIView
# from rest_framework.permissions import AllowAny
# from django.contrib.auth import get_user_model
# from .serializers import CustomUserRegistrationSerializer
# from rest_framework_simplejwt.views import TokenObtainPairView

# class CustomUserRegistrationView(generics.CreateAPIView):
#     queryset = get_user_model().objects.all()
#     serializer_class = CustomUserRegistrationSerializer
#     permission_classes = (AllowAny,)

# class CustomTokenObtainPairView(TokenObtainPairView):
#     pass
