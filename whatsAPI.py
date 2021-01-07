# import pywhatkit
# pywhatkit.sendwhatmsg('+919466519919', 'Hello this is whatsAPI', 0, 45)

from twilio.rest import Client 
 
account_sid = 'AC747a0fe8dddedcfa64a2b0dd62649969' 
auth_token = 'e9ab0fc55ade7b68beb69282a68f4586' 
client = Client(account_sid, auth_token) 
 
message = client.messages.create( 
                              from_='whatsapp:+14155238886',  
                              body='Your appointment is coming up on July 21 at 3PM',      
                              to='whatsapp:+919466519919' 
                          ) 
 
print(message.sid)