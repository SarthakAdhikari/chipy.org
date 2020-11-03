from django.conf.urls import url

from .views import Home

urlpatterns = [
    url(r"^en-US$", Home.as_view(), name="home"),
]
