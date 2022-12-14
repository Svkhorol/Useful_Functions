## Function for working with folders and files using OS module
**Функция для работы с папками и файлами с помощью библиотеки OS**  
  
Функция **concat_csv(root_path, file_name='data.csv')** собирает все данные из папки со вложенной струкурой в один датафрэйм, имеющий следующие столбцы: колонки из самих файлов, а также колонки, соответствующие названию папок, в которых хранится файл.  
  
**`Parameters:`**  
 - `root_path`: str,  путь к папке  
 - `file_name`: str, default 'data.csv',  название csv-файла в формате 'name.csv'  
  Если этот параметр не указан, то считываются файлы с названием 'data.csv'  
  
**`Returns:`** DataFrame  
  
В дальнейшем планируется усовершенствование функции, добавление возможности работы с большим числом вложенных каталогов и др.
  
**Используемые инструменты:**  
Python 3  
Библиотека Pandas  
Библиотека OS    
  
**Содержание:**  
[`concat_csv.py`](https://github.com/Svkhorol/Useful_Functions/blob/main/concat_csv/concat_csv.py): код функции в Python с подробными комментариями    
[`description.ipynb`](https://github.com/Svkhorol/Useful_Functions/blob/main/concat_csv/description.ipynb): ноутбук Jupyter c описанием функции и примером её работы  
[`data_os.zip`](https://github.com/Svkhorol/Useful_Functions/blob/main/concat_csv/data_os.zip): архив каталога с данными из примера  
`Readme.md`: этот файл
