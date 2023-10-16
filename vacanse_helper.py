class VacancyOperator:
    """Класс для валидации данных и сравнения вакансий по минимальной зарплате"""

    def __init__(self, valid_vacancies_list):
        self.valid_vacancies_list = valid_vacancies_list

    def two_vac_comp_by_min_sal(self, first_num, second_num):
        """Метод сравнения двух вакансий по минимальной зарплате"""
        min_salary_1 = self.valid_vacancies_list[first_num - 1]["От"]
        min_salary_2 = self.valid_vacancies_list[second_num - 1]["От"]

        return min_salary_1 >= min_salary_2


    def get_top_n_vacancies_by_sal(self, vac_count):
        """Получение топ N вакансий"""
        source_list = self.valid_vacancies_list
        final_sorted = sorted(source_list,
                              key=lambda d: d["От"], reverse=True)

        return final_sorted[:vac_count]

    def get_all_valid_vacancies(self):
        """Получение всех вакансий"""
        return self.valid_vacancies_list