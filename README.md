### Updated: Feb/17/23


# LoginOnFlask
Login using Flask

Here is demonstrated how to validate and login-in using the flask framework

## Road Map:

- Create and activate VENV  
(using Python 3.7 version)

- This next 3 steps are OPTIONAL, but HIGH recommended !!!
1) python -m pip install --upgrade pip
2) pip install -U setuptools
3) pip install wheel

- pip install -r requirements.txt  

(remove the comment from the "INSERT" method on route "Base URL/crud", to add more "users",
there are currently two users: "turco" and "teste"; both with the password "1234") 

(the route "Base URL/crud" makes de actions in background directly in database) 

- python run.py runserver<br>
(Make sure you have added a User)

## URL base: (verify on the aplication)
Access on your browser: http://localhost:5000

## Routes:
/<br>
(displays the simple message)<br><br>

/login<br>
(display the LOGIN page)<br><br>

/logout<br>
(does the LOGOUT of User)<br><br>

/crud<Br>
(route for CRUD methods, this methods are comented in the code)<br><br>

Example based on the "Curso de Flask" ministred by Julia Rizza 
on your channel of Youtube

