from django.conf.urls import url
from . import views
urlpatterns = [
  url(r'^$', views.RegistrationList.as_view(), name='registration_list'),
  url(r'^new$', views.RegistrationCreate.as_view(), name='registration_new'),
  url(r'^edit/(?P<pk>\d+)$', views.RegistrationUpdate.as_view(), name='registration_edit'),
  url(r'^delete/(?P<pk>\d+)$', views.RegistrationDelete.as_view(), name='registration_delete'),
]