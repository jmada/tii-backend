# TI Invetory Management System

## This is a simple API for:

- Creating an unique interface for keeping on track the goods that you manage.

## Schema

- User

  - email
  - password
  - groups: user or admin (can only belong to one)

- Item

  - title
  - description

- UserItem

  - user_id
  - item_id
