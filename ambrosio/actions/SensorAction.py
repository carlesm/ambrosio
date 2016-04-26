from Action import Action
import subprocess


class SensorAction(Action):
    """Sensors for Ambrosio"""
    def __init__(self):
        super(SensorAction, self).__init__()
        self.triggers = ["temperature"]

    def do(self, command):
        print "Will measure temperature ", " ".join(command)
        th = subprocess.check_output(['sudo',
                                      'AdafruitDHT', '11', '4'])
        return th

    def is_for_you(self, word):
        if word in self.triggers:
            return True
        return False
