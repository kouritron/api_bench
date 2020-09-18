# Example python web server using gunicorn

# Run it like this
# pip3 install gunicorn
# gunicorn -b 0.0.0.0:8082 -w 4 wse_gunc:ws

# this example is just python gunicorn, you probably need other stuff as well.

def do_compute():

    i = 0
    for _ in range(90000):
        i += 1



def ws(environ, start_response):

    do_compute()

    data = b"Hello, World!\n"
    start_response("200 OK", [
        ("Content-Type", "text/plain"),
        ("Content-Length", str(len(data)))
    ])

    return iter([data])
