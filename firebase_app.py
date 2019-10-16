# firebase python 연동

import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from firebase_admin import auth

db_api= ''

# Firebase database 인증 및 앱 초기화
cred = credentials.Certificate(
    'D:/firebase_chat/chatbot-fontend-firebase-ad0minsdk-dsfmx-8302ba1fe.json')
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://chatbot-fontend.firebaseio.com/',
    'databaseAuthVariableOverride': {
        'uid': 'my-service-worker'
    }
})
# As an admin, the app has access to read and write all data,
# regradless of Security Rules
ref = db.reference('')
print(ref.get())


print(app.name)
