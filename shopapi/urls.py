from django.urls import path, re_path
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    re_path(r'^products$', views.ProductPageView.as_view(), name='products'),
    path('buy_product/<int:pk>', views.ProductBuyPageView.as_view(), name='buy_product'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns += staticfiles_urlpatterns()
