from django.urls import path
from . import views

urlpatterns = [
    path('questions/grade/<int:grade>/top/<int:n>/', views.TopQuestionsByGradeView.as_view(), name='top-questions-by-grade'),
    path('questions/topic/<str:topic>/count/<int:n>/', views.QuestionsByTopicView.as_view(), name='questions-by-topic'),
    path('questions/complexity/<str:complexity>/count/<int:n>/', views.QuestionsByComplexityView.as_view(), name='questions-by-complexity'),
    path('questions/grade/<int:grade>/topic/<str:topic>/count/<int:n>/', views.QuestionsByGradeAndTopicView.as_view(), name='questions-by-grade-topic'),
    path('topics/', views.TopicsView.as_view(), name='topics'),
    path('stats/', views.StatsView.as_view(), name='stats'),
    path('health/', views.health_check, name='health'),
]
