from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()

# /user
router.register('user', views.UserViewSet, basename='user')

urlpatterns = router.urls