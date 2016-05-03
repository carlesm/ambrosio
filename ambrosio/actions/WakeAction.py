from Action import Action
from wakeonlan import wol


class WakeAction(Action):
    """Wakes the computer"""
    def __init__(self, cfg):
        super(WakeAction, self).__init__(cfg)
        self.triggers = ["wake"]

    def do(self, command):
        print "Will wake a computer ", " ".join(command)
        ret = "No conegut(s)"
        for arg in command:
            for pc in self.cfg["wol"]["pcs"]:
                if arg == pc["nom"]:
                    wol.send_magic_packet(pc["mac"])
                    ret = "OK"
        return ret

    def is_for_you(self, word):
        if word in self.triggers:
            return True
        return False
