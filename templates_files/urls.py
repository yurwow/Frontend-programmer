from django.urls import path

from .views import DemendPage, GeographyPage, HomePage, LastVacancyPage, SkillsPage


urlpatterns = [
    path('', HomePage, name='homePage'),
    path('DemendPage/', DemendPage, name='demendPage'),
    path('GeographyPage/', GeographyPage, name='geographyPage'),
    path('SkillsPage/', SkillsPage, name='skillsPage'),
    path('LastVacancyPage/', LastVacancyPage, name='lastVacancyPage'),
]