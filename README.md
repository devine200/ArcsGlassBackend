## ARCS & GLASS REAL ESTATE MANAGEMENT 
This portfolio website was developed for ARCs & Glass, a real estate management company based in Lagos, Nigeria. The site showcases the client’s projects and properties, with a custom content management system built using Django's admin panel. This setup enables the client to update website content independently after project completion. We created intuitive database models tailored to the website's structure, ensuring ease of use for non-developers on the admin dashboard. 

Arcs and Glass Ltd was founded in 2019, by Mr. Imran Claud-Ennin and Mrs. Olamide Claud-Ennin. Since the inception, the company has embarked on a mission to redefine the African real estate market through its projects, leveraging on the theme of Simplicity, Functionality and Sophistication.

### TECHNOLOGY STACK
This code base was written mainly using HTML, CSS and JavaScript and some accompanying libraries for website widget and styling.

The Backend of this project was built using the Python Django framework

### PROJECT SETUP

#### CLONE REPO
```bash
git clone https://github.com/devine200/ArcsGlass.git
```

#### SETUP VIRTUAL ENVIRONMENT
```bash
pip install virtualenv && virtualenv env && source env/bin/activate
```

#### INSTALL PROJECT DEPENDENCIES
```bash
pip install -r requirements.txt
```

#### MIGRATE PROJECT DATABASE
```bash
python manage.py makemigrations && python manage.py migrate
```

#### START UP PROJECT SERVER
```bash
python manage.py runserver
```
The above command spawns a project server at [http://localhost:8000](http://localhost:8000)

This project can currently be found live [here](https://arcsnglass.com)