from Channel import Channel

import telepot


class AmbrosioBot(telepot.Bot):
    """AmbrosioBot is my telegram bot"""
    def __init__(self, token):
        super(AmbrosioBot, self).__init__(token)
        self.clist = None

    def set_list(self, clist):
        self.clist = clist

    def on_chat_message(self, msg):
        content_type, chat_type, chat_id = telepot.glance(msg)
        if content_type == 'text':
            command = msg['text']
            if self.clist is not None:
                self.clist.append(command)


class TelegramChannel(Channel):
    """Channel class, received commands from telegram"""
    def __init__(self, name="TelegramChannel"):
        super(TelegramChannel, self).__init__(name)
        self.bot = AmbrosioBot("134963018:AAEV40aoY1zGK2ECr9kIBYzxDj9NLNDpIRI")
        self.messages = []
        self.bot.set_list(self.messages)
        self.bot.notifyOnMessage()

    def get_msg(self):
        if self.msg_avail():
            return self.messages.pop(0)

    def msg_avail(self):
        return len(self.messages) > 0
