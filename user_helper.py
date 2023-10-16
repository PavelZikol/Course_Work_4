from vacanse_helper import VacancyOperator
from json_helper import JsonOperator


class UserHelper:
    """Класс пользовательского интерфейса"""

    def __init__(self, vac_list):
        """Инициализация для работы с пользователем"""
        self.vac_list = vac_list

    @staticmethod
    def functions_choosing():
        """Выбор функции"""
        function_input = input(f"Доступны следующие действия:\n1 - Список доступных вакансий\n2 - Удалить файл Json)\n0 - Выйти\n")
        return function_input

    def func(self):
        """Возможности"""
        if len(self.vac_list) > 0:
            print(f"Я нашла вот столько вакансий: {len(self.vac_list)}.")
            while True:
                chosen_func = self.functions_choosing()

                # Вывод полного списка вакансий
                if chosen_func == "1":
                    all_vac_inst_1 = VacancyOperator(self.vac_list)
                    all_vac = output_formatting(all_vac_inst_1.get_all_valid_vacancies())
                    for item in all_vac:
                        print(item)

                #Удалить Json файл со всеми вакансиями
                if chosen_func == "2":
                    JsonOperator.delete_from_json()
                    print(f"Я удалила этот несчастый файл, я молодец?)")
                    break


                if chosen_func == "0":
                    break

                # Если ошибся
                if chosen_func not in ["0", "1", "2"]:
                    print(f"Сначала выбери функцию!")
                    print()

        else:
            print("Упс. Кажется не нашлось ни одной вакансии с полными данными.")


def output_formatting(hh_vac_valid_list):
    """Метод для преобразования json формата в читабельный формат"""
    hh_formed_vac = []
    counter = 1
    for vacancy in hh_vac_valid_list:
        vacancies_items = f"""Вакансия № {counter}
Ваша вакансия: {vacancy["Ваша вакансия"]}
Ссылка на вакансию: {vacancy["Ссылка на вакансию"]}
От: {vacancy["От"]}
До: {vacancy["До"]}
Валюта: {vacancy["Валюта"]}\n"""

        hh_formed_vac.append(vacancies_items)
        counter += 1
    return hh_formed_vac