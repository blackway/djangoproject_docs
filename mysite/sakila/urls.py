from django.contrib.sitemaps import GenericSitemap
from django.contrib.sitemaps.views import sitemap
from django.urls import path

from . import views
from .models import Customer

app_name = 'sakila'

sitemaps = {
    'sakila': GenericSitemap({
        'queryset': Customer.objects.all(),
        'date_field': 'last_update',
    }, priority=0.9),
}

urlpatterns = [
    # path('polls/', include('polls.urls')),
    # path('admin/', admin.site.urls),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
]
