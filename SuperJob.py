import requests
import os
from abstract_class import CityAndVacancies


class SJApiEngine(CityAndVacancies):
    def __init__(self, city_name, prof_name):
        self.sj_api_url = "https://api.superjob.ru/2.0/"
        self.SUPERJOB = os.getenv("SUPERJOB")
        self.headers = {
            "X-Api-App-Id": self.SUPERJOB
        }
        self.city_name = city_name
        self.prof_name = prof_name

    def get_city_id(self):
        pass

    def get_vacancies(self):
        """Получение всех вакансий выбранного города"""
        sj_vac_url = self.sj_api_url + "/vacancies"
        params = {
            "town": self.city_name,
            "keyword": self.prof_name,
            "count": 100
        }
        response = requests.get(sj_vac_url, params=params, headers=self.headers)

        if response.status_code == 200:
            vacancies = response.json()

        return vacancies["objects"]


def sj_vac_info_validation(sj_vac_source_list):
    """Проверка входящих данных на корректность"""
    hh_valid_vacancies = []
    for vacancies in sj_vac_source_list:
        if isinstance(vacancies["profession"], str):
            vacancy_name = vacancies["profession"]

        if "https://" in vacancies["link"]:
            url = vacancies["link"]

        if vacancies["payment_from"] is not None:
            if (isinstance(vacancies["payment_from"], int) and
                    vacancies["payment_from"] > 0):
                salary_from = vacancies["payment_from"]

            else:
                salary_from = False

            if (isinstance(vacancies["currency"], str) and
                    vacancies["currency"] == "rub"):
                salary_currency = vacancies["currency"]

            else:
                salary_currency = False

            if (isinstance(vacancies["payment_to"], int) and
                    vacancies["payment_to"] > 0):
                salary_to = vacancies["payment_to"]

            else:
                salary_to = False
        else:
            salary_from = salary_currency = salary_to = False

        if vacancies["client"] is not None:
            if ("title" in vacancies["client"]
                    and isinstance(vacancies["client"]["title"], str)):
                employer_name = vacancies["client"]["title"]

            else:
                employer_name = False

        if isinstance(vacancies["candidat"], str):
            requirement = vacancies["candidat"]

        if (vacancy_name and url and salary_from and salary_currency and salary_to
                and employer_name and requirement):
            hh_valid_vacancies.append(vacancies)
    return hh_valid_vacancies


def sj_data_formatting(sj_vac_valid_list):
    """Метод для преобразования json формата в читабельный формат"""
    sj_formed_vac = []
    for vacancy in sj_vac_valid_list:
        vacancies_items = {
            "Ваша вакансия": vacancy["profession"],
            "Ссылка на вакансию": vacancy["link"],
            "От": vacancy["payment_from"],
            "До": vacancy["payment_to"],
            "Валюта": vacancy["currency"]
        }

        sj_formed_vac.append(vacancies_items)
    return sj_formed_vac