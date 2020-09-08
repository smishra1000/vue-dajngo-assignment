# Details of Development

## Adding MySql db
Create db participant
with current credentials used in settings.py

## Installation

### 1. Creating virtual env
Create a folder name "Project"

Go into that Project folder
  
Installing virtualenv --- If not in server or system

`sudo apt install python3-venv`

Creating virtual env

`python3 -m venv participant`

Activating virtual env

`source participant/bin/activate`

if virtual env got activated than ur prompt change with prefix (participant)

### 2. Adding given code
Paste the All code here 

Your code now look like

`Project`
`     paticipant`
`     participant_site`

Go into participant_site

`cd participant_site`

Your prompt look like
`(participant) <home/user>/Project/participant_site>

Install all dependencies

`pip install -r requirements.txt`

Migrate all databases

`python3 manage.py migrate`

Running server
`python3 manage.py runserver 0.0.0.0:8000`

Admin Site will be available at 

http://localhost:8000/admin/

username: admin

password: admin123



//create super user python manage.py createsuperuser

//to view admin part


## Using API through frontend or postman
Basic Auth

demo1

Admindemo@123


ContentType : application/json
