from pyrogram import Client, filters
from pyrogram.types import Message

api_id = api id
api_hash = "api hash"
token = "token"

app = Client("antiviewcounterbot", api_id, api_hash, bot_token=token)

viewsfilter = filters.create(lambda _, __, Message: Message.views)


@app.on_message(viewsfilter & ~filters.linked_channel & ~filters.channel)
async def antiviewcounter(client, message):
    await message.delete()


app.run()
