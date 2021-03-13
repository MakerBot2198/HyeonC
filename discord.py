import discord
import datetime
import time
import asyncio
import os
from discord.ext import commands

client = discord.Client()

@client.event
async def on_ready():
    print("봇이 성공적으로 실행되었습니다.")
    game = discord.Streaming(name="BC ClaN 문의", url='https://www.twitch.tv/bc-clan')
    await client.change_presence(status=discord.Status.online, activity=game)


@client.event
async def on_message(message):
    if message.content.startswith("/색깔"):
        await message.channel.send('`빨강` `주황` `노랑` `초록` `파랑` `보라` `분홍` `검정` `민트` `하늘` `갈색` `회색` `남색`')

    if message.content.startswith("/임베드"):
        if message.content[5:7] == '빨강':
            selcolor = 0xFF0000
        if message.content[5:7] == '주황':
            selcolor = 0xFF8C00
        if message.content[5:7] == '노랑':
            selcolor = 0xFFDC37
        if message.content[5:7] == '초록':
            selcolor = 0x00FC08
        if message.content[5:7] == '파랑':
            selcolor = 0x006AFF
        if message.content[5:7] == '보라':
            selcolor = 0x9932CC
        if message.content[5:7] == '분홍':
            selcolor = 0xFF00FF
        if message.content[5:7] == '검정':
            selcolor = 0x000000
        if message.content[5:7] == '민트':
            selcolor = 0x00FFDD
        if message.content[5:7] == '하늘':
            selcolor = 0x3CFBFF
        if message.content[5:7] == '갈색':
            selcolor = 0x8B4F1D
        if message.content[5:7] == '회색':
            selcolor = 0x828282
        if message.content[5:7] == '남색':
            selcolor = 0x3700FF

        value = message.content[8:]
        embed = discord.Embed(color=selcolor)
        embed.add_field(name="\u200b", value=value, inline=False)
        embed.set_author(name="BC ClaN", icon_url=message.author.avatar_url)

        await message.channel.send(embed=embed)
        await message.delete()
        
    if message.content == '/내정보':
        user = message.author
        date = datetime.datetime.utcfromtimestamp(((int(user.id) >> 22) + 1420070400000) / 1000)
        await message.channel.send(f"{message.author.mention}의 가입일 : {date.year}년/{date.month}월/{date.day}일/{date.hour}시/{date.minute}분/{date.second}초")
        await message.channel.send(f"```# {user}\n* 닉네임 :{user.display_name}\n{user.name}의 이름 : {user.name} \n아이디 : {user.id} \n닉네임 : {user.display_name}```")
        await message.channel.send(message.author.avatar_url)
        
    if message.content.startswith("/청소"):
        number = int(message.content.split(" ")[1])
        await message.delete()
        await message.channel.purge(limit=number)
        time.sleep(1)
        embed = discord.Embed(color=0x9932CC)
        embed.add_field(name="\u200b", value=f"{number}개의 메시지가 삭제되었습니다.", inline=False)
        embed.set_author(name="BC ClaN 메시지 삭제")

        await message.channel.send(embed=embed)
        time.sleep(10)
        
access_token = os.environ['BOT_TOKEN']
client.run(access_token)
