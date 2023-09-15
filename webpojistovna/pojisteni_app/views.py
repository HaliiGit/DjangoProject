from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from django.views.generic import TemplateView
from django.contrib.auth import login, logout, authenticate
from .models import Pojisteny, Pojisteni, Uzivatel, PojisteniPojisteny, Udalosti
from .forms import PojistenyForm, UzivatelForm, LoginForm, PojisteniForm, PojisteniPojistenyForm, UdalostiForm
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator, Page

# Create your views here.
class PojistenyEdit(LoginRequiredMixin, generic.edit.CreateView):
    form_class = PojistenyForm
    template_name = "pojisteni_app/pojisteny_create.html"

    def get(self, request, pk):
        if not request.user.is_admin:
            messages.info(request, "Nemáte práva pro úpravu pojištěného.")
            return redirect("pojistenci_index")
        try:
            pojisteny = Pojisteny.objects.get(pk=pk)
        except:
            messages.error(request, "Tento pojištěnec neexistuje!")
            return redirect("pojistenci_index")
        form = self.form_class(instance=pojisteny)
        return render(request, self.template_name, {"form": form})

    def post(self, request, pk):
        if not request.user.is_admin:
            messages.info(request, "Nemáte práva pro úpravu pojištěnce.")
            return redirect("pojistenci_index")
        form = self.form_class(request.POST)

        if form.is_valid():
            jmeno = form.cleaned_data["jmeno"]
            prijmeni = form.cleaned_data["prijmeni"]
            ulice = form.cleaned_data["ulice"]
            mesto = form.cleaned_data["mesto"]
            psc = form.cleaned_data["psc"]
            tel = form.cleaned_data["tel"]
            email = form.cleaned_data["email"]

            try:
                pojisteny = Pojisteny.objects.get(pk=pk)
            except:
                messages.error(request, "Tento pojištěnec neexistuje!")
                return redirect("pojistenci_index")
            pojisteny.jmeno = jmeno
            pojisteny.prijmeni = prijmeni
            pojisteny.tel = tel
            pojisteny.email = email
            pojisteny.psc = psc
            pojisteny.mesto = mesto
            pojisteny.ulice = ulice
            pojisteny.save()
            return redirect("pojisteny_detail", pk=pojisteny.id)
        return render(request, self.template_name, {"form": form})

class PojisteniEdit(LoginRequiredMixin, generic.edit.CreateView):
    form_class = PojisteniForm
    template_name = "pojisteni_app/pojisteni_create.html"

    def get(self, request, pk):
        if not request.user.is_admin:
            messages.info(request, "Nemáte práva pro úpravu pojištění.")
            return redirect("pojisteni_index")
        try:
            pojisteni = Pojisteni.objects.get(pk=pk)
        except:
            messages.error(request, "Toto pojištění neexistuje!")
            return redirect("pojisteni_index")
        form = self.form_class(instance=pojisteni)
        return render(request, self.template_name, {"form": form})

    def post(self, request, pk):
        if not request.user.is_admin:
            messages.info(request, "Nemáte práva pro úpravu pojištění.")
            return redirect("pojisteni_index")
        form = self.form_class(request.POST)

        if form.is_valid():
            typ_pojisteni = form.cleaned_data["typ_pojisteni"]

            try:
                pojisteni = Pojisteni.objects.get(pk=pk)
            except:
                messages.error(request, "Tento pojištěnec neexistuje!")
                return redirect("pojisteni_index")
            pojisteni.typ_pojisteni
            pojisteni.save()
            return redirect("pojisteny_detail", pk=pojisteni.id)
        return render(request, self.template_name, {"form": form})

