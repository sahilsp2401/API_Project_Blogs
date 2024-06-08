# API_Project_Blog

API_Project_Blog is a Django REST Framework-based API for managing a blog. It allows users to read, create, update, and delete blog posts, with authentication ensuring that only authorized users can perform certain actions.

## Features

- **Read Blogs**: Users can browse and read existing blog posts.
- **User Authentication**: Registration and authentication system for users to access additional functionalities.
- **Create, Update, and Delete Blogs**: Authenticated users can create new blog posts and update or delete their own posts.
- **Pagination**: User read blogs on different pages 
- **Search Functionality**: Users can search for specific blog posts by title, content.

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/API_Project_Blog.git
   cd API_Project_Blog
2. Install dependencies: django,django rest frame_work,simple_jwt and other if required
3. Apply migrations
4. Create a superuser
5. Run the development server
6. Access the API : Open your web browser and go to http://127.0.0.1:8000/api/index/

## API Endpoints
Authentication: /api/account/login (POST)
Register: /api/account/register/ (POST)
List Blogs: /api/index/ (GET)
Create Blog: /api/index/blog/ (POST)
Update Blog: /api/index/blog/ (PATCH)
Delete Blog: /api/index/blog/ (DELETE)

## Contributing
Contributions are welcome! Please feel free to open issues or submit pull requests.

