
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/models/", include("apps.employer.urls")),
    path("api/models/", include("apps.employee.urls")),
    path("api/models/", include("apps.vacancy.urls")),
    path("api/", include("rest_framework.urls")),
    path("api/auth/", include('djoser.urls')),
    path("api/auth/", include("djoser.urls.authtoken")),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
