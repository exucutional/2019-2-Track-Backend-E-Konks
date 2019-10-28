import time
def handler(environ, start_response):
    mstr = 'Hello! Current time: ' + time.asctime() + '\n'
    data = bytes(mstr.encode())
    start_response('200 OK', [
        ("Content-Type", "text/plain"),
        ("Content-Lenght", str(len(data)))
    ])
    return iter([data])
