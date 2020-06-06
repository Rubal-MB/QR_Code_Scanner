import cv2
from pyzbar.pyzbar import decode  #decode as we want to decode our code i.e qr code

capture = cv2.VideoCapture(0)  # 0 for default camer telling python to capture video

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

	key = cv2.waitKey(1) 		#wait for 1 mili second

	if key == 27:   	#27 foe escape button
		break