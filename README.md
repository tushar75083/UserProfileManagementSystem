# User Profile Management System
A simple User Profile Management System implemented using Django and Django REST Framework. This project provides basic CRUD (Create, Read, Update, Delete) operations for managing user profiles through a RESTful API.In this project also added <b>Basic Authentication</b> to secure the apis..

## Features
<b>CRUD Operations:</b> Create, retrieve, update, and delete user profiles using Django REST Framework.<br>
<b>Function-Based Views:</b> Uses function-based views to handle HTTP requests.<br>
<b>ModelSerializer:</b> Serializes the UserProfile model for converting model instances to and from JSON.<br>
<b>Basic Authentication:</b> Added Basic Authentication and Permission Classes to secure the APIs.<br>
<b>API View Decorators:</b> Uses @api_view decorators to define the supported HTTP methods for each endpoint.<br>
<b>JSON Response:</b> All responses are in JSON format, making it suitable for integration with frontend frameworks or mobile applications.<br>

## Technologies Used
<b>Django:</b>The web framework used for developing this project.<br>
<b>Django REST Framework (DRF):</b> Provides powerful tools to build RESTful APIs.<br>
<b>SQLite:</b> Default database for data storage.<br>
<b>Python 3.x:</b> The programming language used for the development.<br>

## Installation
Follow these steps to set up the project on your local machine:<br>
<b>1.Clone the Repository:</b> <br>
git clone https://github.com/tushar75083/UserProfileManagementSystem.git <br>

<b>2.Set Up a Virtual Environment:</b> <br>
python -m venv venv <br>

<b>3.Activate the Virtual Environment:</b> <br>
venv\Scripts\activate <br>

<b>4.Install Required Libraries:</b> <br>
pip install django djangorestframework pillow <br>

<b>5.Run Migrations:</b> <br>
python manage.py migrate <br>

<b>6.Start the Development Server:</b> <br>
python manage.py runserver <br>

<b>7.Access the API:</b> <br>
Open a browser or use a tool like Postman to interact with the endpoints at http://127.0.0.1:8000/. <br>


## Project Structure
<b>Models:</b> Defines the UserProfile model for storing user profile information. <br>
<b>Serializers:</b> Uses ModelSerializer to convert model instances into JSON format and validate input data. <br>
<b>Views:</b> Implements function-based views for handling CRUD operations with @api_view decorators to define allowed HTTP methods (GET, POST, PUT,PATCH, DELETE. <br>
<b>URLs:</b> Maps URL patterns to the corresponding view functions. <br>

## Endpoints

<b>GET </b>   :  /profiles/        ==>   Retrieve a list of all user profiles.  <br>
<b>POST  </b> : /profiles/         ==>   Create a new user profile.  <br>
<b>GET  </b>  :  /profiles/id/   ==>   Retrieve a specific user profile by ID.  <br>
<b>PUT </b>   : /profiles/id/    ==>   Update an existing user profile.  <br>
<b>PATCH </b>   : /profiles/id/    ==>   Partial update an existing user profile.  <br>
<b>DELETE</b>:  /profiles/id/   ==>   Delete a user profile.  <br>

## Dependencies
Below are the required Python packages used in this project:<br>

<b>Django - </b>The main web framework.<br>
<b>djangorestframework - </b>For building REST APIs.<br>
<b>pillow -</b> If the project involves handling image uploads.<br>

