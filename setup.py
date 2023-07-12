from setuptools import setup

setup(name='radiobot',
	version='0.1',
	description='Discord bot to play youtube on voice channel',
	url='http://github.com/NyanCoder-1/radiobot',
	author='NyanCoder',
	install_requires=[
		'youtube_dl',
		'discord.py[voice]',
	],
	zip_safe=False)
