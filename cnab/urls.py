from django.urls import path
from . import views

urlpatterns = [
    path("", views.render_form_view, name="upload"),
    path("transactions/", views.render_transactions_view, name="transaction"),
]
