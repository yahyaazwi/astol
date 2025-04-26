from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('fleet_app.urls')),
    path('api/', include('fleet_app.api.urls')),  # للواجهات البرمجية
]
from fleet_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('test/', views.test_page, name='test'),
]