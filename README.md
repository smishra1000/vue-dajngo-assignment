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

<img width="1440" alt="Screenshot 2020-09-08 at 2 54 10 PM" src="https://user-images.githubusercontent.com/10574792/92458618-470b1400-f1e3-11ea-8ff2-9ddd7de5ec30.png">

<img width="1440" alt="Screenshot 2020-09-08 at 3 00 53 PM" src="https://user-images.githubusercontent.com/10574792/92459273-1aa3c780-f1e4-11ea-8f08-fe7c76fb8250.png">


<img width="1440" alt="Screenshot 2020-09-08 at 12 21 52 PM" src="https://user-images.githubusercontent.com/10574792/92458798-83d70b00-f1e3-11ea-828c-94002db42c86.png">


<img width="1440" alt="Screenshot 2020-09-08 at 12 21 36 PM" src="https://user-images.githubusercontent.com/10574792/92458854-94878100-f1e3-11ea-8959-dec98fd32a91.png">






