from django.urls import path

from.import views
urlpatterns = [
    path("", views.homepage.as_view(), name="homepage"),
    path("contact/", views.contactpage.as_view(), name="contact")
]
