from django.urls import path
from . import views
from . import url_handlers

urlpatterns = [
    path("pojisteni/", views.PojisteniIndex.as_view(), name="pojisteni_index"),
    path("pojistenci/", views.PojistenyIndex.as_view(), name="pojistenci_index"),
    path("<int:pk>/pojisteny_detail/", views.PojistenyCurrent.as_view(), name="pojisteny_detail"),
    path("pojistenci_create/", views.PojistenyCreate.as_view(), name="novy_pojisteny"),
    path("pojisteni_create/", views.PojisteniCreate.as_view(), name="nove_pojisteni"),
    path("udalosti_create/", views.UdalostForm.as_view(), name="udalosti_form"),
    path("pp_create/", views.PojisteniPojistenyCreate.as_view(), name="nove_pp"),
    path("", url_handlers.index_handler),
    path("register/", views.UzivatelViewRegister.as_view(), name="registrace"),
    path("login/", views.UzivatelViewLogin.as_view(), name="login"),
    path("logout/", views.logout_user, name="logout"),
    path("about/", views.AboutView.as_view(), name="about"),
    path("udalosti/", views.UdalostIndex.as_view(), name="udalosti"),
    path("<int:pk>/edit/", views.PojistenyEdit.as_view(), name="edit_pojisteny"),
    path("<int:pk>/edit_pojisteni/", views.PojisteniEdit.as_view(), name="edit_pojisteni"),
    path("<int:pk>/edit_pp/", views.PojisteniPojistenyEdit.as_view(), name="edit_pp"),
    path("<int:pk>/edit_udalost/", views.UdalostiEdit.as_view(), name="edit_udalost"),

]