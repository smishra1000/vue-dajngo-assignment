# vue-dajngo-assignment



To start Front End

npm install

npm install bulma --save

npm install --save npm run vue-style-loader

npm install node-sass sass-loader

# serve with hot reload at localhost:8080
npm run dev

# build for production with minification
npm run build

Browse here

http://localhost:8080





**To Start backend**


 
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



http://127.0.0.1:8000/admin/


http://127.0.0.1:8000/api/   with GET   to see all participants list 

http://127.0.0.1:8000/api/   with POST   to Add as participant 

<img width="1440" alt="Screenshot 2020-09-08 at 3 23 51 PM" src="https://user-images.githubusercontent.com/10574792/92462156-b8e55c80-f1e7-11ea-9918-c9baa035f9be.png">

<img width="1439" alt="Screenshot 2020-09-08 at 3 24 03 PM" src="https://user-images.githubusercontent.com/10574792/92462193-c569b500-f1e7-11ea-968a-f8d9781cbb3c.png">

<img width="1440" alt="Screenshot 2020-09-08 at 3 24 35 PM" src="https://user-images.githubusercontent.com/10574792/92462271-e500dd80-f1e7-11ea-89ab-7d77cd3a4f0c.png">

<img width="1440" alt="Screenshot 2020-09-08 at 3 24 44 PM" src="https://user-images.githubusercontent.com/10574792/92462323-f4802680-f1e7-11ea-8924-b51e5556ec48.png">







