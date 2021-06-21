
from django.contrib import admin
from django.urls import path
from ems import views
from django.conf.urls import url
from django.views.static import serve
from django.conf import settings

urlpatterns = [
    
     path('emp', views.emp),
    path('', views.emp),
    path('show', views.show),
    path('edit/<int:id>', views.edit),
    path('update/<int:id>', views.update),
    path('delete/<int:id>', views.delete),
    path('admin/', admin.site.urls),
    

    url(r'^media/(?P<path>.*)$', serve,{'document_root':       settings.MEDIA_ROOT}), 
    url(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}), 
]
