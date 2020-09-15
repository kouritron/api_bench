"""
Example python web server using tornado
tornado is great for long polling. Also not WSGI, dont abuse it by using its "wsgi features"

-------------------- Things I like about tornado:
- Way more users, contributers than anything else in python HTTP land. probably still used at facebook heavily.
- Not WSGI. great drop that stone age wart.
- Not necesserarily async. good sync perf also. but can't beat long polling use cases. but single thread per process.

- lots of features and library packages that can, but dont have to be used:
    tornado.web: The main one that supplies RequestHandler and Application classes:
There is lots of other useful stuff like:
    tornado.template — Flexible output generation -- dont use it, emit JSON.
    tornado.routing — Basic routing implementation -- we'll need a router one way or another
    tornado.escape — Escaping and string manipulation -- I guess it doesnt hurt, tho there are some in python stlib
    tornado.websocket - Bidirectional communication to the browser -- If you need these, then you need these
    tornado.locks – Synchronization primitives -- notify sleeping async requests in long polling cases
    tornado.auth — 3rd-party login w/ OpenID and OAuth -- Its probably nice help. Tho for crypto control maybe needed
    and many more util stuff, static files(probably better than bottle), even things to help cli parsing, ....

-------------------- Things I dont like about tornado:
- too much code, even tho you dont use most of these, still by the time, you spread large number of contributers
    over this much code, you are actually not left with too many eye per line of code.

- too much code could also become a undecipherable blackbox. with bottle we learnt so much, about it we made our
    own framework eventually. no hidden secrets there. This can be good and bad. You shouldnt re-create everything, but
    hey if you dont need it or python stdlib or linux do this already, I probably dont want an extra 100k python code.

- who likes async, cheroot looks way cleaner, if you dont need long polling, but its not just async. thats there
    if you need it.

- Too much OOP BS, ppl use this with things like "base handler" class "that sets some headers" and "Session MixIn"
multiple inheritance crap that I dont like. Why cant these just be functions. whats wrong with "request handler"
calling a func to add or get session, call a function to set base headers (which you shouldnt even use, we said JSON
API like 10 years ago. Why would you build HTML pages and have one class build the <HEAD> section. it gets crazy
quickly)

- Ecosystem seems to like sqlalchemay which I hate so fkng much. I will never fall for the fraud that is sqlalchemy.
Good news is you dont have to touch it with a ten foot pole.

- routes list is not full info, source of truth. it doesnt have HTTP verb info. not a big deal but its a bummer.


"""
# --------------------
# pip3 install --user tornado  # is enof
# better to get these also:
# - pycurl (python libcurl)
# - pycares (python version of c-ares, aka C async resolution of DNS)
# a couple others you dont need unless you use stone age python

# pip3 install pycurl fails on ubuntu 18:04 for some reason, even in a fresh container. TODO investigate

import tornado.ioloop
import tornado.web


class HandlerForRoot(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, world")


def make_app():

    tornado_routes = [
        (r"/", HandlerForRoot),
    ]

    return tornado.web.Application(tornado_routes)


def main():
    app = make_app()
    app.listen(8082)
    tornado.ioloop.IOLoop.current().start()


if __name__ == "__main__":
    main()
