import pyrebase
import time
import sensor_api
import os

period = 0.02
config = {
        "apiKey":"AlzaSyBcPkjp50hVFQj3jL7NdCMul0Cw9jP5gkc",
        "authDomain":"hacktech-12dad.firebaseapp.com",
        "databaseURL":"https://hacktech-12dad.firebaseio.com",
        "storageBucket":"",
    }

fb = pyrebase.initialize_app(config)
db = fb.database()

heart = sensor_api.HeartbeatSensor(0)
temp = sensor_api.TempSensor(1)
flex = sensor_api.FlexSensor(2)
acc = sensor_api.AccelSensor(0x1D)

seconds = 0

try:
    while True:
        data = {
            'accelerometer':{
                    'x':acc.getValueX(),
                    'y':acc.getValueX(),
                    'z':acc.getValueX(),
                    'theta':acc.getTheta(),
                    'psi':acc.getPsi(),
                    'orientation':acc.getOrientation()
                },
            'heartbeat':{
                    'change':heart.getChange(),
                    'bpm':0,
                },
            'flex':{
                    'intensity':flex.getIntensity(),
                },
            'temp':{
                    'C':temp.getCelcius(),
                    'F':temp.getFahrenheit(),
                }
            }
        if seconds > 0.02:
            db.child('live').update(data)
            db.child('snapshots').push(data)
            os.system('clear')
            print("-"*59)
            print(data['heartbeat']['change'])
            
            seconds = 0
        heart.update()
        seconds += period
        time.sleep(period)

except KeyboardInterrupt:
    pass
