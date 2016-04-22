class Channel(object):
    """Channel class"""
    def __init__(self, cfg, name):
        super(Channel, self).__init__()
        self.name = name
        self.cfg = cfg

    def respond(self, response):
        print "RESPONSE: ", response
