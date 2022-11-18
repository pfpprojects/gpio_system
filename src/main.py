import RPi.GPIO as GPIO
import time
import socket

HOST = "0.0.0.0"
PORT = 5000

GPIO.setmode(GPIO.BOARD)
GPIO.setup(16, GPIO.OUT)
GPIO.output(16, GPIO.LOW)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as socket:
    try:
        socket.bind((HOST, PORT))
        socket.listen()
        # new code
        while True:
        # end new code
            conn, addr = socket.accept()
            print(f"1: accepted client event, client ip: {addr}")
            data = conn.recv(1024)
            if not data:
                print("no data...")
                conn.close()
            request = data.decode("utf-8")
            print(f"2: decoded request= {request}")
            if(request == "start"):
                for i in range(3):
                    GPIO.output(16, GPIO.HIGH)
                    time.sleep(1)
                    GPIO.output(16, GPIO.LOW)
                    time.sleep(1)
                conn.sendall(str.encode(f"your request was: {request}. DONE!"))
            else:
                print("Unknown Request Command!")
                conn.sendall(str.encode(f"your request was: {request}. is Unknown!"))
            print("3: response done")
            conn.close()
            print(f"4: Connection with client: {addr} closed")
    except Exception as e:
        print(e)

print("5: Server closed")