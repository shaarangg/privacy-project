import pyfirmata
board = pyfirmata.Arduino("COM3")
led = board.digital[5]
led.mode = pyfirmata.OUTPUT
while(True):
    inp = int(input("Enter input: "))
    led.write(inp)
    board.digital[13].write(inp)
