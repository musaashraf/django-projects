from django.conf import settings
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path

from .views import *

app_name = 'loginapp'
urlpatterns = [
    path('', index, name='index'),
    path('register/', register, name='register'),
    path('login/', login_page, name='login'),
    path('user_login/', user_login, name='user_login'),
    path('logout/', user_logout, name='logout'),
]
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
