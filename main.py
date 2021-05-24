import pyrebase

firebase_config={
    'apiKey': "AIzaSyBFlqcoYQ07Xjpc3Bfbhuu799TYyhJI_V0",
    'authDomain': "esp32-autocom.firebaseapp.com",
    'databaseURL': "https://esp32-autocom-default-rtdb.firebaseio.com",
    'projectId': "esp32-autocom",
    'storageBucket': "esp32-autocom.appspot.com",
    'messagingSenderId': "37325631743",
    'appId': "1:37325631743:web:24e886b414e061e5141cca"
}

firebase=pyrebase.initialize_app(firebase_config)

# db=firebase.database()
auth=firebase.auth()
# storage=firebase.storage()

#Authentication
# Login
email=input('Entre com seu email.')
password=input('Entre com sua senha.')
try:
    auth.sign_in_with_email_and_password(email,password)
except:
    print('Falha na autenticação!')

