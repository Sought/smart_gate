from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from smart_gate.quickstart import views

router = routers.DefaultRouter()
router.register(r'entry', views.EntryViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('index/', views.index, name='index'),
    path('', views.index, name='index'),
    path('data/', include(router.urls)),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')) 
]
