from flask import Flask,send_from_directory
app = Flask(__name__)
app.secret_key = 'test'
import json

@app.route('/')
def home():
   return "Proxy is up!"

@app.route('/proxy/', methods=['GET'])
def result():
    f =  open('proxy.json')
    file = json.load(f)
    proxy = ""
    for i in file["data"]:        
        proxy = proxy + str(i) + "<br>"
        
    print(proxy)
    html = """<pre style="">"""+proxy+""" </pre>"""


    return html#send_from_directory('','proxy.json')

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0',port=8080,use_reloader=True)
