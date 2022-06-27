import os
from pprint import pprint
from re import template
from time import time
from urllib import response
from requests import request
from bottle import *;
import algebra

secret = "A lot of people dont know how nice I am"

file_template = '''\
<h1>List of files in <em>Congress data</em> </h1> 
<hr>
<ol>
    % for file in files:
        <li> <a href = "files/{{file}}"> {{file}}</li>
    % end
</ol>
'''
@route('/')
def welcome():
    # content negotiation
    response.set_header('Vary', 'Accept')
    if 'text/html' in request.headers.get('Accept', '*/*'):
        response.content_type  = 'text/html'
        return '<h1>Howdy</h1>'
    return "hello"

@route('/now')
def time_service():
    response.set_header('Vary', 'Accept')
    response.content_type  = 'text/plain'
    response.set_header('Cache-Control', 'max-age = 1')
    return time.ctime()

# take additional parameter
@route('/upper/<word>')
def upper_case_service(word:str):
    response.content_type = 'text/plain'
    return word.upper()

# passing a query
@route('/areaCircle')
def area_circle_service():
    last_visit = request.get_cookie('last-visit', 'unknown', secret = secret)
    print(f'last-visit {last_visit}')
    response.set_cookie('last-visit', time.ctime(), secret = secret)
    response.set_header('Vary', 'Accept')
    try:
        radius = float(dict(request.query).get('radius', 0.0))
    except ValueError as e:
        return e.args[0]
    if 'text/html' in request.headers.get('Accept', '*/*'):
        response.content_type  = 'text/html'
        area = algebra.area_cirle(radius)
        return f'<p>Area of a cirlce is <em>{area}</em> </p>'
    return dict(area = area, radius = radius, service  = request.path)

@route('/files')
def show_files():
    files = os.listdir('../part-I/Congress Data Clustering/congress_data')
    response.set_header('Vary', 'Accept')
    if 'text/html' not in request.headers.get('Accept', '*/*'):
        return dict(files = files)
    return template(file_template, files = files)

@route('/files/<filename>')
def show_one_file(filename):
    return static_file(filename, '../part-I/Congress Data Clustering/congress_data')

if __name__ == "__main__":
    run(host = 'localhost', port = 8080)
    print("rest api server is listening")