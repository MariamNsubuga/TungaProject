from django.contrib import admin
from django.urls import path,include
from .views import *
from rest_framework.authtoken.views import obtain_auth_token
# #swagger documentation urls
# from django.contrib import admin
# from django.urls import path, re_path, include
# from drf_yasg.views import get_schema_view
# from drf_yasg import openapi
# from rest_framework import permissions

# schema_view = get_schema_view(
#     openapi.Info(
#         title="Your API",
#         default_version='v1',
#         description="API Description",
#         terms_of_service="https://www.example.com/terms/",
#         contact=openapi.Contact(email="contact@example.com"),
#         license=openapi.License(name="Your License"),
#     ),
#     public=True,
#     permission_classes=(permissions.AllowAny,),
# )
urlpatterns = [
   

    path('', NoteList.as_view()),
    path('/<int:pk>', NoteDetail.as_view()),
    path('/pdf', GeneratePDFView.as_view()),
    path('/csv', GenerateCSVView.as_view()),
    path('/excel/', GenerateExcelView.as_view()),
    path('/email', send_notes_via_email, name='send-notes-via-email'),
    # re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    # path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    # path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    
    
]





