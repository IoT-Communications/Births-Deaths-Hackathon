# **Births and Deaths Registration System**

This is an easy-to-use web application developed for managing the application, processing and issuing of birth or death certificates by the Department of Civil and National Registration.

---

## **Introduction**

Births and Deaths Registration System is accessible through a web browser such as:

* Google Chrome
* Safari 
* Mozilla Firefox
* Internet Explorer etc.

Applicants who visit the site can apply for or alter the names captured in a birth or death certificate. To use the system, capplicants must first ***sign up*** to create an account that will be used to track the status and progress of their applications.

The system is developed to send email and SMS notifications to appropriate individuals at every stage of the application process. This helps to ensure timely and efficient registration of births and deaths. 

---

## **Installation**

Births and Deaths Registration System is built on the [Frappe Framework](https://frappeframework.com/ "Frappe Site"), a full-stack, open source, web development framework written in Python & JavaScript. The framework is ***generic*** and can be used to build database driven apps. ***MariDB*** is the default database for the framework.

To install Births and Deaths Registration System, you will have to install [Frappe-Bench](https://frappeframework.com/docs/v13/user/en/installation "Frappe Bench Installation"), a command-line package and site manager for the Frappe Framework.

>For more details, read the Bench ***README***.

After installing Frappe Bench, you will have to initialise a bench directory with the Frappe Framework using the following command:

```bench
bench init births_deaths
```

Next, change the directory to ***births_deaths*** and download the Births and Deaths Registration app with the following command:

```bench
cd births_deaths

bench get-app births_and_deaths_registration https://github.com/IoT-Communications/Births-Deaths-Hackathon.git
```

Create a new site to install the app by running the command:

```bench
bench new-site births-deaths.example.com
```

This will create a new folder in your ***/sites*** directory and create a new database for this site.

Next, install the Births and Deaths Registration app in this site by running the command:

```bench
bench --site births-deaths.example.com install-app births_and_deaths_registration
```

To run the app locally, you must start the bench service with the command:

```bench
bench start
```

At this point, the Births and Deaths Registration app is installed and listening on port 8000. 

You can now fire up your browser by clicking [this link](http://localhost:8000/ "Login Screen") and you should see the login screen. 

Login as Administrator and use the password you set at the time of creating the site ***(births-deaths.example.com)***.

---

## **License**

MIT