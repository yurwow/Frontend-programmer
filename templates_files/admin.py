from django.contrib import admin
from .models import LastVacancyModel
from .models import Main
from .models import Navigation
from .models import Demand
from .models import Geography
from .models import Skills


admin.site.register(Main)
admin.site.register(Navigation)
admin.site.register(Demand)
admin.site.register(Geography)
admin.site.register(Skills)

admin.site.register(LastVacancyModel)
