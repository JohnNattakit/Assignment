from flask import Flask, abort, request 
import json

app = Flask(__name__)

@app.errorhandler(404)
def page_not_found(e):
    return '''These API allow only POST method, Please use HTTP POST methods follows APIs
  /api/firstfactorial
  /api/rirstreverse
  /api/alphabetsoup

  Sample request
  ```
      POST /api/firstfactorial HTTP/1.1
      Host: 172.16.10.100:5000
      User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0
      Content-Type: application/json
      Accept-Language: en-US,en;q=0.5
      Accept-Encoding: gzip, deflate
      Connection: close
      Upgrade-Insecure-Requests: 1
      Content-Length: 13

      {"input": 9}
  ```'''

@app.route('/')
def index():
  return '''These API allow only POST method, Please use HTTP POST methods follows APIs
  /api/firstfactorial
  /api/rirstreverse
  /api/alphabetsoup

  Sample request
  ```
      POST /api/firstfactorial HTTP/1.1
      Host: 172.16.10.100:5000
      User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0
      Content-Type: application/json
      Accept-Language: en-US,en;q=0.5
      Accept-Encoding: gzip, deflate
      Connection: close
      Upgrade-Insecure-Requests: 1
      Content-Length: 13

      {"input": 9}
  ```'''

@app.route('/api/firstfactorial', methods=['POST']) 
def FN_A1():
    if not request.json:
        abort(400)
    json_string = json.dumps(request.json)
    datastore = json.loads(json_string)
    number = int(datastore["input"])
    result_int = FirstFactorial(number)
    result_str = str(result_int)
    json_format = '{"Output": '+result_str+'}'
    return json_format

@app.route('/api/rirstreverse', methods=['POST']) 
def FN_A2():
    if not request.json:
        abort(400)
    json_string = json.dumps(request.json)
    datastore = json.loads(json_string)
    word = str(datastore["input"])
    result_str = FirstReverse(word)
    json_format = '{"Output": "'+result_str+'"}'
    return json_format

@app.route('/api/alphabetsoup', methods=['POST']) 
def FN_A3():
    if not request.json:
        abort(400)
    json_string = json.dumps(request.json)
    datastore = json.loads(json_string)
    word = str(datastore["input"])
    result_str = AlphabetSoup(word)
    json_format = '{"Output": "'+result_str+'"}'
    return json_format

#Assignment_fucntion
def FirstFactorial(num):
  if num <0:
    return 'You must input positive value'
  if num==0:
    return 1
  #recursive function
  f= num* FirstFactorial(num-1)
  return(f)

def FirstReverse(str):
    return str[::-1]

def AlphabetSoup(str):
  f = ''.join(sorted(str))
  return f

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)