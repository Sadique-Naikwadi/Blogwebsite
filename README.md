# Blog Web Application

This is a simple blog web application built with Django. The application allows users to create, edit, delete, and view blog posts. The application also supports user authentication.

## Features

- User authentication (sign up, login, logout)
- Create, edit, delete, and view blog posts
- Send emails to users
- Sitemap generation
- RSS feed for blog posts
- Responsive design

## Requirements

- Python 3.10.1+
- Django 4.2+

## Installation

1. Clone the repo.
2. Install dependencies: `pip install -r requirements.txt`.
3. Run migrations: `python manage.py migrate`.
4. Open your web browser and go to `http://127.0.0.1:8000/` to see the application.

## Usage

1. Register a new user or log in with an existing account.
2. Create a new blog post by clicking on the "New Post" button.
3. Edit or delete your posts from the post detail page.
4. View all posts on the homepage.
5. Send emails to users from the post detail page.
6. Access the sitemap at `http://127.0.0.1:8000/sitemap.xml`.
7. Subscribe to the RSS feed at `http://127.0.0.1:8000/feed/`.
8. Access the Django admin at `http://127.0.0.1:8000/admin/` to manage users and posts.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
