from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include

urlpatterns = [
                  path('admin/', include('adminSystem.urls')),
                  path('file/', include('fileManager.urls'))
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL,
                                                                                         document_root=settings.STATIC_ROOT)
