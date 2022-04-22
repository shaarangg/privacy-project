import pyfirmata

board = pyfirmata.Arduino("COM3")

from flask import Flask, render_template, jsonify
from flask import request
import jwt
led = board.digital[5]
buzzer  = board.digital[3]
led.mode = pyfirmata.OUTPUT
buzzer.mode = pyfirmata.OUTPUT

app = Flask(__name__)
  
@app.route('/')
def home():

    return render_template('home.html')

@app.route('/ledon', methods=['GET'])  
def turnLedOn():
    token = request.args.get('token')
    try:
        resp = jwt.decode(token, "Privacy and security project", algorithm="HS256")
        if not str(resp["Name"])=="Shivansh":
            return jsonify({"error": "Not authenticated"})
    except:
        return jsonify({"error": "Not authenticated"})
    led.write(1)
    return jsonify({'message':"led on",'data':True})

@app.route('/ledoff', methods= ['GET'])
def turnLedOff():
    token = request.args.get('token')
    try:
        resp = jwt.decode(token, "Privacy and security project", algorithm="HS256")
        if not str(resp["Name"])=="Shivansh":
            return jsonify({"error": "Not authenticated"})
    except:
        return jsonify({"error": "Not authenticated"})
    led.write(0)
    return jsonify({'message':"led off",'data':True})

@app.route('/buzzeron', methods=['GET'])  
def turnBuzzerOn():
    token = request.args.get('token')
    try:
        resp = jwt.decode(token, "Privacy and security project", algorithm="HS256")
        if not str(resp["Name"])=="Shivansh":
            return jsonify({"error": "Not authenticated"})
    except:
        return jsonify({"error": "Not authenticated"})
    buzzer.write(1)
    return jsonify({'message':"buzzer on",'data':True})

@app.route('/buzzeroff', methods= ['GET'])
def turnBuzzerOff():
    token = request.args.get('token')
    try:
        resp = jwt.decode(token, "Privacy and security project", algorithm="HS256")
        if not str(resp["Name"])=="Shivansh":
            return jsonify({"error": "Not authenticated"})
    except:
        return jsonify({"error": "Not authenticated"})
    buzzer.write(0)
    return jsonify({'message':"buzzer off",'data':True})

# main driver function
if __name__ == '__main__':
  
    # run() method of Flask class runs the application 
    # on the local development server.
    app.run(debug=False, host= '192.168.87.213')
    # app.run()