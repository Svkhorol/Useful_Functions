import pandas as pd
import os


def concat_csv(root_path, file_name='data.csv'):
    """
    Данная функция принимает путь к папке и возвращает датафрейм пандаса.
    Parameters
    ---------
    root_path: str
        Путь к папке
    file_name: str, default 'data.csv'
        Название csv-файла в формате 'name.csv'
        Если этот параметр не указан, то считываются файлы с названием 'data.csv'
    Returns: DataFrame
    """

    # Создаем пустой датафрейм df1
    df1 = pd.DataFrame()

    # Итерация по списку папок в корневой папке
    for date in os.listdir(root_path):  # каждая папка - дата (date)
        user_path = os.path.join(root_path, date)  # сохраняем путь корневая папка + вложенная папка 1-го уровня

        # Итерация по списку папок во вложенной папке 1-го уровня
        for user in os.listdir(user_path):  # каждая папка - Имя_Фамилия (user)

            # Получаем путь каждого csv-файла с помощью os.path.join
            # Считываем каждый файл в датафрейм df2 с помощью read_csv
            df2 = pd.read_csv(os.path.join(user_path, user, file_name))

            # Добавляем в датафрейм df2 колонки даты (date) и имени покупателя (user) из переменных цикла (они же - названия папок)
            df2['date'], df2['user'] = date, user

            # Присоединяем считанный датафрейм df2 к созданному ранее df1 с помощью pd.concat (вертикально по умолчанию)
            df1 = pd.concat([df1, df2], ignore_index=True)  # индексы будут по порядку

    # Удаляем колонку со старыми индексами с помощью drop
    df1 = df1.drop(columns='Unnamed: 0')

    # Возвращается итоговый датафрейм
    return df1
