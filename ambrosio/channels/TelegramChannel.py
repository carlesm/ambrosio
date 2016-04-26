from Channel import Channel

import telepot


class AmbrosioBot(telepot.Bot):
    """AmbrosioBot is my telegram bot"""
    def __init__(self, token, usuaris):
        super(AmbrosioBot, self).__init__(token)
        self.clist = None
        self.chat_id = None
        self.users = usuaris

    def set_list(self, clist):
        self.clist = clist

    def on_chat_message(self, msg):
        content_type, chat_type, chat_id = telepot.glance(msg)
        if content_type == 'text':
            command = msg['text']
            if msg['from']['id'] in self.users:
                if self.clist is not None:
                    self.clist.append(command)
                    self.chat_id = chat_id
            else:
                self.sendMessage(chat_id, "A cagar a la via!")

    def respond(self, response):
        if self.chat_id is not None:
            self.sendMessage(self.chat_id, response)



class TelegramChannel(Channel):
    """Channel class, received commands from telegram"""
    def __init__(self, cfg=None, name="TelegramChannel"):
        super(TelegramChannel, self).__init__(cfg, name)
        token = self.cfg["telegram"]["token"]
        self.bot = AmbrosioBot(token, self.cfg["telegram"]["usuaris"])
        self.messages = []
        self.bot.set_list(self.messages)
        self.bot.notifyOnMessage()

    def get_msg(self):
        if self.msg_avail():
            return self.messages.pop(0)

    def msg_avail(self):
        return len(self.messages) > 0

    def respond(self, response):
        if response is None:
            response = "Command not understood"
        self.bot.respond(response)
