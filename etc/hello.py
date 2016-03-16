#bind="0.0.0.0:8080"

#def app (environ, start_response):
#    status = '200 OK'
#    response_headers = [('Content-type','text/plain')]
#    start_response(status, response_headers)
#    options = environ['QUERY_STRING'].split("&")
#    return [i+'\n' for i in options]
def app (environ,start_response):
    status = '200 OK'
    headers= [('Content-type','text/plain')]
    start_response(status,headers)
    body="\r\n".join(environ['QUERY_STRING'].split('&'))
    return [body]
