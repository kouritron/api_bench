
# ***** install ubuntu
# apt install build-essential libev-dev python2-dev
# {pip, pip3} install bjoern

from bjoern import run


def wsgi_app(environ, start_response):  # pylint: disable=unused-argument

    # the wsgi must return an iterable of "bytestrings" (python3 bytes type)
    full_resp = [b'Hello, World']

    # wsgi only takes "strings" and "bytestrings" no such thing as int type anywhere in the spec, hence the str(len...)
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
    run(wsgi_app, "0.0.0.0", 8082)


if '__main__' == __name__:
    main()
