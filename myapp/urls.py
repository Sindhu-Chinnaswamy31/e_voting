from django.urls import path
from myapp import views

app_name="myapp"

urlpatterns = [
    path('register/',views.register,name="registration"),
    path('login/',views.user_login,name="login"),
    path('cast_vote/',views.cast_vote,name="cast_vote"),
]