import tornado.ioloop
import tornado.web
import poset
import os

static_path = os.path.join(os.path.dirname(__file__),"public")

class MainHandler(tornado.web.RequestHandler):
    def get(self):
    	self.render("public/index.html")

class AntiChain(tornado.web.RequestHandler):
	def get(self,foo):
		self.write(poset.getDiagramPosetOf(range(int(foo))))

application = tornado.web.Application([
    (r"/antichain/(.*)", AntiChain),
    (r'/', MainHandler),
    (r'/(.*)', tornado.web.StaticFileHandler, {'path': static_path})
])

if __name__ == "__main__":
    try:
	port = os.environ['PORT'] 
    except KeyError:
	port = 5000

    application.listen(port)
    print "listening port", port
    tornado.ioloop.IOLoop.instance().start()
