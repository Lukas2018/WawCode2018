from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.user.username)


class UserEvent(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tytul = models.CharField(max_length=40)
    opis = models.CharField(max_length=100)
    lokalizacjaNS = models.FloatField()
    lokalizacjaWE = models.FloatField()
    dataOd = models.DateTimeField()

    def __str__(self):
        return str(self.tytul)


class Lokal(models.Model):
    nazwa = models.CharField(max_length=40)
    adres = models.CharField(max_length=200)
    coordinates = models.CharField(max_length=100, blank=True, null=True)
    # lokalizacjaNS = models.FloatField()
    # lokalizacjaWE = models.FloatField()
    cenaPiwa = models.FloatField(blank=True, null=True)
    cenaWodki = models.FloatField(blank=True, null=True)
    jedzenie = models.BooleanField(default=False)
    regionalne = models.BooleanField(default=False)
    karaoke = models.BooleanField(default=False)
    godzinyOtwarcia = models.TextField()
    palarnia = models.BooleanField(default=False)
    ogrodek = models.BooleanField(default=False)
    ladowanieTelefonu = models.BooleanField()
    parkiet = models.BooleanField(default=False)
    mecze = models.BooleanField(default=False)
    jaki_mecz = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return str(self.nazwa)


class Komentarz(models.Model):
    nick = models.ForeignKey(User, on_delete=models.CASCADE)
    lokal = models.ForeignKey(Lokal, on_delete=models.CASCADE)
    tekst = models.CharField(max_length=100)
    ileGwiazdek = models.IntegerField()

    def __str__(self):
        return str(self.nick)


class WydarzenieLokalu(models.Model):
    lokal = models.ForeignKey(Lokal, on_delete=models.CASCADE)
    tytul = models.CharField(max_length=40)
    opis = models.CharField(max_length=100)
    godzinaOd = models.DateTimeField()

    def __str__(self):
        return str(self.tytul)


class Polubienie(models.Model):
    lokal = models.ForeignKey(Lokal, on_delete=models.CASCADE)
    nick = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.nick} polubił {self.lokal}"


class Wlasciciel(models.Model):
    wlasciciel = models.OneToOneField(User, on_delete=models.CASCADE)
    lokal = models.ForeignKey(Lokal, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.wlasciciel.username} polubił {self.lokal.nazwa}"
