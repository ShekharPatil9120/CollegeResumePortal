from django.urls import path
from . import views  # Import views from the current app
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.login_page, name='login_page'),  # Login page
    path('select_college/', views.select_college, name='select_college'),  # College selection page
    path('resume/<int:student_id>/', views.resume_page, name='resume_page'),  # Resume page
]

# Serve media files during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

