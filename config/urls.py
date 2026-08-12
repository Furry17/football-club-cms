
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('pages.urls')),
    path('matches/', include('matches.urls')),
    path('training/', include('training.urls')),
    path('accounts/', include('accounts.urls'))
]
