# Example python web server using bottle/cheroot

# cheroot is cherrypy server separated into its own package.
# and this example will need something like this to work
# pip3 install --user cheroot

import bottle

def do_compute():

    i = 0
    for _ in range(90000):
        i += 1


@bottle.get('/')
def home_page():

    # print("home page called.")
    do_compute()
    return 'Hello World'

if '__main__' == __name__:

    ws_port = 7081
    debug = False
    host = '0.0.0.0'

    bottle.run(app=bottle.app(), host=host, port=ws_port, debug=debug, server="cheroot")
