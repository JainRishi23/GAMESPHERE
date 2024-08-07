# Django Web Project: GAMESPHERE

![Project Logo](https://rishi2305.pythonanywhere.com/static/assets/img/logo.png)

## Overview

This Django web project includes four exciting casino games:

1. **Fortune Wheel**
2. **Roulette**
3. **Lucky Digits**
4. **Seven/Slot Machine Game**

Users can register and log in to play these games. Each user starts with 1000 predefined points, which are updated in real-time as they play the games.

## Features

- **User Registration and Login**: Users must register and log in to access the games.
- **Predefined Points**: Each user starts with 1000 points.
- **Real-Time Updates**: Points are updated in real-time after playing each game.
- **Attractive UI**: A modern, sleek, and inviting design for an enhanced user experience.

## Project Structure

```
/home/rishi2305/PYTHON-DJANGO-PROJECT/
    myProject/
        manage.py
        myProject/
            __init__.py
            settings.py
            urls.py
            wsgi.py
        myApp/
            __init__.py
            models.py
            views.py
            templates/
            static/
            ...
```

## Live Demo

Check out the live project [here](https://rishi2305.pythonanywhere.com/).

## Project Partners

- **Rishi Jain**
- **Rishabh Jain**

## Screenshots

![Registration Page](https://your-registration-page-image-link.com)
![Login Page](https://your-login-page-image-link.com)
![Fortune Wheel Game](https://your-fortune-wheel-image-link.com)
![Roulette Game](https://your-roulette-image-link.com)
![Lucky Digits Game](https://your-lucky-digits-image-link.com)
![Seven/Slot Machine Game](https://your-seven-slot-machine-image-link.com)

## Video Demo

[Watch the project demo](https://your-video-link-here.com)

## Installation and Setup

### Prerequisites

- Python 3.x
- Django 3.x
- Virtual Environment (recommended)

### Cloning the Repository

To clone the repository and set it up on [PythonAnywhere](https://www.pythonanywhere.com/), follow these steps:

1. **Clone the repository**:

    ```bash
    git clone https://github.com/your-username/your-repo-name.git
    cd your-repo-name
    ```

2. **Create a virtual environment and activate it**:

    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

3. **Install the required packages**:

    ```bash
    pip install -r requirements.txt
    ```

4. **Apply migrations**:

    ```bash
    python manage.py migrate
    ```

5. **Create a superuser**:

    ```bash
    python manage.py createsuperuser
    ```

6. **Run the development server**:

    ```bash
    python manage.py runserver
    ```

### Deploying on PythonAnywhere

1. **Sign up and log in to PythonAnywhere**.

2. **Create a new web app** and choose Django as the framework.

3. **Clone your repository** on PythonAnywhere:

    ```bash
    git clone https://github.com/your-username/your-repo-name.git
    ```

4. **Set up a virtual environment** on PythonAnywhere and install the requirements:

    ```bash
    mkvirtualenv --python=python3.8 my-virtualenv
    pip install -r /home/your-username/your-repo-name/requirements.txt
    ```

5. **Configure the WSGI file** to point to your Django application:

    ```python
    import os
    import sys

    path = '/home/your-username/your-repo-name'
    if path not in sys.path:
        sys.path.append(path)

    os.environ['DJANGO_SETTINGS_MODULE'] = 'myProject.settings'

    from django.core.wsgi import get_wsgi_application
    application = get_wsgi_application()
    ```

6. **Reload your web app** on PythonAnywhere to apply the changes.

## Requirements

Create a `requirements.txt` file with the necessary packages:

```txt
Django>=3.0,<4.0
djangorestframework
django-cors-headers
```

Install the requirements:

```bash
pip install -r requirements.txt
```

## Usage

1. **Register an account** on the registration page.
2. **Log in** with your credentials.
3. **Start playing** the games and enjoy!

## Contributing

Feel free to fork this repository, make changes, and submit pull requests. We welcome contributions from the community!

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact

For any questions or support, please reach out to:

- Rishi Jain: [rishijain2356@gmail.com](mailto:rishijain2356@gmail.com)
- Rishabh Jain: [rishabhjain@example.com](mailto:rishabhjain@example.com)
