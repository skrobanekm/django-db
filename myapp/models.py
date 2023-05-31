from django.db import models

class Chovatel(models.Model):
    cislo_prukazu = models.CharField(max_length=6, verbose_name='Prukaz', help_text='Zadejte číslo průkazu',
                             error_messages={'blank': 'usí být vyplněno'})
    jmeno = models.CharField(max_length=80, verbose_name='Jméno', help_text='Zadejte jméno',
                             error_messages={'blank': 'Jméno musí být vyplněno'})
    prijmeni = models.CharField(max_length=50, verbose_name='Příjmení autora', help_text='Zadejte příjmení autora',
                                error_messages={'blank': 'Příjmení musí být vyplněno'})
    telefon = models.CharField(max_length=16, verbose_name='Telefon',
                               help_text='Zadejte telefon v podobě: +420 777 777 777',
                               blank=True)

    class Meta:
        ordering = ['prijmeni', 'jmeno']
        verbose_name = 'Chovatel'
        verbose_name_plural = 'Chovatele'

    def __str__(self):
        return f'{self.jmeno} {self.prijmeni}'




class Oceneni(models.Model):
    druh_oceneni = models.CharField(max_length=20, verbose_name='Druh oceneni', help_text='Zadejte druh oceneni')

    class Meta:
        ordering = ['druh_oceneni']
        verbose_name = 'Oceneni'
        verbose_name_plural = 'Oceneni'

    def __str__(self):
        return f'{self.druh_oceneni}'

class Zvire(models.Model):
    druh_zvirete = models.CharField(max_length=100, verbose_name='Druh zvirete', help_text='Zadejte Druh zvirete',
                             error_messages={'blank': 'Druh musí být vyplněn'})
    cislo_zvirete = models.CharField(max_length=100, verbose_name='Cislo zvirete', help_text='Zadejte cislo zvirete',
                             error_messages={'blank': 'Musí být vyplněn'})
    chovatel = models.ManyToManyField(Chovatel)
    oceneni = models.ManyToManyField(Oceneni)


    class Meta:
        ordering = ['druh_zvirete']
        verbose_name = 'Druh Zvirete'
        verbose_name_plural = 'Druhy Zvirat'

    def __str__(self):
        return f'{self.druh_zvirete}'