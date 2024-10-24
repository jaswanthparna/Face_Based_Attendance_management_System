import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(
    cred,
    {
        "databaseURL": "https://face-recognition-a4601-default-rtdb.firebaseio.com/",
        # database URL
    },
)

ref = db.reference(
    "Students"
)  # reference path to our database... will create student directory in the database

data = {
    "005432": {  # id of student which is a key
        "id": "005432",
        "name": "Jaswanth",
        "password": "Pjaswanth022@",
        "dob": "2003-02-27",
        "address": "Banglore, RRNagar",
        "phone": "7993747604",
        "email": "parnajaswanth@gmail.com",
        "major": "Data Science",
        "starting_year": 2022,
        "standing": "G",
        "total_attendance": 4,
        "year": 4,
        "last_attendance_time": "2024-02-21 12:33:10",
        "content": "This section aims to offer essential guidance for students to successfully complete the course. It will be regularly updated \
                to ensure its relevance and usefulness. Stay tuned for valuable \
                insights and tips that will help you excel in your studies.",
    },
}


for key, value in data.items():
    ref.child(key).set(value)
