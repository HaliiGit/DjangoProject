from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
# Create your models here.

class Pojisteni(models.Model):
    typ_pojisteni = models.CharField(max_length=100)

    def __str__(self):
        return self.typ_pojisteni

    class Meta:
        verbose_name = "Pojištění"
        verbose_name_plural = "Pojištění"

class Pojisteny(models.Model):
    jmeno = models.CharField(max_length=100)
    prijmeni = models.CharField(max_length=100)
    ulice = models.CharField(max_length=200)
    mesto = models.CharField(max_length=200)
    psc = models.IntegerField(default=0)
    tel = models.CharField(max_length=15)
    email = models.CharField(max_length=180)
    pojisteni = models.ManyToManyField(Pojisteni, through='PojisteniPojisteny')

    def __str__(self):
        return "{} {}| {} | {}".format(self.jmeno ,self.prijmeni, self.email, self.tel)

    def formatted_tel(self):
        number = self.tel
        formatted_number = ' '.join([number[i:i + 3] for i in range(0, len(number), 3)])
        return f'{formatted_number}'
    class Meta:
        verbose_name = "Pojištěný"
        verbose_name_plural = "Pojištěnci"

class PojisteniPojisteny(models.Model):
    pojisteni = models.ForeignKey(Pojisteni, on_delete=models.CASCADE)
    pojisteny = models.ForeignKey(Pojisteny, on_delete=models.CASCADE)
    cena = models.IntegerField(default=0)
    predmet_pojisteni = models.CharField(max_length=100)
    platnost_od = models.DateTimeField()
    platnost_do = models.DateTimeField()

    class Meta:
        verbose_name = "Pojištěný - Pojištění"
        verbose_name_plural = "Pojištěný - Pojištění"

    def __str__(self):
        return "{} {} | {}".format(self.pojisteny.jmeno, self.pojisteny.prijmeni, self.pojisteni.typ_pojisteni)

class Udalosti(models.Model):
    cislo_pojistne_smlouvy = models.IntegerField(default=0)
    pojisteni = models.ForeignKey(Pojisteni, on_delete=models.SET_NULL, null=True)
    popis_udalosti = models.CharField(max_length=1000)
    datum_udalosti = models.DateTimeField()

    def __str__(self):
        return "{} | {} | {}".format(self.pojisteni, self.cislo_pojistne_smlouvy, self.datum_udalosti)

    class Meta:
        verbose_name = "Událost"
        verbose_name_plural = "Události"
class UzivatelManager(BaseUserManager):
    def create_user(self, email, password):
        print(self.model)
        if email and password:
            user = self.model(email=self.normalize_email(email))
            user.set_password(password)
            user.save()
            return user

    def create_superuser(self, email, password):
        user = self.create_user(email, password)
        user.is_admin = True
        user.save()
        return user

class Uzivatel(AbstractBaseUser):

    email = models.EmailField(max_length=200, unique=True)
    is_admin = models.BooleanField(default=False)

    class Meta:
        verbose_name = "uživatel"
        verbose_name_plural = "uživatelé"

    objects = UzivatelManager()

    USERNAME_FIELD = "email"

    def __str__(self):
        return "email: {}".format(self.email)

    @property
    def is_staff(self):
        return self.is_admin
    def has_perm(self, perm, obj=None):
        return True
    def has_module_perms(self, app_label):
        return True
