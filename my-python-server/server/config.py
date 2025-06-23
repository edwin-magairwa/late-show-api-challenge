import os

DATABASE_URI = os.getenv('DATABASE_URI', 'postgresql://postgres:postgres@localhost/late_show_db')
DEBUG = True  # Set to False in production
SECRET_KEY = os.getenv('SECRET_KEY', 'your_secret_key')
JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY', 'your_jwt_secret_key')

# Add any other configuration settings as needed
