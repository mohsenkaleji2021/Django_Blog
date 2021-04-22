from django.contrib import admin
from django.urls import path
from django.urls import path , include
from django.conf import settings 
from django.conf.urls.static import static


app_name = 'root_main'
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blogg.urls')),
    path('accounts/', include('accounts.urls'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)