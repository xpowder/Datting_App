from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name="home"),
    path('profile/create/', views.Create_Profile, name='create-profile'),
    path('discover/', views.Profile_list, name='discover'),
    path('profile/<int:pk>/like/', views.Like_profile, name='like-profile'),
    path('profile/<int:pk>/dislike/', views.Dislike_profile, name='dislike-profile'),
    path('likes/', views.profile_like_list, name='likes-profiles')
    
]


if settings.DEBUG:  # Only serve media in debug mode
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)