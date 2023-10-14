#Notebook api 

instructions on how to run the project locally

clone the repo: git clone https://github.com/MariamNsubuga/TungaProject.git

#create a virtual environment

sudo apt install python3-venv

#activate the virtual environment

source venv env/bin/activate

**cd notebook 

pip install requirement.txt

python3 manage.py runserver

The users folder is for handling authentication and authorisation while the notebook folder is for api app.

filter.py handles filter, search and ordering

serializer.py for creating serializer what i want to be accessed in the api

email.py is for sharing notes via email

on deploying the project locally in settings EMAIL_HOST_PASSWORD = 'yourpassword' this can be generating using your gmail account -> account settings -> security -> at the bottom of that page look for addpasswords.


NB: virtual environment creation is based on linux OS and mac for  windows follow this link https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/