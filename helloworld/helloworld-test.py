#! /usr/bin/python
# -*- coding: utf-8 -*-

from cgi import parse_qs, escape

def app (environ, start_response):
    status = '200 OK'
    output = 'Привет, мир! '
   
    # GET PARAMS:
    qs = parse_qs(environ['QUERY_STRING'])
    get_params = ''.join(['%s = %s, ' % (key, escape(qs[key][0])) for key in qs])
    
    # POST PARAMS:
    try:
        request_size = int(environ.get('CONTENT_LENGTH', 0))
    except (ValueError):
        request_size = 0

    request_body = environ['wsgi.input'].read(request_size)
    qs = parse_qs(request_body)
    post_params = ' '.join(['%s = %s, ' % (key, escape(qs[key][0])) for key in qs])

    #RESPONSE:
    response = output + 'GET: ' + get_params + 'POST: ' + post_params
    response_headers = [('Content-type', 'text/plain'),
                        ('Content-Length', str(len(response)))]

    start_response(status, response_headers)
    return iter([response])
