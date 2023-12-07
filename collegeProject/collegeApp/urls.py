from . import views
from django.urls import path
# from .views import my_form_view
# app_name='collegeApp'
urlpatterns=[

    # path('', views.savevalues, name='savevalues'),
    path('',views.index,name='index'),
    # path('myform/', my_form_view, name='my_form'),
    # path('dashboard', views.dashboard, name='dashboard'),
    # path('form_page', views.form_page, name='form_page'),
    path('add/', views.person_create_view, name='person_add'),
      # path('<int:pk>/', views.person_update_view, name='person_change'),

    path('ajax/load-courses/', views.load_courses, name='ajax_load_courses'),  # AJAX
]