class UdalostiEdit(LoginRequiredMixin, generic.edit.CreateView):
    form_class = UdalostiForm
    template_name = "pojisteni_app/udalosti_create.html"

    def get(self, request, pk):
        if not request.user.is_admin:
            messages.info(request, "Nemáte práva pro úpravu události.")
            return redirect("udalosti")
        try:
            udalosti = Udalosti.objects.get(pk=pk)
        except:
            messages.error(request, "Tato událost neexistuje!")
            return redirect("udalosti_form")
        form = self.form_class(instance=udalosti)
        return render(request, self.template_name, {"form": form})

    def post(self, request, pk):
        if not request.user.is_admin:
            messages.info(request, "Nemáte práva pro úpravu události.")
            return redirect("udalosti_form")
        form = self.form_class(request.POST)

        if form.is_valid():
            cislo_pojistne_smlouvy = form.cleaned_data["cislo_pojistne_smlouvy"]
            pojisteni = form.cleaned_data["pojisteni"]
            popis_udalosti = form.cleaned_data["popis_udalosti"]
            datum_udalosti = form.cleaned_data["datum_udalosti"]

            try:
                udalost = Udalosti.objects.get(pk=pk)
            except:
                messages.error(request, "Tato událost neexistuje!")
                return redirect("udalosti_form")
            udalost.cislo_pojistne_smlouvy
            udalost.pojisteni
            udalost.popis_udalosti
            udalost.datum_udalosti
            pojisteni.save()
            return redirect("udalosti_form")
        return render(request, self.template_name, {"form": form})


class PojisteniPojistenyEdit(LoginRequiredMixin, generic.edit.CreateView):
    form_class = PojisteniPojistenyForm
    template_name = "pojisteni_app/pp_create.html"
    def get(self, request, pk):
        if not request.user.is_admin:
            messages.info(request, "Nemáte práva pro úpravu pojištěného.")
            return redirect("pojisteni_index")
        try:
            pojisteni_pojisteny = PojisteniPojisteny.objects.get(pk=pk)
        except:
            messages.error(request, "Toto pojištění neexistuje!")
            return redirect("pojisteni_index")
        form = self.form_class(instance=pojisteni_pojisteny)
        return render(request, self.template_name, {"form": form})

    def post(self, request, pk):
        if not request.user.is_admin:
            messages.info(request, "Nemáte práva pro úpravu pojištěnce.")
            return redirect("pojisteni_index")
        form = self.form_class(request.POST)

        if form.is_valid():
            try:
                pojisteni_pojisteny = PojisteniPojisteny.objects.get(pk=pk)
            except PojisteniPojisteny.DoesNotExist:
                messages.error(request, "Toto pojištění neexistuje!")
                pojisteni_pojisteny = form.instance
                return redirect("pojisteny_detail", pk=pojisteni_pojisteny.pojisteny.pk)
            pojisteni_pojisteny.pojisteni = form.cleaned_data["pojisteni"]
            pojisteni_pojisteny.pojisteny = form.cleaned_data["pojisteny"]
            pojisteni_pojisteny.cena = form.cleaned_data["cena"]
            pojisteni_pojisteny.predmet_pojisteni = form.cleaned_data["predmet_pojisteni"]
            pojisteni_pojisteny.platnost_od = form.cleaned_data["platnost_od"]
            pojisteni_pojisteny.platnost_do = form.cleaned_data["platnost_do"]
            pojisteni_pojisteny.save()

            return redirect("pojisteni_index")
        return render(request, self.template_name, {"form": form})


class PojistenyCurrent(generic.DetailView):
    model = Pojisteny
    template_name = "pojisteni_app/pojisteny_detail.html"



    def get_queryset(self):
        return Pojisteny.objects.all().order_by("-id")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pojisteni_pojisteny = PojisteniPojisteny.objects.filter(pojisteny=self.object).first()
        return context

    def get(self, request, pk):
        try:
            pojisteny = self.get_object()
        except:
            return redirect("pojistenci_index")
        return render(request, self.template_name, {"pojisteny": pojisteny})

    def post(self, request, pk):
        if request.user.is_authenticated:
            if "edit" in request.POST:
                return redirect("edit_pojisteny", pk=self.get_object().pk)
            elif "edit_pojisteni" in request.POST:
                pojisteni_pojisteny = get_object_or_404(PojisteniPojisteny, pk=pk)
                return redirect("edit_pp", pk=pojisteni_pojisteny.get_object().pk)
            elif "delete_pojisteni" in request.POST:
                if not request.user.is_admin:
                    messages.info(request, "Nemáte práva pro smazání pojištění.")
                    return redirect("pojisteni_index")
                else:
                    pojisteni_pojisteny_id = request.POST.get("delete_pojisteni")
                    pojisteni_pojisteny = get_object_or_404(PojisteniPojisteny, pk=pojisteni_pojisteny_id)
                    pojisteni_pojisteny.delete()
            elif "nove" in request.POST:
                return redirect("nove_pp")
            else:
                if not request.user.is_admin:
                    messages.info(request, "Nemáte práva pro smazání pojištěnéno.")
                    return redirect("pojistenci_index")
                else:
                    self.get_object().delete()
            return redirect("pojistenci_index")

