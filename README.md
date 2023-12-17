# Project Overview: REST Framework API Using Django

## Abstract:

This project focuses on the development of a RESTful API using Django and the Django REST Framework (DRF). The primary goal is to showcase the implementation of core concepts such as Django setup, model serialization, authentication, routers, and the use of generic or model viewsets. The project adheres to best practices in API development and serves as a comprehensive example of a fully functional API system.

## Database:

### Customers:
- **customer_id (PK)**
- first_name
- last_name

### Products:
- **ID (PK)**
- Name
- Price

### Orders:
- **ID (PK)**
- CustomerID (FK)
- ProductID (FK)
- Quantity
- CreatedAt

### Reviews:
- **ID (PK)**
- CustomerID (FK)
- ProductID (FK)
- Rating
- Review

## Task To-Do:

### Setting Up Django Environment:

1. **Install Dependencies:**
   - Django
   - Django REST Framework

2. **Create Django Project:**
   - `django-admin startproject projectname`

3. **Create Django App:**
   - `python manage.py startapp appname`

4. **Configure Database:**
   - Define models in `models.py`.
   - Run migrations: `python manage.py makemigrations` and `python manage.py migrate`.

5. **Add App to Settings:**
   - Include the app in the `INSTALLED_APPS` section of `settings.py`.

### Implementing Model Serializers:

1. **Create Serializers:**
   - Define serializers for models in `serializers.py`.
   - Use DRF serializers for converting data types.

2. **Update Views:**
   - Modify views to use the newly created serializers for serialization and deserialization.

### Integrating Authentication Mechanisms:

1. **Choose Authentication Method:**
   - Select authentication method (e.g., token authentication).

2. **Configure Authentication Classes:**
   - Update `settings.py` to include chosen authentication classes.

### Applying Routers for URL Management:

1. **Install Routers:**
   - `pip install djangorestframework`

2. **Configure Routers:**
   - Set up routers in `urls.py` to manage URL routing.

### Utilizing Generic or Model Viewsets:

1. **Create Viewsets:**
   - Define generic or model viewsets in `views.py`.
   - Utilize DRF's viewsets for efficient interaction with the database.

2. **Wire Viewsets to URLs:**
   - Connect viewsets to routers for automatic URL generation.

---

This README provides an overview of the project, including its goals, database structure, and a step-by-step guide to setting up the Django environment, implementing model serializers, integrating authentication mechanisms, applying routers for URL management, and utilizing generic or model viewsets. Follow the outlined tasks to create a robust RESTful API using Django and DRF.
