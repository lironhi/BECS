from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('emergency/', views.emergency, name='emergency'),
    path('trauma/', views.trauma, name='trauma'),
    path('donators/', views.donators, name='donators'),
    path('add_donator', views.add_donator),
    path('takeallom', views.takeallom),
    path('copyall', views.copyall),
    path('auditrail/', views.auditrail, name='auditrail'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)