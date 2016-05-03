from Action import Action
from mpd import (MPDClient, CommandError)


class MusicPlayer(Action):
    """MusicPlayer for Ambrosio"""
    def __init__(self, cfg):
        super(MusicPlayer, self).__init__(cfg)
        self.triggers = ["music", "audio"]
        self.mpd = MPDClient()
        self.mpd.connect("localhost", "6600")

    def do(self, command):
        print "Will play music ", " ".join(command)
        print command
        return "OK"

    def is_for_you(self, word):
        if word in self.triggers:
            return True
        return False
