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
$  git clone https://github.com/kanishkaverma26/Vendor-Management-System.git
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

After successfully running the server, you can access different components of the Vendor Management System.

- **Admin Panel:**
  - URL: [http://localhost:8000/admin/](http://localhost:8000/admin/)
  - Use the superuser credentials created in step 6 to log in.

- **Swagger Documentation:**
  - URL: [http://localhost:8000/swagger/](http://localhost:8000/swagger/)
  - Explore the API endpoints and their documentation using Swagger.

- **API Endpoints:**
  - URL: [http://localhost:8000/api/](http://localhost:8000/api/)
  - The following endpoints are available:

    - **Authentication:**
      - Create a new authentication token (POST): [http://localhost:8000/api/token/](http://localhost:8000/api/token/)

    - **Vendors:**
      - List all vendors (GET): [http://localhost:8000/api/vendors/](http://localhost:8000/api/vendors/)
      - Retrieve a specific vendor (GET): [http://localhost:8000/api/vendors/{vendor_id}/](http://localhost:8000/api/vendors/{vendor_id}/)
      - Create a new vendor (POST): [http://localhost:8000/api/vendors/](http://localhost:8000/api/vendors/)
      - Update a vendor (PUT): [http://localhost:8000/api/vendors/{vendor_id}/](http://localhost:8000/api/vendors/{vendor_id}/)
      - Delete a vendor (DELETE): [http://localhost:8000/api/vendors/{vendor_id}/](http://localhost:8000/api/vendors/{vendor_id}/)
      - Retrieve a specific vendor performance (GET): [http://localhost:8000/api/vendors/{vendor_id}/performance/](http://localhost:8000/api/vendors/{vendor_id}/performance/)

    - **Purchase Orders:**
      - List all purchase orders (GET): [http://localhost:8000/api/purchase_orders/](http://localhost:8000/api/purchase_orders/)
      - Retrieve a specific purchase order (GET): [http://localhost:8000/api/purchase_orders/{order_id}/](http://localhost:8000/api/purchase_orders/{order_id}/)
      - Create a new purchase order (POST): [http://localhost:8000/api/purchase_orders/](http://localhost:8000/api/purchase_orders/)
      - Update a purchase order (PUT): [http://localhost:8000/api/purchase_orders/{order_id}/](http://localhost:8000/api/purchase_orders/{order_id}/)
      - Delete a purchase order (DELETE): [http://localhost:8000/api/purchase_orders/{order_id}/](http://localhost:8000/api/purchase_orders/{order_id}/)
      - Acknowledge a purchase order (POST): [http://localhost:8000/api/purchase_orders/{order_id}/acknowledge/](http://localhost:8000/api/purchase_orders/{order_id}/acknowledge/)

Feel free to explore and interact with the provided API endpoints using the above URLs. Use POST to create new entries, PUT to update existing ones, and the Authentication endpoints to manage authentication tokens.

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
