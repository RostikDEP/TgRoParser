from pyrogram import Client


class IdDetector:
    def __init__(self):
        self.app = Client("me_account")