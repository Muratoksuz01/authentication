from .views import *
from django.urls import path
urlpatterns = [
    path("",home,name="home"),
    path("signin/",signin,name="signin"),
    path("signup/",signup,name="signup"),
    path("signout/",signout,name="signout")



]
