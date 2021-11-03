from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name = 'costs'
urlpatterns = [
    path(
        '',
        auth_views.LoginView.as_view(template_name='costs/login.html'),
        name='login',
    ),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('signup/', views.signup, name='signup'),
    path('warehousing/', views.warehousing, name='warehousing'),
    path('warehousing_views/', views.warehousing_views, name='warehousing_views'),
    path('earning/', views.earning, name='earning'),
    path('earning_views/', views.earning_views, name='earning_views'),
    path('cost_accounting/', views.cost_accounting, name='cost_accounting'),
    path('cost_views/', views.cost_views, name='cost_views'),
    path('profit/', views.profit, name='profit'),
]