# Сервис для публикации вакансий

Сервис позволяет публиковать вакансии (Раздел находится в разработке)

## Как установить

Сервис упакован в контейнеры, для запуска проекта локально или на сервере в директории `./job_finder` нужно создать `.env` файл и записать в него следующие переменные:
```dotenv
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
POSTGRES_SERVER=db
POSTGRES_PORT=5432
POSTGRES_DB=postgres

TLS_MODE=off
SITE_HOST=localhost
```
(Раздел находится в разработке)

### Запуск Docker-compose
В корневой директории выполнить следующую команду:
```bash
docker-compose up --build
```
# Описание работы сервиса
Раздел находится в разработке

# Цели проекта

Код написан в учебных целях, ознакомление с фреймворком FastAPI
