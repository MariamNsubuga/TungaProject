# # # serializers.py
# # from rest_framework import serializers
# # from .models import CustomUser

# # class CustomUserRegistrationSerializer(serializers.ModelSerializer):
# #     class Meta:
# #         model = CustomUser
# #         fields = ('email', 'first_name', 'last_name', 'password')
# #         extra_kwargs = {'password': {'write_only': True}}

# #     def create(self, validated_data):
# #         user = CustomUser(
# #             email=validated_data['email'],
# #             first_name=validated_data['first_name'],
# #             last_name=validated_data['last_name'],
# #             username=validated_data['username']
# #         )
# #         user.set_password(validated_data['password'])
# #         user.save()
# #         return user
# from rest_framework import serializers
# from django.contrib.auth import get_user_model
# from django.contrib.auth import password_validation
# from django.utils.translation import gettext as _

# User = get_user_model()

# class CustomUserSerializer(serializers.ModelSerializer):
#     password = serializers.CharField(write_only=True, required=True, validators=[password_validation.validate_password])

#     class Meta:
#         model = User
#         fields = ('id', 'email', 'first_name', 'last_name', 'password','username')

# class LoginSerializer(serializers.Serializer):
#     email = serializers.EmailField()
#     password = serializers.CharField()

# class PasswordResetSerializer(serializers.Serializer):
#     email = serializers.EmailField()
