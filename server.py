import tornado.ioloop
import tornado.web
import poset

class MainHandler(tornado.web.RequestHandler):
    def get(self):
    	self.render("index.html")

class AntiChain(tornado.web.RequestHandler):
	def get(self,foo):
		self.write(poset.getDiagramPosetOf(range(int(foo))))

application = tornado.web.Application([
    (r"/", MainHandler),
    (r"/antichainpage/(.*)", AntiChain)
])

if __name__ == "__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()
