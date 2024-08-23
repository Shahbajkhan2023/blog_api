Blog API Project
Overview
This project is a Django application that implements a simple blog API using Django Rest Framework (DRF). The API allows for creating, retrieving, updating, and deleting blog posts, comments, and users. It also supports categorizing and tagging posts.

Features
Post Management: Create, update, delete, and retrieve blog posts.
Comment Management: Add and view comments on posts.
User Management: View user details.
Categories and Tags: Assign categories and tags to posts.
Authentication: Only authenticated users can perform certain actions.
Requirements
Django 4.2.15
Django Rest Framework 3.15.2
Installation
Clone the Repository

bash
Copy code
git clone <repository_url>
cd <repository_directory>
Create a Virtual Environment

bash
Copy code
python -m venv env
source env/bin/activate  # On Windows use `env\Scripts\activate`
Install Dependencies

bash
Copy code
pip install -r requirements.txt
Apply Migrations

bash
Copy code
python manage.py migrate
Create a Superuser

bash
Copy code
python manage.py createsuperuser
Run the Development Server

bash
Copy code
python manage.py runserver
API Endpoints
Posts

GET /posts/ - List all posts
POST /posts/ - Create a new post
GET /posts/{id}/ - Retrieve a specific post
PUT /posts/{id}/ - Update a specific post
DELETE /posts/{id}/ - Delete a specific post
Comments

GET /comments/ - List all comments
POST /comments/ - Create a new comment
GET /comments/{id}/ - Retrieve a specific comment
PUT /comments/{id}/ - Update a specific comment
DELETE /comments/{id}/ - Delete a specific comment
Users

GET /users/ - List all users
GET /users/{id}/ - Retrieve a specific user
Models
Category: Represents categories for blog posts.
Tag: Represents tags for blog posts.
Post: Represents a blog post with a title, content, author, categories, and tags.
Comment: Represents a comment on a blog post.
Serializers
UserSerializer: Serializes user data.
CommentSerializer: Serializes comment data.
PostSerializer: Serializes post data, including categories and tags.
Viewsets
PostViewsets: Handles CRUD operations for posts.
CommentViewSet: Handles CRUD operations for comments.
UserViewSet: Handles CRUD operations for users.
URL Configuration
blog/urls.py: Configures URL routing for posts, comments, and users using DRF's DefaultRouter.
Dependencies
The project's dependencies are listed in requirements.txt:

makefile
Copy code
asgiref==3.8.1
backports.zoneinfo==0.2.1
Django==4.2.15
djangorestframework==3.15.2
sqlparse==0.5.1
typing-extensions==4.12.2
