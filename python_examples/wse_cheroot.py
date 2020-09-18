# Example python web server using cheroot

# cheroot is cherrypy server separated into its own package.
# and this example will need something like this to work
# pip3 install --user cheroot

from cheroot import wsgi
# from cheroot.ssl import builtin

# ======================================================================================================================
# ======================================================================================================================
# def do_compute():

#     i = 0
#     for _ in range(90000):
#         i += 1


def wsgi_app(environ, start_response):  # pylint: disable=unused-argument

    # the wsgi must return an iterable of "bytestrings" (python3 bytes type)
    full_resp = [b'Hello, World']

    # wsgi only takes "strings" and "bytestrings". No such thing as int type anywhere in the spec,
    # hence the str(len...)
    response_headers = [
        ('Content-type', 'text/plain'),
        ('Content-Length', str(len(full_resp[0]))),
    ]

    status = '200 OK'
    start_response(status, response_headers)

    return full_resp


# ======================================================================================================================
# ======================================================================================================================
def main():

    cheroot_server_options = {
        'wsgi_app': wsgi_app,
        'bind_addr': ('0.0.0.0', 8082),

        # numthreads (int): number of threads for WSGI thread pool
        'numthreads': 10,

        # server_name (str): web server name to be advertised via Server HTTP header
        # 'server_name': None,
        # max (int): maximum number of worker threads
        # 'max': -1,
        # request_queue_size (int): the 'backlog' arg to socket.listen(); max queued conn
        # 'request_queue_size': 5,
        # timeout (int): the timeout in seconds for accepted connections
        # 'timeout': 10,
        # shutdown_timeout (int): the total time (sec), 2 wait 4 worker threads 2 cleanly exit
        # 'shutdown_timeout': 5,
        # accepted_queue_size (int): maximum number of active requests in queue
        # 'accepted_queue_size': -1,
        # accepted_queue_timeout (int): timeout for putting request into queue
        # 'accepted_queue_timeout': 10,
    }

    server = wsgi.Server(**cheroot_server_options)
    try:
        server.start()
    finally:
        server.stop()


if '__main__' == __name__:
    main()
