from django.urls import re_path
from rest_framework.urlpatterns import format_suffix_patterns

from . import views


urlpatterns = [
    # models misiones urls
    re_path(r'^misiones$', views.MisionList.as_view()),
    re_path(r'^misiones/(?P<pk>\d+)$', views.MisionDetail.as_view()),
    re_path(r'^misiones/min$', views.MisionMinList.as_view()),

    # models mediciones urls
    re_path(r'^mediciones$', views.MedicionList.as_view()),
    re_path(r'^mediciones/(?P<pk>\d+)$', views.MedicionDetail.as_view()),
    re_path(r'^mediciones/min$', views.MedicionMinList.as_view()),

    re_path(r'^ultima-mision$', views.LastMisionMinList.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
