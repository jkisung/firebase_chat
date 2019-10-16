from firebase import firebase

firebase= firebase.FirebaseApplication(
    "https://chatbot-fontend.firebaseapp.com/", authentication=None)

result= firebase.get('/users', None)
print(result)

authentication= firebase.authentication()

