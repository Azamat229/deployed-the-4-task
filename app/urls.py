from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('', views.CourseListView.as_view(), name='list'),
    path('<int:pk>/', views.CourseDetailView.as_view(), name='detail'),
    # path('courses/', views.CourseCreateView.as_view())

]

urlpatterns = format_suffix_patterns(urlpatterns)
