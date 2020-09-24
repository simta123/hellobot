import discord
import asyncio
import random
import openpyxl
from discord import Member
from discord.ext import commands
import youtube_dl
from urllib.request import urlopen, Request
import urllib
import urllib.request
import bs4
import 급식
import os
import sys
import json
from selenium import webdriver
import time
import datetime

countG = 0
client = discord.Client()
players = {}
queues= {}
musiclist=[]
mCount=1
searchYoutube={}
searchYoutubeHref={}

def check_queue(id):
    if queues[id]!=[]:
@@ -100,7 +104,16 @@ async def on_message(message):
            colour = discord.Colour.blue()
        )

        embed.set_footer(text = '끗')
        #embed.set_footer(text = '끗')
        dtime = datetime.datetime.now()
        #print(dtime[0:4]) # 년도
        #print(dtime[5:7]) #월
        #print(dtime[8:11])#일
        #print(dtime[11:13])#시
        #print(dtime[14:16])#분
        #print(dtime[17:19])#초
        embed.set_footer(text=str(dtime.year)+"년 "+str(dtime.month)+"월 "+str(dtime.day)+"일 "+str(dtime.hour)+"시 "+str(dtime.minute)+"분 "+str(dtime.second)+"초")
        #embed.set_footer(text=dtime[0:4]+"년 "+dtime[5:7]+"월 "+dtime[8:11]+"일 "+dtime[11:13]+"시 "+dtime[14:16]+"분 "+dtime[17:19]+"초")
        embed.add_field(name = '!안녕', value = '인사하고싶을때 ㄱㄱ',inline = False)
        embed.add_field(name='!오늘배그', value='오늘 배그각 알려줌', inline=False)
        embed.add_field(name='!홋치', value='!홋치 단어1 단어2 형식으로 적으면 학습함', inline=False)
@@ -165,16 +178,21 @@ async def on_message(message):


    if message.content.startswith("!재생"):

        server = message.server
        voice_client = client.voice_client_in(server)
        msg1 = message.content.split(" ")
        url = msg1[1]
        player = await voice_client.create_ytdl_player(url, after=lambda: check_queue(server.id))
        print(player.is_playing())
        players[server.id] = player
        await client.send_message(message.channel, embed=discord.Embed(description="재생한다!!!!"))
        print(player.is_playing())
        player.start()




    if message.content.startswith("!일시정지"):
        id = message.server.id
        await client.send_message(message.channel, embed=discord.Embed(description="장비를 정비합니다"))
@@ -189,19 +207,21 @@ async def on_message(message):
        id = message.server.id
        await client.send_message(message.channel, embed=discord.Embed(description="세계의 시간은 멈춰있다..."))
        players[id].stop()
        print(players[id].is_playing())

    if message.content.startswith('!예약'):
        msg1 = message.content.split(" ")
        url = msg1[1]
        server = message.server
        voice_client = client.voice_client_in(server)
        player = await voice_client.create_ytdl_player(url, after=lambda: check_queue(server.id))
        print(player)

        if server.id in queues:
            queues[server.id].append(player)
            print('if 1 '+str(queues[server.id])) #queues배열 확인
        else:
            queues[server.id] = [player]
            queues[server.id] = [player] #딕셔너리 쌍 추가
            print('else 1' + str(queues[server.id]))#queues배열 확인
        await client.send_message(message.channel,'예약 완료\n')
        musiclist.append(url) #대기목록 링크
@@ -234,6 +254,8 @@ async def on_message(message):
            del queues[server.id]
            await client.send_message(message.channel,'예약중인 음악 모두 취소 완료')

        #if message.content.startswith('!'):




@@ -638,15 +660,6 @@ async def on_message(message):
            await client.send_message(message.channel, embed=embed3)


        #https://cdn.nekos.life/neko/neko_001.png
        #https://cdn.nekos.life/neko/neko001.png

    if message.content.startswith('!구규범'):
        number = random.randrange(1,23)
        filename = 'gu'+str(number)+'.jpg'
        #filename = "gu1"  + ".jpg"
        await client.send_message(message.channel, embed=discord.Embed(title="그의 찬란한 모습.....",color=discord.Color.red()))
        await client.send_file(message.channel, filename)


    if message.content.startswith('!실시간검색어') or message.content.startswith('!실검'):
@@ -683,7 +696,7 @@ async def on_message(message):
        client_id = ""
        client_secret = ""

        url = ""
        url = "https://openapi.naver.com/v1/papago/n2mt"
        print(len(learn))
        vrsize = len(learn)  # 배열크기
        vrsize = int(vrsize)
@@ -798,16 +811,7 @@ async def on_message(message):
        embed.add_field(name='모래', value=급식.lunchtextD2(), inline=False)
        await client.send_message(message.channel, embed=embed)

    if message.content.startswith("!테스트"):
        embed = discord.Embed(
            title='테스트',
            description='ㅇㅇ',
            colour=discord.Colour.green()
        )
        embed.add_field(name='테스트', value='[Discordapp](<https://discordapp.com>)', inline=False)
        embed.add_field(name='테스트중..', value="https://youtu.be/WptXk39wiIQ", inline=False)
        await client.send_message(message.channel, embed=embed)


    if message.content.startswith("!복권"):
        Text = ""
        number = [1, 2, 3, 4, 5, 6, 7]
