#! usr/bin/env python3

import discord, asyncio, datetime
from get_news import get_news

update_news_ready= True

def main():
	TOKEN = input()
	client = discord.Client()
	
	async def print_news(channel):
		news = get_news()
		if news:
			tmp, link = news[0].replace("\n\n\n", "\n").replace("\n\n", "\n"), news[1]
			cntr = 0
			out = ""
			for a in tmp.split("\n"):
				if cntr + len(a) > 2000:
					await channel.send(out)
					out = a + "\n"
					cntr = len(a) + 1
				else:
					out +=  a + "\n"
					cntr += len(a) + 1
			if out:
				await channel.send(out)
			await channel.send(link)
		else:
			await(channel.send("no new news"))

	async def update_news(server):
		global ready
		await client.wait_until_ready()
		if datetime.datetime.now().hour == 23:
			channel = server.get_channel(574844490854957056)
			if str(channel) == "bns-news-update":
				await print_news(channel)
				update_news_ready= False
				await asyncio.sleep(3600)
				update_news_ready= True
			else:
				await channel.send("rip wrong channel")

	@client.event
	async def on_ready():
		print("The bot is ready!")
	
	@client.event
	async def on_message(message):
		global update_news_ready
		if not message.author.bot and update_news_ready:
			await update_news(message.guild)
		if message.content == "Hello" and str(message.author) == "Tushiroo#0221":
			await message.channel.send("*World*")
		if message.content == "!fp" and str(message.author) == "Tushiroo#0221":
			await print_news(message.channel)

	client.run(TOKEN)

if __name__ == "__main__":
	main()
