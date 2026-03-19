# Общий смысл

### (не совсем правильно, написано под github)

Наш **workflow** (ci.yaml) запускается при каждом пуше в ветку **main** и делает следующее:

- Клонирует репозиторий на сервер

- Настраивает Python 3.13

- Устанавливает зависимости

- Прогоняет **black** (форматирует код)

Эти действия производятся на серверах Github

Сам workflow с разбором
```yaml
# Название Workflow
name: Code Refactoring

# Событие, которое запускает этот процесс
on:
  push:
    branches:
      - main  # Запуск при пуше в ветку main

# Работа, которая будет сделана 
jobs:
  refactor:
    name: Lint & Format Code  # Название задачи
    runs-on: ubuntu-latest  # Операционная система для выполнения задач, в данном случае Ubuntu (на серверах Github)

    steps:
      # Клонирование репозитория на сервер
      - name: Checkout Repository
        uses: actions/checkout@v4

      # Установка Python
      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: "3.13"

      # Обновление pip
      - name: Upgrade pip
        run: python -m pip install --upgrade pip  # Обновление pip до последней версии, чтобы избежать проблем с устаревшими версиями

      # Установка зависимостей
      - name: Install Dependencies
        run: pip install -r requirements.txt

      # Форматирование с помощью Black
      - name: Run Black
        run: black .
```