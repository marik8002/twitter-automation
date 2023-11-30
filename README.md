# Софт для автоматизации твиттер фермы

**Мой тг канал (следите за обновлениями) - https://t.me/easypeoff**

## Установка

**Способ 1**

- Создать виртуальное окружение

```
python -m venv venv
```

- Активировать виртуальное окружение (нужно будет делать каждый раз перед запуском софта)

Для пользователей Windows:

```
venv/Scripts\activate
```
Для пользователей Mac и linux:

```
source venv/Scripts/activate
```

- Установить зависимости
```
pip install -r requirements.txt
```

**Способ 2**
- Установить poetry https://python-poetry.org/docs/

- Активировать виртуальное окружение (нужно будет делать каждый раз перед запуском софта)
```
poetry shell
```
- Установить зависимости

```
poetry install
```

## Настройка
Скоро допишу

config.py - основной файл с настройками

modules_settings.py - настройки модулей

В data/ находятся примеры нужных файлов

accounts.txt - auth token'ы твиттеров

proxies.txt - прокси

user_agents.txt - отпечатки

## Запуск
В активированном виртуальном окружении (см. установку)
```
python main.py
```
