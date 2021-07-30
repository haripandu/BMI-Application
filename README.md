# BMI Application
Calculator for Body Mass Index  

## Prerequisites  
Currently supported and tested on Linux and Windows environment.  
Also supported to run on Docker Container.  

Before use this application, please make sure you have been installed these prerequisites:
- python 3.7+. You also can create virtual environment first before running this application  
- Docker Container Runtime installed (If you want to run this application as container)

## What is implementing?
1. BMI Web Application which hosted on HEROKU.

2. CI/CD workflow is performing baseline scan and full scan from OWASP ZAPROXY. It used ZAPROXY Github repository when scanning.

3. Both baseline scan and full scan are triggered by push to BMI Application repository on Github.

4. Baseline scan is a script that runs the ZAP spider against the specified target for (by default) 1 minute and then waits for the passive scanning to complete before reporting the results. 
This means that the script doesn't perform any actual ‘attacks’ and will run for a relatively short period of time (a few minutes at most).

5. Full scan is a script that runs the ZAP spider against the specified target (by default with no time limit) followed by an optional ajax spider scan and then a full active scan before reporting the results.
This means that the script does perform actual ‘attacks’ and can potentially run for a long period of time.

6. Both baseline scan and full scan scripts are on ZAPROXY repository.

Baseline scan repository (https://github.com/zaproxy/action-baseline.git)

Full scan repository (https://github.com/zaproxy/action-full-scan.git)

7. When push a change to BMI-Application repository, owasp-scan.yml as a workflow triggered baseline and full scan. After scanning completed, Github will issued each report through Github Actions.
Report can be downloaded on email notification from github-actions[bot] or list reports on this [https://github.com/haripandu/BMI-Application/issues].

8. Please find below for sample reports which is issued by Github Action.
ZAP Full Scan Report : https://github.com/haripandu/BMI-Application/issues/10
ZAP Baseline Scan Report : https://github.com/haripandu/BMI-Application/issues/9

9. The downloaded report will informed what the vulnerability finding with risk level (High, Medium, Low & Informational).


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

        docker pull haripandu/BMI-Application  

2. Run container  

   Example: You can run this container on detached mode and run on default port 5000

        docker run -d -p 5000:5000 --name bmi-calculator haripandu/BMI-Application:latest  

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

### HEROKU Mock Up Lab  

If you are interesting to preview the feature for this app, please check heroku deployment on this link:  

Main application: [https://hpdm-bmi-app.herokuapp.com/](https://hpdm-bmi-app.herokuapp.com/)  
  
REST API: https://hpdm-bmi-app.herokuapp.com/  
Change height and weight for your input, example:  
[https://hpdm-bmi-app.herokuapp.com/api?height=167&weight=70]https://hpdm-bmi-app.herokuapp.com/api?height=167&weight=70)