class PojistenyIndex(generic.ListView):

    template_name = "pojisteni_app/pojisteny_index.html"
    context_object_name = "pojisteny"
    paginate_by = 6

    def get_queryset(self):
        queryset = Pojisteny.objects.all().order_by("-id")
        return queryset  

    def get(self, request):
        try:
            pojisteny = self.get_queryset()
            paginator = Paginator(pojisteny, self.paginate_by)
            page_number = self.request.GET.get('page')
            page = paginator.get_page(page_number)
        except:
            return redirect("pojistenci_index")
        return render(request, self.template_name, {"pojisteny": page})

    def post(self, request):
        if request.user.is_authenticated:
            if "edit" in request.POST:
                pojisteny_id = request.POST.get("edit")
                return redirect("edit_pojisteny", pk=pojisteny_id)
            elif "delete" in request.POST:
                if not request.user.is_admin:
                    messages.info(request, "Nemáte práva pro smazání pojištění.")
                else:
                    pojisteny_id = request.POST.get("delete")
                    pojisteny = get_object_or_404(Pojisteny, pk=pojisteny_id)
                    pojisteny.delete()
            return redirect("pojistenci_index")

class PojisteniIndex(generic.ListView):
    paginate_by = 6
    template_name = "pojisteni_app/pojisteni_index.html"
    context_object_name = "pojisteni"


    def get_queryset(self):
        queryset = Pojisteni.objects.all().order_by("-id")
        paginator = Paginator(queryset, self.paginate_by)
        page_number = self.request.GET.get('page')
        page = paginator.get_page(page_number)
        return page

    def get(self, request):
        try:
            pojisteni = self.get_queryset()
        except:
            return redirect("pojisteni_index")
        return render(request, self.template_name, {"pojisteni": pojisteni})

    def post(self, request):
        if request.user.is_authenticated:
            if "edit" in request.POST:
                pojisteni_id = request.POST.get("pk")
                return redirect("edit_pojisteni", pk=pojisteni_id)

            elif "delete" in request.POST:
                if not request.user.is_admin:
                    messages.info(request, "Nemáte práva pro smazání pojištění.")
                else:
                    pojisteni_id = request.POST.get("pk")
                    if pojisteni_id:
                        pojisteni = get_object_or_404(Pojisteni, pk=pojisteni_id)
                        pojisteni.delete()
                        messages.success(request, "Pojištění bylo smazáno.")
                    else:
                        messages.error(request, "Nebylo poskytnuto platné ID pojištěnce.")

            return redirect("pojisteni_index")


class UdalostIndex(generic.ListView):
    paginate_by = 6
    template_name = "pojisteni_app/udalosti.html"
    context_object_name = "udalosti"

    def get_queryset(self):
        queryset = Udalosti.objects.all().order_by("-id")
        return queryset

    def post(self, request):
        if request.user.is_authenticated:
            if "edit" in request.POST:
                udalost_id = request.POST.get("pk")
                return redirect("edit_udalost", pk=udalost_id)

            elif "delete" in request.POST:
                if not request.user.is_admin:
                    messages.info(request, "Nemáte práva pro smazání události.")
                else:
                    udalosti_id = request.POST.get("pk")
                    if udalosti_id:
                        udalost = get_object_or_404(Udalosti, pk=udalosti_id)
                        udalost.delete()
                        messages.success(request, "Událost byla smazána.")
                    else:
                        messages.error(request, "Nebylo poskytnuto platné ID událost.")

            return redirect("udalosti")

class PojistenyCreate(LoginRequiredMixin,generic.edit.CreateView):

    form_class = PojistenyForm
    template_name = "pojisteni_app/pojisteny_create.html"

    def get(self, request):
        if not request.user.is_admin:
            messages.info(request, "Nemáte práva pro přídání pojištěného.")
            return redirect("pojistenci_index")
        form = self.form_class(None)
        return render(request, self.template_name, {"form": form})

    def post(self, request):
        if not request.user.is_admin:
            messages.info(request, "Nemáš práva pro přidání pojištěného.")
            return redirect("pojistenci_index")
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return redirect("pojistenci_index")
        return render(request, self.template_name, {"form": form})

