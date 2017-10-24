#/usr/bin/python


from requests_toolbelt import MultipartEncoder
import requests
import config
from time import sleep

from ring_doorbell import Ring
myring = Ring(config.ringUSER, config.ringPASS)
print myring.doorbells

def checkDoorBell():
	doorbell = myring.doorbells[0]
	last = None
	var = 1
	while var == 1:
		current = doorbell.last_recording_id
		if current != last:
			print "New recording ID found, sending notification to Cisco Spark"
			last = current
			#print current #uncomment to help debug
			#print last
			downloadLastRecording()
			sendSpark()
			sleep(30)			
		else:
			#print "current equal to last"  #uncomment if needed
			#print current
			#print last
			sleep(30)

def downloadLastRecording():
	doorbell = myring.doorbells[0]
	doorbell.recording_download(
		doorbell.last_recording_id, filename='last_rec.mp4',override=True)


def sendSpark():
        print 'Forming up the Cisco Spark message with attachment'
        filepath    = 'last_rec.mp4'
        filetype    = 'video/mp4'
        roomId      = config.roomId
        token       = config.token
        url         = "https://api.ciscospark.com/v1/messages"


        my_fields={'roomId': roomId,
                'text': 'Hi, here is the latest video from you RING doorbell' ,
                'files': ('last_rec.mp4', open(filepath, 'rb'), filetype)
		}
        m = MultipartEncoder(fields=my_fields)
        r = requests.post(url, data=m,
                  headers={'Content-Type': m.content_type,
                           'Authorization': 'Bearer ' + token})

        #print r.json() #uncomment to see JSON response from Cisco Spark 
        print 'The latest video of someone ringing your doorbell has been send to your Cisco Spark room'


checkDoorBell()
