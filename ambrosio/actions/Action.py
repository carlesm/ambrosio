class Action(object):
    """Action to be carried on by Ambrosio"""
    def __init__(self, cfg):
        super(Action, self).__init__()
        self.cfg = cfg

    def do(self):
        pass

    def is_for_you(self, word):
        pass
