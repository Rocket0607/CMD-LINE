import numpy as np
import cv2
import base64 

cap = cv2.VideoCapture(0)

while True:

    ret, frame = cap.read()

    cv2.imshow('frame', frame)

    ret, jpeg = cv2.imencode(".jpg", frame)

    str_bytes = []
    bytes = frame.tobytes()
    str_byte = base64.b64encode(bytes)
    str_bytes.append(str_byte)

    if cv2.waitKey(10) & 0xFF == ord('q'):
        break

cap.release()
with open("bytes.txt", "wb") as bytes_file:
    for byte in str_bytes:
        bytes_file.write(byte)
    