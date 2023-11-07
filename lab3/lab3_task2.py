# TODO Напишите функцию find_common_participants
def find_common_participants(participants_first_group: str, participants_second_group: str, separator = ",") -> list:
    """
    Получение списка участников двух встреч
    :param participants_first_group: участники первой встречи - строка
    :param participants_second_group: участники второй встречи - строка
    :param separator: разделитель, если не "," (необязательный)
    :return: список участников первой и второй встречи
    """

    if not isinstance(participants_first_group, str):
        raise TypeError(f"аргумент participants_first_group должен быть строкой, а не {type(participants_first_group)}")

    if not isinstance(participants_second_group, str):
        raise TypeError(f"аргумент participants_first_group должен быть строкой, а не {type(participants_first_group)}")

    first_list = [i for i in participants_first_group.split(separator)]
    second_list = [i for i in participants_second_group.split(separator)]

    hangout = list(set(first_list) & set(second_list))
    return hangout






if __name__ == "__main__":
    participants_first_group = "Иванов|Петров|Сидоров"
    participants_second_group = "Петров|Сидоров|Смирнов"

    # TODO Провеьте работу функции с разделителем отличным от запятой
    print(find_common_participants(participants_first_group, participants_second_group, "|"))