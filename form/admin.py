from django.contrib import admin
from .models.animal import Animal
from .models.cheptel import Cheptel
from .models.race import Race
from .models.preleveur import Preleveur

admin.site.register(Animal)
admin.site.register(Cheptel)
admin.site.register(Race)
admin.site.register(Preleveur)