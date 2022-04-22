import pyfirmata
board = pyfirmata.Arduino("COM3")

from flask import Flask, render_template, jsonify
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
    board.digital[13].write(1)
    led.write(1)
    return jsonify({'message':"led on",'data':True})

@app.route('/ledoff', methods= ['GET'])
def turnLedOff():
    board.digital[13].write(0)
    led.write(0)
    return jsonify({'message':"led off",'data':True})

@app.route('/buzzeron', methods=['GET'])  
def turnBuzzerOn():
    board.digital[13].write(1)
    buzzer.write(1)
    return jsonify({'message':"buzzer on",'data':True})

@app.route('/buzzeroff', methods= ['GET'])
def turnBuzzerOff():
    board.digital[13].write(0)
    buzzer.write(0)
    return jsonify({'message':"buzzer off",'data':True})

# main driver function
if __name__ == '__main__':
  
    # run() method of Flask class runs the application 
    # on the local development server.
    app.run(debug=False, host= '192.168.87.213')
    # app.run()