class PojisteniCreate(LoginRequiredMixin,generic.edit.CreateView):

    form_class = PojisteniForm
    template_name = "pojisteni_app/pojisteni_create.html"

    def get(self, request):
        if not request.user.is_admin:
            messages.info(request, "Nemáte práva pro přídání pojištění.")
            return redirect("pojisteni_index")
        form = self.form_class(None)
        return render(request, self.template_name, {"form": form})

    def post(self, request):
        if not request.user.is_admin:
            messages.info(request, "Nemáš práva pro přidání pojištění.")
            return redirect("pojisteni_index")
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return redirect("pojisteni_index")
        return render(request, self.template_name, {"form": form})

class UdalostForm(generic.edit.CreateView):
    form_class = UdalostiForm
    template_name = "pojisteni_app/udalosti_create.html"

    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {"form": form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return redirect("udalosti")
        return render(request, self.template_name, {"form": form})

class PojisteniPojistenyCreate(LoginRequiredMixin,generic.edit.CreateView):

    form_class = PojisteniPojistenyForm
    template_name = "pojisteni_app/pp_create.html"

    def get(self, request):
        if not request.user.is_admin:
            messages.info(request, "Nemáte práva pro přídání pojištění.")
            return redirect("pojisteni_index")
        form = self.form_class(None)
        return render(request, self.template_name, {"form": form})

    def post(self, request):
        if not request.user.is_admin:
            messages.info(request, "Nemáš práva pro přidání pojištění.")
            return redirect("pojisteny_detail", pk=PojisteniPojisteny.pojisteny.pk)
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save(commit=True)
            pojisteni_pojisteny = form.instance
            return redirect("pojisteny_detail", pk=pojisteni_pojisteny.pojisteny.pk)
        return render(request, self.template_name, {"form": form})

class UzivatelViewRegister(generic.edit.CreateView):
    form_class = UzivatelForm
    model = Uzivatel
    template_name = "pojisteni_app/register_form.html"

    def get(self, request):
        if request.user.is_authenticated:
            messages.info(request, "Jste přihlášený, nemůžete se registrovat.")
            return redirect("pojistenci_index")
        else:
            form = self.form_class(None)
        return render(request, self.template_name, {"form": form})

    def post(self, request):
        if request.user.is_authenticated:
            messages.info(request, "Jste přihlášený, nemůžete se registrovat.")
            return redirect("pojistenci_index")
        form = self.form_class(request.POST)
        if form.is_valid():
            uzivatel = form.save(commit=False)
            password = form.cleaned_data["password"]
            uzivatel.set_password(password)
            uzivatel.save()
            login(request, uzivatel)
            return redirect("pojistenci_index")

        return render(request, self.template_name, {"form": form})


class UzivatelViewLogin(generic.edit.CreateView):
    form_class = LoginForm
    template_name = "pojisteni_app/login_form.html"

    def get(self, request):
        if request.user.is_authenticated:
            messages.info(request, "Jste přihlášený, nemůžete se přihlášit znovu.")
            return redirect("pojistenci_index")
        else:
            form = self.form_class(None)
        return render(request, self.template_name, {"form": form})

    def post(self, request):
        if request.user.is_authenticated:
            messages.info(request, "Jste přihlášený, nemůžete se přihlášit znovu.")
            return redirect("pojistenci_index")
        form = self.form_class(request.POST)
        if form.is_valid():
            email = form.cleaned_data["email"]
            password = form.cleaned_data["password"]
            user = authenticate(email=email, password=password)
            if user:
                login(request, user)
                return redirect("pojistenci_index")
            else:
                messages.error(request, "Tento účet neexistuje.")
        return render(request, self.template_name, {"form": form})

class AboutView(TemplateView):
    template_name = "pojisteni_app/about.html"


def logout_user(request):
    if request.user.is_authenticated:
        logout(request)
    else:
        messages.info(request, "Nemůžeš se odhlásit pokud nejsi přihlášený.")
    return redirect("login")

