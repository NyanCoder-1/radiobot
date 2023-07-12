import discord
from discord.ext import commands
import json
import asyncio
import re
import YTPlay

def synchronize_async_helper(to_await):
	async_response = []

	async def run_and_capture_result():
		r = await to_await
		async_response.append(r)

	loop = asyncio.get_event_loop()
	coroutine = run_and_capture_result()
	loop.run_until_complete(coroutine)
	return async_response[0]

def main():
	intents = discord.Intents.default()
	intents.message_content = True
	bot = commands.Bot(command_prefix='>', intents=intents)

	@bot.command()
	async def ping(ctx:commands.Context):
		await ctx.reply('pong')
	@bot.command()
	async def echo(ctx:commands.Context, msg:str):
		await ctx.reply(msg)
	@bot.command()
	async def slap(ctx:commands.Context):
		# grab the user who sent the command
		user=ctx.message.author
		voice_channel=user.voice.channel
		channel=None
		# only play music if user is in a voice channel
		if voice_channel!= None:
			# grab user's voice channel
			channel = voice_channel.name
			await ctx.reply('User is in channel: '+ channel)
			# create StreamPlayer
			vc = await voice_channel.connect(self_deaf=True)
			
			vc.play(discord.FFmpegPCMAudio('content/oof.mp3'))
			while vc.is_playing():
				await asyncio.sleep(1)
			# disconnect after the player has finished
			vc.stop()
			await vc.disconnect()
			vc = None
		else:
			await ctx.send('User is not in a voice channel.')

	synchronize_async_helper(YTPlay.setup(bot))

	configData = json.load(open('config.json', 'r'))
	bot.run(configData['token'])

if __name__ == "__main__":
	main()
