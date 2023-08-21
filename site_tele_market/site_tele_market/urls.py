from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("main.urls")),
    path('buy/', include("main.urls")),
    path('sell/', include("main.urls")),
    path('buy/filter', include("main.urls")),
]
