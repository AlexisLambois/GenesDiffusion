from django.contrib import admin
from form.models.animal import Animal
from form.models.cheptel import Cheptel
from form.models.race import Race
from form.models.preleveur import Preleveur
from form.models.prelevement import Prelevement
from form.models.genotypage import Genotypage

admin.site.register(Cheptel)
admin.site.register(Race)
admin.site.register(Preleveur)
admin.site.register(Animal)
admin.site.register(Prelevement)
admin.site.register(Genotypage)