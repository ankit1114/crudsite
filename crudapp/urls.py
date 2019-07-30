from django.urls import re_path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'crudapp'

urlpatterns = [
    re_path(r"id/$", auth_views.id.as_view(template_name="accounts/index.html"),name='id'),
    re_path(r"nmae/$", auth_views.Name.as_view(), name="name"),
    re_path(r"email/$", views.email.as_view(), name="email"),
    re_path(r"contact/$", views.Contact.as_view(), name="contact"),
]
