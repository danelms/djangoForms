from django.contrib import admin
from django.urls import path
from Pizza import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home),
    path('home', views.home, name='home'),
    path('order', views.order, name='order'),
]
urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
