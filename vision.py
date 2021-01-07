import cv2
import winsound
from twilio.rest import Client
import datetime

account_sid = 'AC747a0fe8dddedcfa64a2b0dd62649969' 
auth_token = 'e9ab0fc55ade7b68beb69282a68f4586' 
client = Client(account_sid, auth_token)

oldtime = datetime.datetime.now()
newtime = datetime.datetime.now()

cam = cv2.VideoCapture(0)
while cam.isOpened():
    ret, frame1 = cam.read()
    ret, frame2 = cam.read()
    diff = cv2.absdiff(frame1, frame2)
    gray = cv2.cvtColor(diff, cv2.COLOR_RGB2GRAY)
    blur = cv2.GaussianBlur(gray, (5,5), 0)
    _, thresh = cv2.threshold(blur, 20, 255, cv2.THRESH_BINARY)
    dilated = cv2.dilate(thresh, None, iterations=3)
    contours, _ = cv2.findContours(dilated, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    
    
    # cv2.drawContours(frame1, contours, -1, (0, 255, 0), 2)
    for c in contours:
        if cv2.contourArea(c) < 5000:
            continue
        x, y, w, h = cv2.boundingRect(c)
        cv2.rectangle(frame1, (x,y), (x+w, y+h), (0, 255, 0), 2)
        newtime = datetime.datetime.now()
        time_diff = newtime - oldtime
        if(time_diff.seconds >= 15):
            message = client.messages.create(from_='whatsapp:+14155238886', body='Kindly see you room, Someone entered', to='whatsapp:+919466519919' )
            oldtime = datetime.datetime.now()
        #winsound.PlaySound('alert1.wav', winsound.SND_ASYNC)
    if cv2.waitKey(10) == ord('q'):
        cv2.destroyAllWindows()
        cam.release()
        break
    cv2.imshow('Security camera', frame1)
    