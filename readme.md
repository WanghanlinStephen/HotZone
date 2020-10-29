Quick Start
To get this project up and running locally on your computer:

Set up the Python development environment. We recommend using a Python virtual environment.
Assuming you have Python setup, run the following commands (if you're on Windows you may use py or py -3 instead of python to start Python):
pip3 install -r requirements.txt
python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py collectstatic
python3 manage.py test # Run the standard tests. These should all pass.
python3 manage.py createsuperuser # Create a superuser

Before running the project, you have to pip 'requests' like sudo pip install requests
Or you can reference to this websites for more information: https://stackoverflow.com/questions/17309288/importerror-no-module-named-requests

python3 manage.py runserver
Open a browser to http://127.0.0.1:8000/admin/ to open the admin site
Important tasks:
I have created three login account for test purpose

1:Superuser
Account: stephen
Password: Wsq809327698

2:Test for Staff
Account: Test_Staff
Password: Wsq809327698

3:Test for client
Account: Test_Client
Password: Wsq809327698
