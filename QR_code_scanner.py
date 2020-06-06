import cv2
from pyzbar.pyzbar import decode  

capture = cv2.VideoCapture(0) 

recieved_data = None
while True:
	_, frame = capture.read()	

	decoded_data = decode(frame)
	try:
		data = decoded_data[0][0]
		if data != recieved_data:
			print(data)
			recieved_data = data
	except:
		pass

	cv2.imshow('QR Code Scanner', frame)

	key = cv2.waitKey(1)  

	if key == 27:   
		break
