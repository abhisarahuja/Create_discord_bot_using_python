import discord

intents = discord.Intents.all()
client = discord.Client(commmand_prefix='!', intents = intents)

@client.event
async def on_ready():
    print("We have logged in as {0.user}".format(client))
    
@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith("hi"):
        await message.channel.send("Hello")
        
    if message.content.startswith('image'):
        await message.channel.send(file = discord.File("rewind.png"))
        
    if message.content.startswith("video"):
        await message.channel.send(file = discord.File("python.mp4"))
        
    if message.content.startswith("audio"):
        await message.channel.send(file = discord.File("Beautiful_Mistakes.mp3"))
        
    if message.content.startswith("file"):
        await message.channel.send(file = discord.File("Python.pdf"))
        

        
client.run("MTA2NzMxNTU3MjUxMTA4MDQ5OQ.G9IdSo.kCosbJuwC2Q5iE_1B89mAgsXKdG7ZmUQxVGUL8")