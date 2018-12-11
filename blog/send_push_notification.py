import onesignal as onesignal_sdk

# For security you should load your app_api_key from enviroment variables
app_id = '877d417d-3142-49d6-9823-87ac29a97486'
app_api_key = 'ljksfhsdkjfhskjfhsfklasdfhslfskfjhslakfjsah'

# Load OneSignal SDK
onesignal_client = onesignal_sdk.Client(app={"app_auth_key": app_api_key, "app_id": app_id})

def send_push_notification(content,headings,url,player_ids):
    '''Send a push notification to one or multiple users
       content and headings must be dictionaries {"en": "Message",}
       url is a string
       players_id must be an array
    '''
    
    new_notification = onesignal_sdk.Notification(contents=content)
    new_notification.set_parameter("include_player_ids",player_ids)
    new_notification.set_parameter("headings", headings)
    new_notification.set_parameter("url", url)
    # send notification, it will return a response
    onesignal_response = onesignal_client.send_notification(new_notification)
    return onesignal_response

# Sample data 
content = {"en": "Julián, Your Python Developer vacancy has a new candidate. Click for details.", 
            "es": "Julián, tu vacante Python Developer tiene una nueva postulación, haz clic para ver."}
headings = {"en": "You have a new candidate.", 
            "es": "Tienes un nuevo candidato."}
player_ids = ['d8ebaaca-d443-4af3-8107-7cd3edeae917','61fd9d54-c432-482d-9010-eafb7b7acf16']
url = "https://test.myjobstudio.com/vacancy/myjobstudio/bla-bla-bla/56.html"

push = send_push_notification (content=content,headings=headings,url=url, player_ids=player_ids  )
print(push.status_code)
print(push.json())