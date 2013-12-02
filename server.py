import tornado.ioloop
import tornado.web
import poset
import os

static_path = os.path.join(os.path.dirname(__file__),"static")


class MainHandler(tornado.web.RequestHandler):
    def get(self):
    	self.render("index.html")

class AntiChain(tornado.web.RequestHandler):
	def get(self,foo):
		self.write(poset.getDiagramPosetOf(range(int(foo))))

application = tornado.web.Application([
    (r"/antichainpage/(.*)", AntiChain),
    (r'/static/(.*)', tornado.web.StaticFileHandler, {'path': static_path}), 
    (r'/', MainHandler)
])

if __name__ == "__main__":
    application.listen(8080)
    tornado.ioloop.IOLoop.instance().start()
