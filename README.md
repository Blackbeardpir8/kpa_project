
# KPA Form Submission Project (Django REST Framework)

This is a simple Django REST API project I made as part of an internship assignment. It is used to submit and retrieve railway form data like **Bogie Checksheet** and **Wheel Specifications**.

I used Django, Django REST Framework, and PostgreSQL to build and test this.

---

##  Features

- ✅ Submit **Bogie Checksheet** form (with nested sections)
- ✅ Submit and get **Wheel Specification** forms
- ✅ Basic validation and required fields
- ✅ Dropdown-type fields using `choices` in models
- ✅ PostgreSQL for database
- ✅ `.env` for environment configuration
- ✅ Fully tested using Postman

---

## 💻 Technologies Used

- Python 3.13
- Django 5.x
- Django REST Framework
- PostgreSQL
- python-decouple (for `.env`)
- Postman (for testing)
- drf-yasg (optional for Swagger)

---

##  Folder Structure

```
kpa_project-main/
├── .env.example
├── README.md
├── requirements.txt
├── manage.py
├── postman/
│   └── KPA_form data.postman_collection.json
├── forms/
│   ├── models.py
│   ├── views.py
│   ├── serializers.py
│   ├── urls.py
│   └── ...
├── kpa_api/
│   └── settings.py, urls.py, ...
```

---

## 🔧 How to Run Locally

### 1. Clone the Project

```bash
git clone <your-repo-or-folder>
cd kpa_project-main
```

### 2. Create Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate   # on Windows
```

### 3. Install Requirements

```bash
pip install -r requirements.txt
```

### 4. Setup `.env` File

Create a file named `.env` in the root and add:

```
DEBUG=True

DB_NAME=kpa_db
DB_USER=postgres
DB_PASSWORD=postgres
DB_HOST=localhost
DB_PORT=5432
```

Make sure PostgreSQL is installed and the database `kpa_db` is created.

---

### 5. Run Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 6. Start the Server

```bash
python manage.py runserver
```

Your API will be live at: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

---

## 📬 API Endpoints

### 🔹 1. Bogie Checksheet Form - POST

**POST** `/api/forms/bogie-checksheet`

```json
{
  "formNumber": "BOGIE-2025-001",
  "inspection_by": "user_id_456",
  "inspection_date": "2025-07-03",
  "bogieDetails": {
    "bogieNo": "BG1234",
    "makerYearBuilt": "RDSO/2018",
    "incomingDivAndDate": "NR / 2025-06-25",
    "deficitComponents": "None",
    "dateOfIOH": "2025-07-01"
  },
  "bogieChecksheet": {
    "bogieFrameCondition": "Good",
    "bolster": "Good",
    "bolsterSuspensionBracket": "Cracked",
    "lowerSpringSeat": "Good",
    "axleGuide": "Worn"
  },
  "bmbcChecksheet": {
    "cylinderBody": "WORN_OUT",
    "pistonTrunnion": "GOOD",
    "adjustingTube": "DAMAGED",
    "plungerSpring": "GOOD"
  }
}
```

---

### 🔹 2. Wheel Specifications Form - POST

**POST** `/api/forms/wheel-specifications`

```json
{
  "formNumber": "WHEEL-2025-001",
  "submittedBy": "user_id_123",
  "submittedDate": "2025-07-03",
  "fields": {
    "treadDiameterNew": "915 (900-1000)",
    "lastShopIssueSize": "837 (800-900)",
    "condemningDia": "825 (800-900)",
    "wheelGauge": "1600 (+2,-1)"
  }
}
```

---

### 🔹 3. Get Wheel Forms - GET

**GET** `/api/forms/wheel-specifications?formNumber=WHEEL-2025-001`

Returns filtered wheel specification records.

---

##  Postman Testing

I used Postman to test all APIs.  
You can import the collection from:

 `postman/KPA_form data.postman_collection.json`

Just open Postman → Import → select this file → run the requests.


---

— **Deepak Yadav**
