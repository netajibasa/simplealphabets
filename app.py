#!/usr/bin/env python

import urllib
import json
import os

from flask import Flask
from flask import request
from flask import make_response
from random import randrange
# Flask app should start in global layout
app = Flask(__name__)


@app.route('/webhook', methods=['POST'])
def webhook():
    req = request.get_json(silent=True, force=True)

    print("Request:")
    print(json.dumps(req, indent=4))

    res = processRequest(req)

    res = json.dumps(res, indent=4)
    # print(res)
    r = make_response(res)
    r.headers['Content-Type'] = 'application/json'
    return r


def processRequest(req):
    #if req.get("result").get("action") != "yahooWeatherForecast":
    #    return {}
    #baseurl = "https://query.yahooapis.com/v1/public/yql?"
    #yql_query = makeYqlQuery(req)
    #if yql_query is None:
    #    return {}
    #yql_url = baseurl + urllib.urlencode({'q': yql_query}) + "&format=json"
    #result = urllib.urlopen(yql_url).read()
    #data = json.loads(result)
    #res = makeWebhookResult(data)
    #return res
    #data = getAlphabet(req)
    list1 = ['Give one more alphabet', 'Say one more letter', 'What is your next alphabet', 'Ok give the next alphabet']
    
    random_number = randrange(4) # from 0 to 9 and 10 is not included
    rndString = list1[random_number]
    data = getAlphabet(req)
    print ("Netaji")
    print(data)
    return {
        "speech": data + " " +rndString,
        "displayText": "test",
        # "data": data,
        # "contextOut": [],
        "source": "mysource"
    }
	
	
def getAlphabet(req):
    result = req.get("result")
    parameters = result.get("parameters")
    alphabet = parameters.get("user-alphabet")
    lowerAlphabet = alphabet.upper()
    returnValue=""
    list2 = ['Next One is ','Next is ']
    random_number = randrange(2) # from 0 to 9 and 10 is not included
    rndString = list2[random_number]
    
    if lowerAlphabet == 'A':
        returnValue = 'B'
    elif lowerAlphabet == 'B':
        returnValue = 'C'
    elif lowerAlphabet == 'C':
        returnValue = 'D'
    elif lowerAlphabet == 'D':
        returnValue = 'E'
    elif lowerAlphabet == 'E':
        returnValue = 'F'
    elif lowerAlphabet == 'F':
        returnValue = 'G'
    elif lowerAlphabet == 'G':
        returnValue = 'H'
    elif lowerAlphabet == 'H':
        returnValue = 'I'
    elif lowerAlphabet == 'I':
        returnValue = 'J'
    elif lowerAlphabet == 'J':
        returnValue = 'K'
    elif lowerAlphabet == 'K':
        returnValue = 'L'
    elif lowerAlphabet == 'L':
        returnValue = 'M'
    elif lowerAlphabet == 'M':
        returnValue = 'N'
    elif lowerAlphabet == 'N':
        returnValue =  'O'
    elif lowerAlphabet == 'O':
        returnValue =  'P'
    elif lowerAlphabet == 'P':
        returnValue =  'Q'
    elif lowerAlphabet == 'Q':
        returnValue =  'R'
    elif lowerAlphabet == 'R':
        returnValue =  'S'
    elif lowerAlphabet == 'S':
        returnValue =  'T'
    elif lowerAlphabet == 'T':
        returnValue =  'U'
    elif lowerAlphabet == 'U':
        returnValue =  'V'
    elif lowerAlphabet == 'V':
        returnValue =  'W'
    elif lowerAlphabet == 'W':
        returnValue =  'X'
    elif lowerAlphabet == 'X':
        returnValue =  'Y'
    elif lowerAlphabet == 'Y':
        returnValue =  'Z'
    elif lowerAlphabet == 'Z':
        returnValue =  'you said the last one. Ok Ill Start C'
    else:
        returnValue = 'I did not understand. I am starting with B'

    if lowerAlphabet != 'Z':
       return rndString + ". " + returnValue
    else:
       return returnValue
    #return alphabet
	
	
def makeYqlQuery(req):
    result = req.get("result")
    parameters = result.get("parameters")
    city = parameters.get("geo-city")
    if city is None:
        return None

    return "select * from weather.forecast where woeid in (select woeid from geo.places(1) where text='" + city + "')"


def makeWebhookResult(data):
    query = data.get('query')
    if query is None:
        return {}

    result = query.get('results')
    if result is None:
        return {}

    channel = result.get('channel')
    if channel is None:
        return {}

    item = channel.get('item')
    location = channel.get('location')
    units = channel.get('units')
    if (location is None) or (item is None) or (units is None):
        return {}

    condition = item.get('condition')
    if condition is None:
        return {}

    # print(json.dumps(item, indent=4))

    speech = "Today in " + location.get('city') + ": " + condition.get('text') + \
             ", the temperature is " + condition.get('temp') + " " + units.get('temperature')

    print("Response:")
    print(speech)

    return {
        "speech": speech,
        "displayText": speech,
        # "data": data,
        # "contextOut": [],
        "source": "apiai-weather-webhook-sample"
    }


if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))

    print "Starting app on port %d" % port

    app.run(debug=False, port=port, host='0.0.0.0')
