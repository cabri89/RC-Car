from flask import Flask,render_template, Response;
from flask import send_file
from camera import VideoCamera
import RPi.GPIO as GPIO
import cv2
app = Flask(__name__);

Motor1A = 37
Motor1B = 40
Motor1E = 35
motor1 = [Motor1A, Motor1B, Motor1E]

Motor2A = 36
Motor2B = 38
Motor2E = 33

motor2 = [Motor2A, Motor2B, Motor2E]

GPIO.setmode(GPIO.BOARD)

# Initialise les pin en out des moteurs
for pin in motor1 + motor2:
    GPIO.setup(pin,GPIO.OUT)

GPIO.PWM(Motor1E,50).start(100)   ## pwm de la pin 22 a une frequence de 50 Hz
GPIO.PWM(Motor2E,50).start(100)   ## pwm de la pin 22 a une frequence de 50 Hz

def move(engine,direction):
    if direction == 0:
        GPIO.output(engine[0],GPIO.LOW)
        GPIO.output(engine[1],GPIO.HIGH)
    else:
        GPIO.output(engine[1],GPIO.LOW)
        GPIO.output(engine[0],GPIO.HIGH)

    GPIO.output(engine[2],GPIO.HIGH)
    GPIO.output(Motor1E,GPIO.LOW)
    GPIO.output(Motor2E,GPIO.LOW)

def active(engine,direction):
    if direction == 0:
        GPIO.output(engine[0],GPIO.LOW)
        GPIO.output(engine[1],GPIO.HIGH)
    else:
        GPIO.output(engine[1],GPIO.LOW)
        GPIO.output(engine[0],GPIO.HIGH)
    GPIO.output(engine[2],GPIO.HIGH)

def stop():
    GPIO.output(Motor1E,GPIO.LOW)
    GPIO.output(Motor2E,GPIO.LOW)

# GPIO.cleanup()

@app.route("/")
def index():
    return render_template("index.html")

def gen(camera):
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

@app.route('/video_feed')
def video_feed():
    return Response(gen(VideoCamera()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')
@app.route('/move/<direction>')
def move_car(direction):
    direction = int(direction)
    if direction == 0:
        active(motor1,0)
        active(motor2,0)
    elif direction == 1:
        active(motor1,1)
        active(motor2,1)
    elif direction == 2:
        active(motor1,1)
        active(motor2,0)
    elif direction == 3:
        active(motor1,0)
        active(motor2,1)

    # show the user profile for that user
    return 'direction %s' % direction

@app.route('/stop/')
def stop_car():
    stop()

    # show the user profile for that user
    return 'Car stop'


if __name__ == "__main__":
    app.run(host='0.0.0.0',port='5500',debug=True)
