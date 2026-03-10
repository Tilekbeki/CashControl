@echo off

REM Запуск виртуального окружения (предполагается, что виртуальное окружение находится в папке venv)
call myvenv\Scripts\activate

REM Запуск Django сервера
cd C:\Users\tilek\Desktop\web projects\CashControl\cashcontrol
start cmd /k "python manage.py runserver"

REM Переход в папку с React проектом (замените на вашу папку)
cd C:\Users\tilek\Desktop\web projects\CashControl\front

start cmd /k "npm run start"

