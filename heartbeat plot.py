import plotly.plotly as py
import plotly.graph_objs as go
import pyrebase
import time

config = {
        "apiKey":"AlzaSyBcPkjp50hVFQj3jL7NdCMul0Cw9jP5gkc",
        "authDomain":"hacktech-12dad.firebaseapp.com",
        "databaseURL":"https://hacktech-12dad.firebaseio.com",
        "storageBucket":"",
    }

fb = pyrebase.initialize_app(config)
db = fb.database()

data = db.child('snapshots').get()
data = data.each()

print(data)
y = [change.get('heartbeat').get('change') for change in data]

#print(y)
