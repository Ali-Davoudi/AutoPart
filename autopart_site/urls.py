from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    path('', include('home_module.urls')),
    path('', include('auth_module.urls')),
    path('', include('product_module.urls')),
    path('', include('about_module.urls')),
    path('', include('contact_module.urls')),
    path('', include('service_module.urls')),
    path('', include('faq_module.urls')),
    path('', include('site_module.urls')),
    path('', include('blog_module.urls')),
    path('', include('userpanel_module.urls')),
    path('', include('basket_order_module.urls')),
    path('', include('wishlist_module.urls')),
    path('', include('pwa.urls'))
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
