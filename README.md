# Social Media App

Welcome to the Social Media App! This is a Django-based application designed to let users connect, follow each other, and share posts. The app comes with full authentication and authorization features.

## Features

- **User Authentication**: Securely register, log in, and log out.
- **Authorization**: Different user permissions to ensure secure access to various parts of the application.
- **Homepage**: View posts from users you follow.
- **User Profile Page**: Manage and view your personal information and posts.
- **More Profiles Page**: Browse through all user profiles, and follow or unfollow users.

## Installation

1. **Clone the repository**:
    ```sh
    git clone https://github.com/MohammedRaghib/Week-3-Project-Django.git
    cd Week-3-Project-Django
    ```

2. **Set up the virtual environment**:
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. **Install dependencies**:
    ```sh
    pip install -r requirements.txt
    ```

4. **Apply migrations**:
    ```sh
    python manage.py migrate
    ```

5. **Run the development server**:
    ```sh
    python manage.py runserver
    ```

## Usage

- **Homepage**: After logging in, the homepage displays posts from users you follow.
- **User Profile Page**: Accessible via the user menu, allows users to view and manage their profile and personal posts.
- **More Profiles Page**: Lists all user profiles, with options to follow or unfollow users from thier profile page
