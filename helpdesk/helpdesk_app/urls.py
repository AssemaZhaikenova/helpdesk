from django.urls import path
from . import views
from helpdesk_app import views_auth


urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create_problem, name='create-problem'),
    path('list/', views.problem_list, name='problem-list'),
    path('problem/<int:problem_id>/', views.problem_detail, name='problem-detail'),
    path('login/', views_auth.login_view, name='login'),
    path('logout/', views_auth.logout_view, name='logout'),
]

