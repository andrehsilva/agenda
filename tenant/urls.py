from django.urls import path
from . import views

urlpatterns = [
    path('tenant/',views.tenant, name="list_tenant"),
]
