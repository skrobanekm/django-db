from django.contrib import admin
from .models import Chovatel, Zvire, Oceneni

# Register your models here.
admin.site.register(Chovatel)
admin.site.register(Zvire)
admin.site.register(Oceneni)