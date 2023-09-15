from django import forms
from .models import Pojisteny, Pojisteni, Uzivatel, PojisteniPojisteny, Udalosti
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Row, Column
class PojistenyForm(forms.ModelForm):

    class Meta:
        model = Pojisteny
        fields = ["jmeno", "prijmeni", "ulice", "mesto", "psc", "tel", "email"]
        labels = {"jmeno": "Jméno", "prijmeni": "Příjmení", "ulice": "Ulice", "mesto": "Město", "psc": "PSČ", "tel": "Telefon", "email":" e-mail"}

    def __init__(self, *args, **kwargs):
        super(PojistenyForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(

        )
class PojisteniForm(forms.ModelForm):

    class Meta:
        model = Pojisteni
        fields = ["typ_pojisteni"]
        labels = {"typ_pojisteni": "Typ pojištění"}

    def __init__(self, *args, **kwargs):
        super(PojisteniForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout()

class PojisteniPojistenyForm(forms.ModelForm):

    class Meta:
        model = PojisteniPojisteny
        fields = ["pojisteni", "pojisteny", "cena", "predmet_pojisteni", "platnost_od", "platnost_do"]
        labels = {
            "pojisteni": "Pojištění",
            "pojisteny": "Pojištěný",
            "cena": "Cena",
            "predmet_pojisteni": "Předmět pojištění",
            "platnost_od": "Platnost od: |rok-mesic-den| ",
            "platnost_do": "Platnost do: |rok-mesic-den|",
        }



class UdalostiForm(forms.ModelForm):

    class Meta:
        model = Udalosti
        fields = ["cislo_pojistne_smlouvy", "pojisteni", "popis_udalosti", "datum_udalosti"]
        labels = {
            "cislo_pojistne_smlouvy": "Číslo pojistné smlouvy",
            "pojisteni": "Pojištění",
            "popis_udalosti": "Popis události",
            "datum_udalosti": "Datum události",
        }
    def __init__(self, *args, **kwargs):
        super(UdalostiForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
        )


class PojisteniUserForm(forms.ModelForm):

    class Meta:
        model = Pojisteni
        fields = ["typ_pojisteni"]
        labels = {"typ_pojisteni": "Typ pojištění"}

    def __init__(self, *args, **kwargs):
        super(PojisteniUserForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout()

class UzivatelForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Uzivatel
        fields = ["email", "password"]

class LoginForm(forms.Form):
    email = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        fields = ["email", "password"]