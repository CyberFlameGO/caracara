from django.urls import path

from user_area.views.web import user

app_name = 'user_area_web'

urlpatterns = [
    path('dashboard/', user.DashboardView.as_view(), name='dashboard'),
]