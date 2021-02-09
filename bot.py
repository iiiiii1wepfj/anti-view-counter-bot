from pyrogram import Client, filters

api_id = api id
api_hash = 'api hash'
token = "token"

app = Client("antiviewcounterbot", api_id, api_hash, bot_token=token)

viewsfilter = filters.create(lambda _, __, Message: Message.views)

@app.on_message(viewsfilter)
async def antiviewcounter(client, message):
 await message.delete()

app.run()
