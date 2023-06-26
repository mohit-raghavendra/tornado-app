import tornado


class StartHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("../html/start.html", n=0, result="")
