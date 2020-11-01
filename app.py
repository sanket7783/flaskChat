from flask import Flask,request,Response
import requests
import sys
from datetime import datetime
from firebase_admin import firestore

key = "1313288692:AAG3k3FYeJIOCh7XgVkDmtDQ6v3yQM32t_0"
app = Flask(__name__)

db = firestore.Client()
doc_ref = db.collection(u'messages')

def firesave(msg):
    data={}
    data['createdAt']=firestore.SERVER_TIMESTAMP
    data['text']=msg
    doc_ref.add(data)

def sendmessage(chatid,msg):
    url = "https://api.telegram.org/bot{}/sendMessage".format(key)
    payload = {
        "text":msg,
        "chat_id":chatid
        }
    
    resp = requests.get(url,params=payload)
    return resp.ok

@app.route("/",methods=["POST","GET"])
def index():
    if(request.method == "POST"):       
        resp = request.get_json()
        msgtext = resp["message"]["text"]
        sendername = resp["message"]["from"]["first_name"]
        chatid = resp["message"]["chat"]["id"]
        global chatId
        chatId = chatid
        msg = resp["message"]["text"]
        firesave(msg)
        if msg=='/start':
            msg="Welcome!!!!!"
            sendmessage(chatid,msg)
        
    return Response('ok',status=200)


@app.route("/sendMessage",methods=['GET','POST'])
def sendMessage():
    try:
        print("****************************")
        print(request.values)
        sendmessage(881170538,request.values['data'])
    except Exception as e:
        Response(e,status=400)
    return Response('ok',status=200)

@app.route("/setwebhook/")
def setwebhook():
    url = "https://ngrok-url.ngrok.io/"
    s = requests.get("https://api.telegram.org/bot{}/setWebhook?url={}".format(key,url))
    if s:
        return "yes"
    else:
        return "fail"


if __name__ == "__main__":
    app.run(debug=True)