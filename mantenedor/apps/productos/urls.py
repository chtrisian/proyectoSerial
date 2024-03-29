from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.urlpatterns import format_suffix_patterns
from .views import ProductViewSet, API_objects_details


urlpatterns = [
    path('api/', ProductViewSet.as_view()),
    path('api/<int:pk>/', API_objects_details.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)

urlpatterns += [   
    path('', views.main_page),
    path('tienda', views.shop),
    path('producto_add/', (views.producto_view)),
    path('producto_delete/<int:cod>/', (views.producto_delete)),
    path('producto_editar/<int:cod>/', (views.producto_edit)),
    path('producto_list/', (views.producto_list)),
    path('tienda/mas_vendidos', (views.shop_mas_vendidos)),
    path('tienda/oferta_mes', (views.shop_oferta_mes)),
]
if settings.DEBUG:
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
