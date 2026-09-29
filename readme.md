# Python/Django Box Selection System

## Overview

This project is a Django-based system that recommends a suitable shipping box for a product.

The system checks:

- Product dimensions
- Product weight
- Box internal dimensions
- Box maximum weight capacity
- Box cost

Among the boxes that can contain the product and support its weight, the system recommends the lowest-cost suitable box.

## Technologies

- Python
- Django
- SQLite
- Django Test Framework

## Project Structure

```text
box_selection/
├── box_selector/
│   ├── migrations/
│   ├── admin.py
│   ├── models.py
│   ├── services.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── config/
├── .gitignore
├── TEST_OUTPUT.md
├── manage.py
└── README.md