@@ -868,16 +872,120 @@ async def on_message(message):
            description="검색한 영상 결과",
            colour=discord.Color.blue())

        for i in range(0, 4):
        for i in range(0, 5):
            entireNum = entire[i]
            entireText = entireNum.text.strip()  # 영상제목
            print(entireText)
            test1 = entireNum.get('href')  # 하이퍼링크
            print(test1)
            rink = 'https://www.youtube.com'+test1
            embed.add_field(name=str(i+1)+'번째 영상',value=entireText + '\n링크 : '+rink)
           # embed.add_field(name=str(i+1)+'번째 영상',value=entireText + '\n링크 : '+rink)
            embed.add_field(name=str(i + 1) + '번째 영상', value='\n' + '[%s](<%s>)' % (entireText, rink),
                            inline=False)  # [텍스트](<링크>) 형식으로 적으면 텍스트 하이퍼링크 만들어집니다
            searchYoutubeHref[i] = rink
        await client.send_message(message.channel,embed=embed)

    if message.content.startswith('1'):

        if not searchYoutubeHref: #저장된 하이퍼링크가 없다면
            print('searchYoutubeHref 안에 값이 존재하지 않습니다.')
            await client.send_message(message.channel, embed=discord.Embed(description="검색한 영상이 없습니다."))
        else:
            print(searchYoutubeHref[0])
            server = message.server
            voice_client = client.voice_client_in(server)
            url = searchYoutubeHref[0]
            player = await voice_client.create_ytdl_player(url, after=lambda: check_queue(server.id))
            print(player.is_playing())
            players[server.id] = player
            await client.send_message(message.channel, embed=discord.Embed(description="재생한다!!!!"))
            print(player.is_playing())
            player.start()

            for i in range(0,5):
                del searchYoutubeHref[i]

    if message.content.startswith('2'):

        if not searchYoutubeHref:
            print('searchYoutubeHref 안에 값이 존재하지 않습니다.')
            await client.send_message(message.channel, embed=discord.Embed(description="검색한 영상이 없습니다."))
        else:
            print(searchYoutubeHref[1])
            server = message.server
            voice_client = client.voice_client_in(server)
            url = searchYoutubeHref[1]
            player = await voice_client.create_ytdl_player(url, after=lambda: check_queue(server.id))
            print(player.is_playing())
            players[server.id] = player
            await client.send_message(message.channel, embed=discord.Embed(description="재생한다!!!!"))
            print(player.is_playing())
            player.start()

            for i in range(0,5):
                del searchYoutubeHref[i]

    if message.content.startswith('3'):

        if not searchYoutubeHref:
            print('searchYoutubeHref 안에 값이 존재하지 않습니다.')
            await client.send_message(message.channel, embed=discord.Embed(description="검색한 영상이 없습니다."))
        else:
            print(searchYoutubeHref[2])
            server = message.server
            voice_client = client.voice_client_in(server)
            url = searchYoutubeHref[2]
            player = await voice_client.create_ytdl_player(url, after=lambda: check_queue(server.id))
            print(player.is_playing())
            players[server.id] = player
            await client.send_message(message.channel, embed=discord.Embed(description="재생한다!!!!"))
            print(player.is_playing())
            player.start()

            for i in range(0,5):
                del searchYoutubeHref[i]

    if message.content.startswith('4'):

        if not searchYoutubeHref:
            print('searchYoutubeHref 안에 값이 존재하지 않습니다.')
            await client.send_message(message.channel, embed=discord.Embed(description="검색한 영상이 없습니다."))
        else:
            print(searchYoutubeHref[3])
            server = message.server
            voice_client = client.voice_client_in(server)
            url = searchYoutubeHref[3]
            player = await voice_client.create_ytdl_player(url, after=lambda: check_queue(server.id))
            print(player.is_playing())
            players[server.id] = player
            await client.send_message(message.channel, embed=discord.Embed(description="재생한다!!!!"))
            print(player.is_playing())
            player.start()

            for i in range(0,5):
                del searchYoutubeHref[i]

    if message.content.startswith('5'):

        if not searchYoutubeHref:
            print('searchYoutubeHref 안에 값이 존재하지 않습니다.')
            await client.send_message(message.channel, embed=discord.Embed(description="검색한 영상이 없습니다."))
        else:
            print(searchYoutubeHref[4])
            server = message.server
            voice_client = client.voice_client_in(server)
            url = searchYoutubeHref[4]
            player = await voice_client.create_ytdl_player(url, after=lambda: check_queue(server.id))
            print(player.is_playing())
            players[server.id] = player
            await client.send_message(message.channel, embed=discord.Embed(description="재생한다!!!!"))
            print(player.is_playing())
            player.start()

            for i in range(0,5):
                del searchYoutubeHref[i]


    if message.content.startswith('!이모티콘'):

        emoji = [" ꒰⑅ᵕ༚ᵕ꒱ ", " ꒰◍ˊ◡ˋ꒱ ", " ⁽⁽◝꒰ ˙ ꒳ ˙ ꒱◜⁾⁾ ", " ༼ つ ◕_◕ ༽つ ", " ⋌༼ •̀ ⌂ •́ ༽⋋ ",
@@ -1014,6 +1122,17 @@ async def on_message(message):
    if message.content.startswith('!반가워'):
        msg = '{0.author.mention} 나도반가워!'.format(message)
        await client.send_message(message.channel, msg)

client.run('')














client.run('토큰')
