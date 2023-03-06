# API для Yatube

### Описание
Проект девятого спринта от Яндекс.Практикум

### Как запустить проект:
Клонировать репозиторий и перейти в него в командной строке:
```
git clone https://github.com/Olegsnap/api_final_yatube
cd kittygram_backend
```
Cоздать и активировать виртуальное окружение:
```
python -m venv venv
source venv/scripts/activate
```
Обновить pip:
```
python3 -m pip install --upgrade pip
```
Установить зависимости из файла requirements.txt:
```
pip install -r requirements.txt
```
Выполнить миграции:
```
python3 manage.py migrate
```
Запустить проект:
```
python3 manage.py runserver
```

**Примеры работы с API для неавторизованных пользователей**
- ```GET api/v1/posts/``` - получить список всех публикаций.
- ```GET api/v1/groups/``` - получение списка доступных сообществ
- ```GET api/v1/{post_id}/comments/``` - получение всех комментариев к публикации
- ```GET api/v1/{post_id}/comments/{id}/``` - Получение комментария к публикации по id

### Автор
Олег Асташкин ([GitHub Profile](https://github.com/Olegsnap))
