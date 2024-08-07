Sure, here's the updated README file with a smaller logo image:

---

# Django Web Project: Casino Games

<img src="https://rishi2305.pythonanywhere.com/static/assets/img/logo.png" alt="Project Logo" width="200"/>

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

![Registration Page](img/registration-page.png)
![Login Page](img/login-page.png)
![Fortune Wheel Game](img/fortune-wheel.png)
![Roulette Game](img/roulette.png)
![Lucky Digits Game](img/lucky-digits.png)
![Seven/Slot Machine Game](img/slot-machine.png)

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

Here's the complete README file with the smaller logo and detailed instructions:

---

# Django Web Project: Casino Games

<img src="img/project-logo.png" alt="Project Logo" width="200"/>

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

![Registration Page](img/registration-page.png)
![Login Page](img/login-page.png)
![Fortune Wheel Game](img/fortune-wheel.png)
![Roulette Game](img/roulette.png)
![Lucky Digits Game](img/lucky-digits.png)
![Seven/Slot Machine Game](img/slot-machine.png)

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

3. **Install the required dependencies**:

    ```bash
    pip install -r requirements.txt
    ```

4. **Apply migrations**:

    ```bash
    python manage.py migrate
    ```

5. **Run the development server**:

    ```bash
    python manage.py runserver
    ```

Now you can access the project at `http://127.0.0.1:8000/`.

### Deploying on PythonAnywhere

1. **Sign up or log in to PythonAnywhere**.
2. **Create a new web app**:
    - Choose **Manual configuration** for Django.
    - Choose the Python version that matches your virtual environment.

3. **Upload your project files** to PythonAnywhere.

4. **Set up your virtual environment** on PythonAnywhere:
    - Go to the **Virtualenv** tab and enter the path to your virtual environment.

5. **Configure the WSGI file**:
    - Edit the WSGI configuration file to point to your project's settings.

6. **Apply migrations** and **collect static files**:

    ```bash
    python manage.py migrate
    python manage.py collectstatic
    ```

7. **Reload your web app** on PythonAnywhere to see the changes.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

This README file provides a comprehensive guide for setting up and deploying the Django web project with the included casino games. Make sure to replace placeholder URLs and paths with actual ones specific to your project.
