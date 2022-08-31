from django.contrib import admin
from django.urls import path, include
from movie import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('movie.urls')),
    path('news/', include('news.urls')),
    path('about/', views.about, name="about"),
    path('signup/', views.signup, name="signup"),

]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
