from django.urls import path
from core.views import index, contact, signup
from django.contrib.auth import views
from core.forms import LoginForm

app_name = "core"

urlpatterns = [
    path('', index, name="index"),
    path('contact/', contact, name="contact"),
    path('signup/', signup, name="signup"),
    path('login/', views.LoginView.as_view(authentication_form=LoginForm,
         template_name="login.html"), name="login"),
]
