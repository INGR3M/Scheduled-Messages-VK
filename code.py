import vk_api
import datetime
import config

mytoken = config.token
session = vk_api.VkApi(token=mytoken)
vk = session.get_api()


def sendras(mes,u_id):
	vk.messages.send(user_id=u_id, message=mes,random_id=0)

count = 0

while True:
	
	timenow = datetime.datetime.now()
	if count == 1:
		if timenow.hour == 22 and timenow.minute == 40:
			count = 0

	if (timenow.hour == 22 and timenow.minute == 38 and count == 0) or (timenow.hour == 22 and timenow.minute == 43 and count == 0):#Send twice at 22 38 and 22 43, 22 40 resets counter
		sendras("Some text","524155319") 
		count += 1
	