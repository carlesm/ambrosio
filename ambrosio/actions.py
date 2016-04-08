

class Action(object):
    """Action to be carried on by Ambrosio"""
    def __init__(self):
        super(Action, self).__init__()

    def do(self):
        pass

    def is_for_you(self, word):
        pass


class MusicPlayer(Action):
    """MusicPlayer for Ambrosio"""
    def __init__(self):
        super(MusicPlayer, self).__init__()
        self.triggers = ["music", "audio"]

    def do(self):
        print "Will play music"

    def is_for_you(self, word):
        if word in self.triggers:
            return True
        return False
