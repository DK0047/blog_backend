from django.urls import include, path
from rest_framework import routers
from .import views
from django.conf.urls.static import static
from django.conf import settings


router = routers.DefaultRouter() #api setting
router.register(r'blog',views.Blog_detailsview)
router.register(r'blog/<int:blog_id>',views.Blog_detailsview)

 
urlpatterns = [
    path(r'', include(router.urls)),
    path(r'api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path("signup/", views.signup, name="signup"),
    path("login/", views.login, name="login"),
    
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)