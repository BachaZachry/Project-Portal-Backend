# Project Portal Back-end
Project portal is an academic platform for teachers and students, allowing project submission, preview and attrubition. Done as a pluri-disciplinary project for college.

## Technologies
 - Python 3.7
 - Django Rest Framework
 - React
 - Ionic Framework
 - PostgreSQL
 - Styled-componants

## Setup
### Database Setup
````
- psql 
- CREATE DATABASE databasename;
- CREATE USER username WITH PASSWORD 'password';
- GRANT ALL PRIVILIGES ON DATABASE databasename TO username;
````
### Project Setup
````
 - pipenv install
 - Create .env file in projectPortal following .env.example
 - pipenv run python manage.py makemigrations
 - pipenv run python manage.py migrate
````
### Running The Back-end
``pipenv run python manage.py runserver``

## Documentation

Upon running the project,a proper documentation can be found at `` localhost:8000/docs/ ``

## Features
- Add,edit teachers and students (invite-only but for the sake of testing a register feature has been added)
- Project submission with file-upload
- Promotions management and project attribution
- Team and invite systems

## Links
- **[Demo](https://pluri-portal.web.app/)** 
- **[Front-end repository](https://github.com/Qalamar/pluri-portal)**
