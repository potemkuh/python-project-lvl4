### Hexlet tests and linter status:
[![Actions Status](https://github.com/potemkuh/python-project-lvl4/workflows/hexlet-check/badge.svg)](https://github.com/potemkuh/python-project-lvl4/actions)
[![Actions Status](https://github.com/potemkuh/python-project-lvl4/workflows/Super-Linter/badge.svg)](https://github.com/potemkuh/python-project-lvl4/actions)
[![Test Coverage](https://api.codeclimate.com/v1/badges/15cded7c44ba937ad39f/test_coverage)](https://codeclimate.com/github/potemkuh/python-project-lvl4/test_coverage)

Проект развернуть на Heroku: https://thawing-reaches-90961.herokuapp.com/

### Функциональные возможности
-- Приложение настроено на работу с базой данных PostgreSQL;
-- Реализована авторизация пользователей;
-- В системе может быть зарегистрировано множество пользователей;
-- Пользователь после авторизации может создавать себе задачу, указав для этого ее название, описание, статус, назначить исполнителя из списка зарегистрированных пользователей и при необходимости выбрать один или несколко тегов из списка;
-- Пользователь может редактировать содержимое любой своей или чужой задачи;
-- Пользователь может удалить любую из ранее созданных задач;
-- Пользователь может вывести список задач с возможностью фильтрации по статусу, автору, исполнителю, а также по тегам;
-- Пользователь может может добавлять, редактировать и изменять статусы, а также добавлять теги.

### Установка
-- Выполнить команду poetry install для активации виртуального окружения и установки зависимостей
-- Замениете название файла .env.example на .env и задайте свои значения переменных внутри этого файла.
-- Приминить миграции выполнив команду make migrate