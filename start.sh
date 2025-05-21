#!/bin/bash

echo "Ожидание готовности базы данных..."
sleep 10

echo "Запуск миграций..."
alembic upgrade head
if [ $? -ne 0 ]; then
    echo "Ошибка при выполнении миграций"
    exit 1
fi

echo "Инициализация базы данных..."
python3 init_db.py
if [ $? -ne 0 ]; then
    echo "Ошибка при инициализации базы данных"
    exit 1
fi

echo "Запуск приложения..."
python3 main.py
