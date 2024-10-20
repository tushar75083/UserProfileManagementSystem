from django.urls import path
from myapp import views


urlpatterns = [
    path('profiles/',views.user_profile_list, name='profileslists'),
    path('profiles/<int:pk>',views.user_profile_detail, name='profiledetails'),
]
