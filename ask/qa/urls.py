from django.urls import path, re_path
from . import views
from django.conf.urls import include, url

urlpatterns = [
    # re_path(r'', views.test),
    path('', views.index),
    path('login', views.test),
    path('signup', views.test),
    path('question/<int:q_id>/', views.question_view),
    path('ask', views.test),
    path('popular', views.popular),
    path('new', views.test),
]
