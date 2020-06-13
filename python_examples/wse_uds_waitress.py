from waitress import serve

# ======================================================================================================================
# ======================================================================================================================

# def do_compute():

#     i = 0
#     for _ in range(90000):
#         i += 1


# simple wsgi app.
def ws(environ, start_response):

    # do_compute()

    data = b"Hello, World!\n"
    start_response("200 OK", [("Content-Type", "text/plain"), ("Content-Length", str(len(data)))])

    return iter([data])


if __name__ == '__main__':

    serve(ws, unix_socket='/tmp/wse_waitress_test.sock')
