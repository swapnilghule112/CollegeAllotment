from django.urls import path
from . import views
from college_allotment import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.create_profile, name = 'create'),
    path('download-report',views.download_report, name = 'download_report'),
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)