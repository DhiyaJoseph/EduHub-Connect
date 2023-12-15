from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('',views.index,name='index'),
    path('cart',views.cart,name='cart'),
    path('student_dashboard',views.student_dashboard,name='student_dashboard'),
    path('dashboard',views.dashboard,name='dashboard'),
    path('student_profile',views.student_profile,name='student_profile'),
    path('student_settings',views.student_settings,name='student_settings'),
    path('course',views.course,name='course'),
    path('lesson', views.lesson, name='lesson'),
    path('student_enrolled_courses',views.student_enrolled_courses,name='student_enrolled_courses'),
    path('login', views.login_view, name='login'),  
    path('sign_up',views.sign_up,name='sign_up'),
    path('checkout',views.checkout,name='checkout'),
    path('course_details/<slug:slug>/', views.course_details, name='course_details'),

]
