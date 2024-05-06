


# Django--Hospital-Management-System
<p>An online Hospital-Management-System developed in django-3 which allow users to contact  online with there hospital anytime :) </p>

### Short Note

This guide will Step-by-Step help you to create your own Hospital-Management-System application in django. React and Django Framework. 

Note: this guide is not for absolute beginners so im assuming that you have the basic knowledge of MVT in django to get started. To know more on it i recommend you <a href="https://docs.djangoproject.com/en/3.0/">django documentation</a>.

# Table of contents
- [About_this_App](#About_this_App)
- [hospitals_app](#hospitals_app)
  * [models](#models)
  * [migrations](#migrations)
  * [admin](#admin)
  * [server](#server)
  * [views](#views)
  * [urls](#urls)
  
<hr>

## About_this_App
Django Hospital Management System is a comprehensive application designed to efficiently manage hospital operations. It covers various aspects of hospital management, including patient and doctor records, appointments, prescriptions, receptionist tasks, HR functions, and more.


## hospitals_app

Lets begin our project by starting our project and installing a hospitals app, type below commands in terminal.

(django_project)$`django-admin startproject HospitalManagementSystem .` (do not avoid this period)

(django_project)$`python manage.py startapp hospitals`

Now, open your favourite IDE and locate this project directory. (Im using VS Code so it should be something like this) note that at this point django doesnt know about this app, therefore we need to mention this app name inside our settings.py file.

* settings.py 

open your ecom_project folder, in here you will find settings.py file (open it). Go to Installed app section and mention your app name there (as shown below).


	INSTALLED_APPS = [
	    'django.contrib.admin',
	    'django.contrib.auth',
	    'django.contrib.contenttypes',
	    'django.contrib.sessions',
	    'django.contrib.messages',
	    'django.contrib.staticfiles',

	    # my apps,				# changes
	    'hospitals',
	    ]


### models

When done with the settings.py file, open the course folder (our app), in here you we find models.py file (open it)
Now put the following code in it,


	from django.db import models

    class Doctor(models.Model):
        name = models.CharField(max_length=50)
        mobile = models.IntegerField()
        special = models.CharField(max_length=50)

        def __str__(self):
        return self.name;

    class Patient(models.Model):
        name = models.CharField(max_length=50)
        gender = models.CharField(max_length=10)
        mobile = models.IntegerField(null=True)
        address = models.CharField(max_length=50)

        def __str__(self):
        return self.name;

    class Appointment(models.Model):
        doctor = models.ForeignKey(Doctor,on_delete=models.CASCADE)
        patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
        date1 = models.DateField()
        time1 = models.TimeField()

        def __str__(self):
        return self.doctorname+"--"+self.patient.name;

    class Contact(models.Model):
        name = models.CharField(max_length=100, null=True)
        contact = models.CharField(max_length=15, null=True)
        email = models.CharField(max_length=50, null=True)
        subject = models.CharField(max_length=100, null=True)
        message = models.CharField(max_length=300, null=True)
        msgdate = models.DateField(null=True)
        isread = models.CharField(max_length=10,null=True)

        def __str__(self):
            return self.id

    

* what we done here ?

In  `models.py` file, we defined four Django models: `Doctor`, `Patient`, `Appointment`, and `Contact`. Let's go through each model and discuss what they represent:

1. `Doctor` model:
   - It has the following fields:
     - `name`: CharField with a maximum length of 50 characters, representing the name of the doctor.
     - `mobile`: IntegerField, representing the mobile number of the doctor.
     - `special`: CharField with a maximum length of 50 characters, representing the specialization of the doctor.
   - It has a `__str__` method that returns the name of the doctor as a string.

2. `Patient` model:
   - It has the following fields:
     - `name`: CharField with a maximum length of 50 characters, representing the name of the patient.
     - `gender`: CharField with a maximum length of 10 characters, representing the gender of the patient.
     - `mobile`: IntegerField (nullable), representing the mobile number of the patient.
     - `address`: CharField with a maximum length of 50 characters, representing the address of the patient.
   - It has a `__str__` method that returns the name of the patient as a string.

3. `Appointment` model:
   - It has the following fields:
     - `doctor`: ForeignKey to the `Doctor` model, using `on_delete=models.CASCADE` to ensure referential integrity.
     - `patient`: ForeignKey to the `Patient` model, using `on_delete=models.CASCADE` to ensure referential integrity.
     - `date1`: DateField, representing the date of the appointment.
     - `time1`: TimeField, representing the time of the appointment.
   - It has a `__str__` method that returns a string representation of the appointment, including the name of the doctor and the name of the patient.

4. `Contact` model:
   - It has the following fields:
     - `name`: CharField with a maximum length of 100 characters (nullable), representing the name of the contact.
     - `contact`: CharField with a maximum length of 15 characters (nullable), representing the contact information.
     - `email`: CharField with a maximum length of 50 characters (nullable), representing the email of the contact.
     - `subject`: CharField with a maximum length of 100 characters (nullable), representing the subject of the contact.
     - `message`: CharField with a maximum length of 300 characters (nullable), representing the message of the contact.
     - `msgdate`: DateField (nullable), representing the date of the contact message.
     - `isread`: CharField with a maximum length of 10 characters (nullable), representing the status of whether the message has been read.
   - It has a `__str__` method that returns the ID of the contact as a string.

These models define the structure and relationships between different entities in your Django application. They can be used to create database tables and perform operations on the data stored in those tables, such as creating, updating, and querying records.


## migrations 

now its time to create some tables in our database, most of which is already handled by django, we just need to run following commands:

(django_project)$`python manage.py makemigrations`

(django_project)$`python manage.py migrate`

Migrations for  `models.py`  involve the following steps:

1. Initial migration: When you first create the Django app and define the models, you need to generate an initial migration. This initial migration sets up the database tables for the models defined in `models.py`.

2. Creating tables for models: The initial migration creates the necessary database tables for the `Doctor`, `Patient`, `Appointment`, and `Contact` models. Each model corresponds to a separate table in the database.

3. Adding fields: If you add any new fields to the models or make modifications to existing fields, you will need to create a new migration to reflect those changes in the database schema. Django's migration system will generate the necessary migration files to add or alter the respective fields in the database tables.

4. Applying migrations: Once you have the migration files, you can apply the migrations to update the database schema. Django's migration system will execute the migration files, creating or modifying the database tables according to the changes made in `models.py`.

5. Handling relationships: In the case of the `Appointment` model, which has foreign key relationships with both the `Doctor` and `Patient` models, the migration system will create the appropriate foreign key constraints in the database tables. This ensures referential integrity between the tables.

6. Data migration (optional): If you need to migrate existing data when making changes to the models, you can write data migration scripts. These scripts allow you to manipulate the data in the database during the migration process.

By following these steps, Django's migration system helps you keep the database schema in sync with the changes made to the models defined in `models.py`. It provides a structured and controlled way to manage the evolution of your database schema over time.

### admin

now we need to register our models in admin file in order in to use them. Put the following code in admin.py file

	from django.contrib import admin
    from .models import Doctor, Patient, Appointment, Contact

    admin.site.register(Doctor)
    admin.site.register(Patient)
    admin.site.register(Appointment)
    admin.site.register(Contact)

Here, .models means from this current directory import the Doctor  and Patient ,Appointment ,Contact  model, from Models.py file and
for each model to register we need the command --> admin.site.register(model_name)

### server

Now, lets check that our model is being registered properly or not. First lets ensure that our server is running properly. Put the following commmand in terminal:

(django_project)$`python manage.py runserver`

* now open this link in your browser http://127.0.0.1:8000/

You will see a rocket there and a message saying, 'The install worked successfully! Congratulations!'

if yes, we didn't make any mistakes. Good !

* Now go to admin page by using this link http://127.0.0.1:8000/admin/


### views


	from rest_framework import viewsets
    from .serializers import DoctorSerializer, PatientSerializer, AppointmentSerializer, ContactSerializer
    from .models import Doctor, Patient, Appointment, Contact

    class DoctorViewSet(viewsets.ModelViewSet):
        queryset = Doctor.objects.all()
        serializer_class = DoctorSerializer

    class PatientViewSet(viewsets.ModelViewSet):
        queryset = Patient.objects.all()
        serializer_class = PatientSerializer

    class AppointmentViewSet(viewsets.ModelViewSet):
        queryset = Appointment.objects.all()
        serializer_class = AppointmentSerializer

    class ContactViewSet(viewsets.ModelViewSet):
        queryset = Contact.objects.all()
        serializer_class = ContactSerializer

In our  `views.py` file, the following actions are performed:

1. Importing necessary modules and classes:
   - `viewsets` from `rest_framework`: This module provides a set of base classes for creating API views.
   - `DoctorSerializer`, `PatientSerializer`, `AppointmentSerializer`, and `ContactSerializer`: These are serializer classes responsible for converting Django model instances into JSON representations and vice versa.
   - `Doctor`, `Patient`, `Appointment`, and `Contact`: These are the model classes defined in the application.

2. Defining viewsets:
   - `DoctorViewSet`, `PatientViewSet`, `AppointmentViewSet`, and `ContactViewSet`: These classes are subclasses of `viewsets.ModelViewSet`, which provides the implementation for CRUD (Create, Retrieve, Update, Delete) operations on the models.
   - Each viewset specifies the queryset, which is an object representing the collection of records to be queried, and the serializer class responsible for serializing and deserializing the model instances.

3. Configuring the viewsets:
   - The `queryset` attribute of each viewset is set to retrieve all objects from the corresponding model's table in the database. For example, `DoctorViewSet` retrieves all `Doctor` objects, `PatientViewSet` retrieves all `Patient` objects, and so on.
   - The `serializer_class` attribute of each viewset is set to the respective serializer class for that model. This determines how the model instances should be serialized and deserialized.

By defining these viewsets, the `views.py` file sets up the API views for performing CRUD operations on the `Doctor`, `Patient`, `Appointment`, and `Contact` models. The viewsets handle the logic for retrieving, creating, updating, and deleting instances of these models and use the specified serializers for data conversion.




### urls
we create urls.py file to confic our urls-endpoints 


	from django.urls import include, path
    from rest_framework import routers
    from .views import DoctorViewSet, PatientViewSet, AppointmentViewSet, ContactViewSet

    router = routers.DefaultRouter()
    router.register(r'doctors', DoctorViewSet)
    router.register(r'patients', PatientViewSet)
    router.register(r'appointments', AppointmentViewSet)
    router.register(r'contacts', ContactViewSet)

    urlpatterns = [
        path('', include(router.urls)),
    ]


* what we done here ? 

In the  `urls.py` file, the following actions are performed:

1. Importing necessary modules and classes:
   - `include` and `path` from `django.urls`: These are used to define URL patterns for the API endpoints.
   - `routers` from `rest_framework`: This module provides a simple way to automatically generate URLs for the API views.

2. Creating a router:
   - The `router` variable is an instance of `routers.DefaultRouter()`. This router class automatically generates the URL patterns for the API views based on the registered viewsets.

3. Registering viewsets with the router:
   - The `router.register()` method is used to register the viewsets with the router.
   - Each viewset is registered with a specific URL pattern and a corresponding prefix. For example, `DoctorViewSet` is registered with the URL pattern `doctors/`, `PatientViewSet` with `patients/`, `AppointmentViewSet` with `appointments/`, and `ContactViewSet` with `contacts/`.

4. Defining urlpatterns:
   - The `urlpatterns` list is created to define the URL patterns for the API endpoints.
   - The `path()` function is used to specify the root URL pattern ('/') and include the URLs generated by the router by using the `include()` function.
   - By including the router URLs, all the registered viewsets' URL patterns are automatically added to the root URL pattern.

By setting up the `urls.py` file in this way, the router automatically generates the URL patterns for the API endpoints based on the registered viewsets. These URL patterns map to the corresponding viewsets and handle the HTTP requests for CRUD operations on the `Doctor`, `Patient`, `Appointment`, and `Contact` models.


Before putting some code in this file go to HospitalManagementSystem folder and open urls.py file. Update this file in the follwing manner

	from django.contrib import admin
	from django.urls import path, include # changes

	urlpatterns = [
	    path('admin/', admin.site.urls),
	    path('', include('hospitals.urls')),  # changes
	]


 








































