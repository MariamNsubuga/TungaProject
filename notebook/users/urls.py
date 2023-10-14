from django.urls import path, re_path
from dj_rest_auth.registration.views import RegisterView, VerifyEmailView
from dj_rest_auth.views import LoginView, LogoutView
from rest_framework_simplejwt import views as jwt_views
# from .views import CustomUserRegistrationView
# from .views import CustomUserRegistrationView, CustomTokenObtainPairView

urlpatterns = [
#     path('account-confirm-email/<str:key>/', ConfirmEmailView.as_view()),
#     path('register/', CustomUserRegistrationView.as_view(), name='user-registration'),
#     path('token/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('register/', RegisterView.as_view()),
    path('login/', LoginView.as_view()),
    path('logout/', LogoutView.as_view()),

    path('verify-email/',
         VerifyEmailView.as_view(), name='rest_verify_email'),
    path('account-confirm-email/',
         VerifyEmailView.as_view(), name='account_email_verification_sent'),
    re_path(r'^account-confirm-email/(?P<key>[-:\w]+)/$',
         VerifyEmailView.as_view(), name='account_confirm_email'),
]