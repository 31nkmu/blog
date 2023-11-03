from django.urls import path

from apps.comment import views

urlpatterns = (
    path('', views.CommentCreateView.as_view()),
    path('<int:pk>/', views.CommentDetailView.as_view()),
)
