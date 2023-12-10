from django.contrib import admin
from django.contrib.auth.models import Group, User
from django.urls import path
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    path("api/schema/docs/", SpectacularSwaggerView.as_view(url_name="schema")),
]

admin.site.site_header = "Django Admin"
admin.site.site_title = "Django Admin"
admin.site.index_title = "Welcome to Django Admin"
admin.site.unregister(Group)
admin.site.unregister(User)
