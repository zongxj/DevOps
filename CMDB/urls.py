"""DevOps URL Configuration
"""
from django.urls import path
from . import views

app_name = 'cmdb'
urlpatterns = [
    # ex： /CMDB/
    path('', views.IndexView.as_view(), name='index'),
    path('index', views.IndexView.as_view(), name='index'),
    # ex： /CMDB/5/
    # path('<int:question_id>/', views.detail, name='detail'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    # ex： /CMDB/5/results/
    # path('<int:question_id>/results/', views.results, name='results'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    # ex： /CMDB/5/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),
    # login
    path('login/', views.login, name='login'),
    # authin
    path('login/authin/', views.authin, name='authin'),

]
