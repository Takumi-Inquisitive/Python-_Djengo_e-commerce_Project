# TechStore - Modern eCommerce Platform

A futuristic eCommerce platform built with Django, featuring a modern UI with glassmorphism effects and responsive design.

## Features

- **Homepage**: Showcases featured products, categories, customer reviews, and newsletter signup
- **Product Listing**: Browse products with category filtering
- **Product Details**: View detailed information about each product
- **Shopping Cart**: Add/remove items and manage quantities
- **Checkout Process**: Complete purchases with a streamlined checkout experience
- **Order Summary**: View order details and history
- **Responsive Design**: Works seamlessly on desktop, tablet, and mobile devices
- **Modern UI**: Glassmorphism effects, animations, and a dark theme

## Technology Stack

- **Backend**: Django 5.1
- **Database**: PostgreSQL
- **Frontend**: HTML, CSS, JavaScript
- **Styling**: Custom CSS with modern design principles
- **Icons**: Font Awesome

## Setup Instructions

1. Clone the repository
2. Create a virtual environment: `python -m venv env1`
3. Activate the virtual environment:
   - Windows: `env1\Scripts\activate`
   - Linux/Mac: `source env1/bin/activate`
4. Install dependencies: `pip install -r requirements.txt`
5. Set up the database:
   - Create a PostgreSQL database named `djangoapp1_db`
   - Update database credentials in `settings.py` if needed
6. Run migrations: `python manage.py migrate`
7. Create a superuser: `python manage.py createsuperuser`
8. Run the development server: `python manage.py runserver`
9. Access the admin panel at `http://127.0.0.1:8000/admin/`
10. Add products, categories, and other content through the admin interface

## Project Structure

- `ecommerce/`: Main project directory
  - `ecommerce/`: Project settings and configuration
  - `store/`: Main application
    - `static/`: CSS, JavaScript, and image files
    - `templates/`: HTML templates
    - `models.py`: Database models
    - `views.py`: View functions
    - `urls.py`: URL routing

## Customization

- **Colors**: Edit the CSS variables in `static/css/main.css`
- **Products**: Add or modify products through the admin interface
- **Categories**: Create new categories to organize products
- **Images**: Replace placeholder images in the `static/images` directory

## License

This project is licensed under the MIT License - see the LICENSE file for details. 