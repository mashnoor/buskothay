
import json
import flask
from flask import Flask
from flask import request
from search import get_path
app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    print("Etering Webhook")
    req = request.get_json(silent=True, force=True)
    from_place = req['result']['parameters']['from']
    to_place = req['result']['parameters']['to']
    
    
    result = "Your shortest route is: " + str(get_path(from_place, to_place)[::-1]) + "\r\n\r\n"

    if from_place == "Gabtoli" and to_place == "Kalshi":
       
        result+= "Your can 'Achim' bus from Gabtoli"
    else:
        result+= "Sorry, can't find in bus database :("


    return generate_response(result)


def generate_response(text):
    r = {
        "speech":text,
        "displayText":"http://www.quanfield.com",
        "source":"facebook",

    }
    r = json.dumps(r, indent=4)
    res = flask.make_response(r)
    res.headers['Content-Type'] = 'application/json'
    return res

if __name__ == '__main__':
    port = 5002

    print("Starting app on port %d" % port)

    app.run(port=port)
    #app.run(host='0.0.0.0', port=port)