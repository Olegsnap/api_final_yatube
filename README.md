# API для Yatube

### Описание
Проект девятого спринта от Яндекс.Практикум. Позволяет взаимодействовать с социальной сетью Yatube через API. Доступны просмотр, создание и изменение публикаций, комментариев, подписок на авторов. Доступен просмотр списка групп. Установка проекта и примеры взаимодействия описаны ниже.

### Как запустить проект:
Клонировать репозиторий и перейти в него в командной строке:
```
git clone https://github.com/Olegsnap/api_final_yatube
cd api_final_yatube
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
Создать суперпользователя:
```
python manage.py createsuperuser
```
Запустить проект:
```
python3 manage.py runserver
```

**Примеры работы с API для неавторизованных пользователей**
- ```GET api/v1/posts/``` - получить список всех публикаций.
- ```GET api/v1/posts/{post_id}/``` - получить публикацию по id
- ```GET api/v1/groups/``` - получение списка доступных сообществ
- ```GET api/v1/groups/{group_id}``` - получить сообщество по id
- ```GET api/v1/{post_id}/comments/``` - получение всех комментариев к публикации
- ```GET api/v1/{post_id}/comments/{comment_id}/``` - Получение комментария к публикации по id

**Получение токена для пользователя**
- ```POST api/v1/jwt/create/``` - Получение токена (необходимо указать логин и пароль пользователя в параметрах)

**Примеры работы с API для авторизованных пользователей**
- ```POST api/v1/posts/``` - создание публикации
- ```PUT api/v1/posts/{post_id}``` - обновление публикации с указанным id
- ```PATCH api/v1/posts/{post_id}``` - частичное обновление публикации с указанным id
- ```DELETE api/v1/posts/{post_id}``` - удаление публикации с указанным id
- ```POST api/v1/{post_id}/comments/``` - создание комментария к посту с указанным id 
- ```PUT api/v1/{post_id}/comments/{comment_id}/``` - обновление комментария с указанным id к посту с указанным id 
- ```PATCH api/v1/{post_id}/comments/{comment_id}/``` - частичное обновление комментария с указанным id к посту с указанным id 
- ```DELETE api/v1/{post_id}/comments/{comment_id}/``` - удаление комментария с указанным id к посту с указанным id 
- ```GET api/v1/follow/``` - получение списка подписок
- ```POST api/v1/follow/``` - подписка пользователя на автора

### Автор
Олег Асташкин :koala:
[<img src='https://cdn.jsdelivr.net/npm/simple-icons@3.0.1/icons/github.svg' alt='github' height='40'>](https://github.com/Olegsnap)
