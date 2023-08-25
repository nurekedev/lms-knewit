from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'course'

urlpatterns = [
    path('', views.index),
    path('<int:day>/<int:month>/<int:year>/<slug:course_data>/', views.course_detail, name='detailed_info'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
