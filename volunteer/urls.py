
from django.urls import path, re_path
from .views import register, detail, volunteers

urlpatterns = [
    path('Registeration/', register, name="volunter-rgister"),
    path('Detail/<int:pk>', detail, name="volunter-detail"),
    path('all/', volunteers, name="volunters"),
]