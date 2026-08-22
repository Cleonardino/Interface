from discord import Client, Intents

## Setup
intents : Intents = Intents.default()
intents.message_content = True
client : Client = Client(intents=intents)