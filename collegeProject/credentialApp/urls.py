from . import views
from django.urls import path
app_name='credentialApp'
urlpatterns=[
    path('register',views.register,name='register'),
    path('login',views.login_view,name='login'),
    path('dashboard',views.dashboard,name='dashboard'),
    path('logout',views.Logout,name='logout'),
    # path('form_page',views.form_page,name='form_page'),

]
