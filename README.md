# What is it?
This repository contains python source code of Recursion, Math Fundamentals, String Manipulation, String Maniulation, Sorting, Web Service.

# Program and API
I devoloped these codes by using `python` + `flask`(for Assignemnt4)

# Installation (for Assignment4)
## Python
Download Python: https://www.python.org/
OR
```
pip install virtualenv --upgrade
virtualenv --python=python3 ~/virtual-python3
source ~/virtual-python3/bin/activate
```

## Flask
Download Flask: http://flask.pocoo.org/
OR
```
$ pip install Flask
$ export FLASK_ENV=development
$ export FLASK_APP=app.py
$ flask run --host 0.0.0.0
```
* $ vim app.py <=== (contain code in Assignment4)

## Use Postman or Burp Suite to request API
Download Burp Suite: https://portswigger.net/burp
Download POSTMAN: https://www.getpostman.com/downloads/
Request following API
```
  /api/firstfactorial
  /api/rirstreverse
  /api/alphabetsoup
```
### Sample HTTP request (/api/firstfactorial)
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
```

### Sample HTTP response
```
	HTTP/1.0 200 OK
	Content-Type: text/html; charset=utf-8
	Content-Length: 18
	Server: Werkzeug/0.14.1 Python/3.6.8
	Date: Tue, 23 Apr 2019 04:28:50 GMT

	{"Output": 362880}
```