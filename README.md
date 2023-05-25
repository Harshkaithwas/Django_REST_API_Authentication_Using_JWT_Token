
# Django_REST_API_Authentication_Using_JWT_Token

This is a Authentication app bases djnago rest framework uses jwt (json web tokens),

For using this project:
    
1. Copy this code to your project and use it there.
        
        Run this code and use jwt Authentication

2. Download this code to your machine.

Here you need to setup the databse settings in settings.py file for using this code, I used mysql and you can use database of your own choice.

    
    
    Before setting up the database use mysql to setup your database nad use those cradencials here in settings.py file.
        DATABASES = {
    'default': {
                    'ENGINE': 'django.db.backends.mysql',
                    'NAME': 'main',
                    'HOST': 'localhost',
                    'PORT': '3306',
                    'USER': 'root',
                    'PASSWORD': '261121',
                }
            }   

After cloning this project into your local machine, make a virtual environment inside the main directory of any name and put that file's name(path) in .gitignore(so that it won't show it in github repo) and then install all the modules of requirements.txt by command:

        pip install -r requirements.txt

3.  Make Migration by using command:

            python manage.py makemigrations

4.  Migrate by using command:

            python manage.py migrate

5.  Create super user by using command:

        python manage.py createsuperuser

6.  Use the urls/Api's in your browser or postman to test and you are ready to use them within your project.

    GoTo:

    1. For sign_up

            http://127.0.0.1:8000/accounts/sign_up/ 

    2. For sign_in

            http://127.0.0.1:8000/accounts/sign_in/



