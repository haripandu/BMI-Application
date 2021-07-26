# lanandra BMI Calculator
Calculator for Body Mass Index  

## Prerequisites  
Currently supported and tested on Linux and Windows environment.  
Also supported to run on Docker Container.  

Before use this application, please make sure you have been installed these prerequisites:
- python 3.7+. You also can create virtual environment first before running this application  
- Docker Container Runtime installed (If you want to run this application as container)

## How to Use  

### Local file  
1. Clone this repository to your local  
2. Install requirements  

    On Linux:  

        python3 -r requirements.txt  

    On Windows:  

        python -r requirements.txt  

3. For development, run main.py. This command will execute and run application as development web server  

    On Linux:  

        python3 main.py  
    
    On Windows:  

        python main.py  

4. For production web server, execute this command:  

    On Linux:
    
        gunicorn -b 0.0.0.0:5000 wsgi:app  

    On Windows:  

        waitress-serve --listen=0.0.0.0:5000 wsgi:app  

5. From your web browser access the application. Default port is 5000.  

    Example: localhost:5000  

### Run on Docker container  

1. Pull image from Docker Hub  

        docker pull lanandra/bmi-calculator  

2. Run container  

   Example: You can run this container on detached mode and run on default port 5000

        docker run -d -p 5000:5000 --name bmi-calculator lanandra/bmi-calculator:latest  

3. From your web browser access the application. Default port is 5000.  

    Example: localhost:5000 

### For CLI Junkie  

1. You can run bmi.py to run application on Command Line Interface  

    On Linux  

        python3 bmi.py  

    On Windows  

        python bmi.py

### REST API  

If you need REST API service from this application, you can use this method:  

1. Before passing directly from browser, you can test using application such as Postman  

2. Pass height and weight arguments use POST method. URL for api is  

        http://localhost:5000/api  

3. Example of usage

        http://localhost:5000/api?height=167&weight=70  

4. Example of output  

        {
        "bmi": 25.1,
        "label": "Overweight"
        }  

### heroku mock up lab  

If you are interesting to preview the feature for this app, please check heroku deployment on this link:  

Main application: [https://lanandra-bmi-calculator.herokuapp.com/](https://lanandra-bmi-calculator.herokuapp.com/)  
  
REST API: https://lanandra-bmi-calculator.herokuapp.com/api?height=float&weight=float  
Change height and weight for your input, example:  
[https://lanandra-bmi-calculator.herokuapp.com/api?height=167&weight=70](https://lanandra-bmi-calculator.herokuapp.com/api?height=167&weight=70)