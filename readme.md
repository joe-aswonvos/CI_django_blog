# Codestar Blog

This project is a blog application developed as part of the Code Institute & Headforwards full stack development bootcamp. It serves as a learning exercise to understand and implement various technologies and best practices in web development using Django. The application allows users to create, edit, and delete blog posts, as well as comment on them. It also includes user authentication and other essential features for a modern web application.

## Contents

1. [Technologies Used](#technologies-used)
2. [Installation](#installation)
3. [Usage](#usage)
4. [Features](#features)
5. [Testing](#testing)
6. [Deployment](#deployment)
7. [Credits](#credits)

## Technologies Used

- **Django**: The main web framework used for developing the application.
- **SQLite**: The database used for development and testing.
- **Bootstrap**: For responsive design and styling.
- **jQuery**: For DOM manipulation and AJAX requests.
- **Cloudinary**: For managing media files.
- **Crispy Forms**: For better form handling and styling.
- **Django Allauth**: For user authentication and social account integration.
- **Django Summernote**: For rich text editing in the admin panel.

## Installation

1. Clone the repository:
   ```sh
   git clone https://github.com/yourusername/codestar_blog.git
   ```
2. Navigate to the project directory:
   ```sh
   cd codestar_blog
   ```
3. Install the required dependencies:
   ```sh
   pip install -r requirements.txt
   ```
4. Set up the database:
   ```sh
   python manage.py migrate
   ```
5. Create a superuser:
   ```sh
   python manage.py createsuperuser
   ```
6. Run the development server:
   ```sh
   python manage.py runserver
   ```

## Usage

- Access the application at [http://127.0.0.1:8000/](http://_vscodecontentref_/1).
- Log in as the superuser to access the admin panel at [http://127.0.0.1:8000/admin/](http://_vscodecontentref_/2).
- Create, edit, and delete blog posts from the admin panel.
- Comment on blog posts as a logged-in user.

## Features

- User authentication (login, logout, registration).
- Create, edit, and delete blog posts.
- Comment on blog posts.
- Responsive design using Bootstrap.
- Rich text editing with Django Summernote.
- Media file management with Cloudinary.

## Testing

- Run the tests using the following command:
  ```sh
  python manage.py test
  ```

## Deployment

- The application can be deployed to Heroku or any other cloud platform.
- Ensure to set the necessary environment variables and configurations for the production environment.

## Credits

- Developed as part of the Code Institute & Headforwards full stack development bootcamp.
- Special thanks to the instructors and mentors for their guidance and support.
