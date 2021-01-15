# TI Invetory Management System

## This is a simple API for:

- Creating an unique interface for keeping on track the goods that you manage.

## Schema

- User

  - email
  - password
  - groups: user or admin (can only belong to one)

- UserProfile

  - first_name
  - last_name
  - image
  - created_at

- Item

  - description
  - brand_id
  - model_id
  - operating_system_id
  - serial_number
  - image
  - created_at
  - updated_at

- UserItem

  - user_id
  - item_id

- Brand

  - name
  - description
  - created_at
  - updated_at

- Model

  - name
  - description
  - created_at
  - updated_at

- Operating System

  - name
  - description
  - created_at
  - updated_at
