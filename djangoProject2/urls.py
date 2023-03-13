
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('adman/', admin.site.urls),
    path('', include('tst.urls'))
]
