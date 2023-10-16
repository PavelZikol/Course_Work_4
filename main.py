from HeadHunter import HHApiEngine, hh_vac_info_validation, hh_data_formatting
from SuperJob import SJApiEngine, sj_vac_info_validation, sj_data_formatting
from json_helper import JsonOperator
from user_helper import UserHelper

if __name__ == "__main__":
    print(f"Привет! Я курсовая 4, давайте проверим мою работоспособность\n")
    while True:
        platform_input = input(f"Выбери платформу: 1 - HeadHunter  2 - SuperJob  3- Выйти\n> ")
        if platform_input not in ["1", "2", "3"]:
            print(f"Что-то не так попробуй по новой)")
            print()
        else:
            platform = {
                "1": "HeadHunter",
                "2": "SuperJob"
            }
            if platform_input == "3":
                print("Пока")
                break
            else:
                print(f"Отлично! Ты выбрал платформу {platform[platform_input]}\n")
                city_name_input = input(f"В каком городе хочешь найти вакансию?\n").capitalize()
                prof_input = input(f"Напиши вакансию необходимую вам\n").capitalize()
                if platform_input == "1":
                    hh_block = HHApiEngine(city_name_input, prof_input)
                    vac_source = hh_block.get_vacancies()  # Получение вакансий с HeadHunter
                    hh_valid_vac = hh_vac_info_validation(vac_source)  # Валидация вакансий
                    fin_valid_list = hh_data_formatting(hh_valid_vac)  # Приведение к общему виду

                elif platform_input == "2":
                    sj_block = SJApiEngine(city_name_input, prof_input)
                    vac_source = sj_block.get_vacancies()  # Получение вакансий с SuperJob
                    sj_valid_vac = sj_vac_info_validation(vac_source)  # Валидация вакансий
                    fin_valid_list = sj_data_formatting(sj_valid_vac)  # Приведение к общему виду

            json_list = JsonOperator(fin_valid_list)
            json_list.save_to_json()
            work_vac_list = json_list.get_json()
            user_instance = UserHelper(work_vac_list)
            user_instance.func()