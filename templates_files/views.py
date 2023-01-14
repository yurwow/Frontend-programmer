import re

import requests
from django.shortcuts import render
from .models import LastVacancyModel
from .models import Main
from .models import Navigation
from .models import Demand
from .models import Geography
from .models import Skills

def LastVacancyPage(request):

    class HHAPI:

        def __init__(self, search_text: str):
            self.text = search_text

        def __get_full_vacancies__(self, date: str, count_vac: int) -> list:
            url = 'https://api.hh.ru/vacancies'
            return requests.get(url, dict(text=self.text,
                                          specialization=1,
                                          date_from=f"{date}T00:00:00",
                                          date_to=f"{date}T23:00:00",
                                          per_page=count_vac,
                                          page=1)).json()["items"]

        def get_data_vacancies(self, date: str, count_vac: int):
            data = self.__get_full_vacancies__(date, count_vac)
            result_list = []
            for vac in data:
                url_vac = f'https://api.hh.ru/vacancies/{vac["id"]}'
                resp = requests.get(url_vac).json()
                if resp['salary']:
                    description = ' '.join(re.sub(re.compile('<.*?>'), '', resp['description'])
                                           .strip()
                                           .split())
                    description = description[:100] + '...' if len(description) >= 100 else description
                    result_list.append({'name': resp['name'],
                                        'description': description,
                                        'key_skills': list(map(lambda x: x['name'], resp['key_skills'])),
                                        'employer': resp['employer']['name'],
                                        'salary': f"{resp['salary']['from']} - {resp['salary']['to']} {resp['salary']['currency']}",
                                        'area': resp['area']['name'],
                                        'published_at': resp['published_at'][:10],
                                        'alternate_url': resp['alternate_url']})

            return result_list

    hh = HHAPI('front-end')
    vacs = hh.get_data_vacancies('2022-12-15', 10)

    last_vacancies = LastVacancyModel.objects.all()
    navigation = Navigation.objects.all()
    context = {'vacs': vacs, 'last_vacancies': last_vacancies, 'navigation': navigation}

    return render(request, 'LastVacancyPage.html' , context)

def HomePage(request):
    home_info = Main.objects.all()
    navigation = Navigation.objects.all()
    context = {'navigation': navigation, 'home_info': home_info}
    return render(request, 'HomePage.html', context)

def SkillsPage(request):
    skills_info = Skills.objects.all()
    navigation = Navigation.objects.all()
    context = {'navigation': navigation, 'skills_info': skills_info}
    return render(request, 'SkillsPage.html', context)

def GeographyPage(request):
    geography_info = Geography.objects.all()
    navigation = Navigation.objects.all()
    context = {'navigation': navigation, 'geography_info': geography_info}
    return render(request, 'GeographyPage.html', context)

def DemendPage(request):
    demand_info = Demand.objects.all()
    navigation = Navigation.objects.all()
    context = {'navigation': navigation, 'demand_info': demand_info}
    return render(request, 'DemendPage.html', context)
