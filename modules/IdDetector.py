import asyncio

from pyrogram import filters, idle, handlers
from pyrogram.types import Message
from modules import app


class IdDetector:
    def __init__(self):
        self.app = app
        self.run = True
        self.word = ""
        self.app.add_handler(handlers.MessageHandler(self.MessageHandler))

    async def MessageHandler(self, client, message: Message):
        if message.text == self.word:
            print(f"ID detected: {message.chat.id}")
            self.run = False
            await self.app.stop()

    def DetectMessage(self, word):
        self.word = word
        print("Start detection...")
        while self.run:
            try:
                self.app.start()
            except Exception as e:
                # print(e)
                pass


# if __name__ == "__main__":
#     detector = IdDetector()
#     detector.DetectMessage("Test")
