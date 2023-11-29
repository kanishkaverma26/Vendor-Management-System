# Vendor-Management-System
The repository contains Vendor Management System will handle vendor profiles, track purchase orders, and calculate vendor performance metrics using Django web development framework in python language.

### Installation
**1. Create a Folder where you want to save the project**

**2. Create a Virtual Environment and Activate**

Install Virtual Environment First
```
$  pip install virtualenv
```

Create Virtual Environment

For Windows
```
$  python -m venv venv
```
For Mac
```
$  python3 -m venv venv
```
For Linux
```
$  virtualenv venv
```

Activate Virtual Environment

For Windows
```
$  source venv/scripts/activate
```
For Mac
```
$  source venv/bin/activate
```

For Linux
```
$  source bin/activate
```

**3. Clone this project**
```
$  git clone git@github.com:kanishkaverma26/Vendor-Management-System.gitt
```

**4. Install Requirements from 'requirements.txt'**
```python
$  pip3 install -r requirements.txt
```

**5. Run The Server**

Command for PC:
```python
$ python manage.py runserver
```

Command for Mac:
```python
$ python3 manage.py runserver
```

Command for Linux:
```python
$ python3 manage.py runserver
```

**6. Accessing the Application**
After running the server, you can access the following:

Admin Panel: Open your web browser and navigate to http://localhost:8000/admin/

Swagger Documentation: http://localhost:8000/swagger/

APIs for Vendor and Purchase Orders: http://localhost:8000/api/

**7. Login Credentials**

Create Super User

Command for PC:
```
$  python manage.py createsuperuser
```

Command for Mac:
```
$  python3 manage.py createsuperuser
```

Command for Linux:
```
$  python3 manage.py createsuperuser
```



Then Add Email and Password

**or Use Default Credentials**

*For SuperAdmin*
Email: kanishka@hashstudioz.com
Password: Hash@123
