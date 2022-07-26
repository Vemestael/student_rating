# student_rating

## About

Site to display the rating of students at the university

## Installation and using

This project provides you a working Django environment without requiring you to install Python/Django, a web server, and any other server software on your local machine. For this, it requires Docker and Docker Compose.

1. Install [Docker](https://docs.docker.com/engine/installation/) and [Docker-compose](https://docs.docker.com/compose/install/);

2. Clone this project and then cd to the project folder;

3. Create your own .env file by copying .env.example:
    ```sh
    $ cp src/.env.example src/.env
    ```

4. Update the environment variables in the docker-compose.yml and .env files.

5. Build the images and run the containers:
     ```sh
    $ docker-compose -f docker-compose.yml up -d --build
    ```
   
6. Run database migrations:
    ```sh
    $ docker-compose run django python manage.py migrate
    ```
   
7. You've done! Main page is available on http://localhost, phpMyAdmin - http://localhost:3309

8. After finishing work, you can stop running containers:
    ```sh
    $ docker-compose down
    ```