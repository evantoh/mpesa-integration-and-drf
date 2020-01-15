from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('api/shop/', views.MwendaList.as_view()),
    path('api/item/item-id/<int:pk>/',views.MwendaDescription.as_view())

]
