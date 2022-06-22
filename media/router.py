from media_app.viewsets import ImgViewset
from rest_framework import routers

router = routers.DefaultRouter()
router.register('media',ImgViewset)