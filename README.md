# Angelica's web store

This project is a web store CRUD RESTful API built with Python.

## Motivation

Working on this project helped me learn a more effective way to design and test my API endpoints as well as using the Flask-Restful extension.

It was fun to take the time to learn about

Test-first API design with Postman
Lambda functions
Writing SQL scripts in Python
Manging environments in Postman

All APIs I have built before, I have used routes to define endpoints. Thinking of endpoints as resources and treating them as objects with properties and methods has provided me with a new way of thinking about API design, and coming from an OOD perspective, this feels a very natural way of thinking when designing this kind software.

This project was also interesting for me because it transitioned from using SQL to access Resources to using SQLAlchemy database Models. While I have worked a lot with SQLAlchemy before, it was nice to go back to SQL which I had not touched since Makers and see the operations transition to the SQLAlcheny queries I am more familiar with these days.

## Built with

- Flask
- JWT
- Postman
- PostgreSQL
- Heroku

## Features

- User authentication
- CRUD operations
- WIP

## Set up and run API

**Create a virtual environment**

`<python3 -m venv env>`

**Activate your virtual environment**

`<source env/bin/activate>`

**Install the required dependencies**

`<pip3 install -r requirements.txt>`

**To run the API**

`<ptyhon app.py>`

## How to use

This API is live on [Angelica's Web Sotore][1] 🎢

[1]: https://stores-rest-api-a1.herokuapp.com/ "Angelica's Web Sotore"

However, being an API, you will get a 404 message. You can still try it out on [Postman][2].

[2]: https://www.postman.com/ "Postman"

Credits

To build this API, I used this tutorial by Jose Salvatierra - [REST APIs with Flask and Python][3]

[3]: https://www.udemy.com/course/rest-api-flask-and-python/ "REST APIs with Flask and Python"

This tutorial is excellent and demystified a lot of questions I had about Python, even if I had been coding in Python for a while, he took the time to explain concepts such as argument unpacking and Python decorators. I highly recommend his course.

This tutorial by Miguel Grinberg was also handy when thinking about design first - [Building Web APIs][4]
It also covers decorators and lessons around designing APIs and scaling them.

[4]: https://learning.oreilly.com/videos/building-web-apis/

This blogpost was very useful when setting up Postman environments. It saves a lot of typing and copy-pasting
https://dev.to/loopdelicious/using-jwt-to-authenticate-and-authorize-requests-in-postman-3a5h
