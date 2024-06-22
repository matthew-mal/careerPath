from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/1/users/', include('user.urls'), namespace='users'),
    path('api/1/jobs/', include('jobs.urls'), namespace='jobs'),
]
