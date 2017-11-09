import serial
ser_addr = '/dev/ttyUSB0'

def unlock():
    with serial.Serial('/dev/ttyS1', 19200, timeout=1) as ser:
        ser.write(b'1')
