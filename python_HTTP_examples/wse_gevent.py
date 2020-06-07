# Example python web server using bottle/gevent

# When testing with wrk, I occasionally see some socket errors (mostly timeout)
# latencies are awful. you have 2 push -c down to 100 or less even then its like 20ms 30ms latency. 
# with -c4000 you get 300ms avg latency. 400ms 500ms 1s for higher percentiles. 

# It seems like the co-operative multi tasking causes the server to accept more connections than it can
# chew and ends up exploding the latencies through the root. 
# total req/s still way below golang. just barely above cheroot

# Starting things out with import monkey patch does not feel good either. 

# pip3 install --user gevent

from gevent import monkey; monkey.patch_all()

import bottle


def do_compute():
    
    i = 0
    for _ in range(90000):
        i += 1


@bottle.get('/')
def home_page():

    do_compute()
    return 'Hello World'



if '__main__' == __name__:

    ws_port = 7081
    debug = False
    host = '0.0.0.0'
    bottle.run(app=bottle.app(), host=host, port=ws_port, debug=debug, server="gevent")

