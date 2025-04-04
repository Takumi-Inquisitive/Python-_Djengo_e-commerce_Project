# TechStore - E-Commerce Website

A modern e-commerce website built with Django, featuring a responsive design and user-friendly interface.

## Features

- User authentication (login, register, logout)
- Product browsing and filtering by category
- Shopping cart functionality
- Order management
- Product reviews and ratings
- Responsive design with modern UI
- Secure checkout process

## Technologies Used

- Django 5.1.7
- SQLite3 (development database)
- Bootstrap 5
- Crispy Forms
- Font Awesome icons
- Custom CSS and JavaScript

## Setup Instructions

1. Clone the repository:
```bash
git clone <repository-url>
cd ecommerce
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Apply migrations:
```bash
python manage.py migrate
```

5. Create a superuser:
```bash
python manage.py createsuperuser
```

6. Run the development server:
```bash
python manage.py runserver
```

7. Visit http://127.0.0.1:8000/ in your browser

## Project Structure

- `store/` - Main application directory
  - `models.py` - Database models
  - `views.py` - View functions
  - `urls.py` - URL patterns
  - `forms.py` - Form classes
  - `templates/` - HTML templates
  - `static/` - Static files (CSS, JS, images)

## Contributing

1. Fork the repository
2. Create a new branch
3. Make your changes
4. Submit a pull request

## License

This project is licensed under the MIT License. 