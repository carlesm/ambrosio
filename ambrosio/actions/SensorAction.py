from Action import Action


class SensorAction(Action):
    """Sensors for Ambrosio"""
    def __init__(self):
        super(SensorAction, self).__init__()
        self.triggers = ["temperature"]

    def do(self, command):
        print "Will measure temperature ", " ".join(command)
        return "OK"

    def is_for_you(self, word):
        if word in self.triggers:
            return True
        return False
