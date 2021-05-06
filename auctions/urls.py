from django.urls import path
from . import views

from django.conf import settings
from django.conf.urls.static import static

app_name="auctions"

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("add", views.add, name="add"),
    path("<int:auction_id>/auction", views.auction, name="auction")
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)