import os
import web

urls = (
	'/', 'Index'
)


class Index:
	def GET (self):
		return 'Hello world'
		
class AppTest(web.application):
	def run (self, port=80, *middleware):
		func = self.wsgifunc (*middleware)
		return web.httpserver.runsimple (func, ('0.0.0.0', port))
		
if __name__ == '__main__':
	app = AppTest (urls, globals())
	envport = int (os.getenv('VCAP_APP_PORT'))
	app.run (port=envport)