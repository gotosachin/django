"""Contain all the url for player"""
# import url
from django.conf.urls import url
# django
from django.contrib.auth.views import LoginView, LogoutView

from .views import home, new_invitation, accept_invitation, profile

urlpatterns = [
    url(r'home$', home, name="player_home"),
    url(r'login$', LoginView.as_view(template_name="player/login_form.html"), name="player_login"),
    url(r'logout$', LogoutView.as_view(), name="player_logout"),
    url(r'new_invitation$', new_invitation, name="player_new_invitation"),
    # url(r'profile/(?P<id>\d+)/$', profile, name="player_profile"),
    url(r'accept_invitation/(?P<id>\d+)/$', accept_invitation, name="player_accept_invitation"),
]