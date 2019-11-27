import discord
import asyncio
from bs4 import BeautifulSoup
import requests
import bs4
from urllib.request import urlopen, Request
import urllib
import urllib.request


client = discord.Client()

@client.event
async def on_ready():
    print("다음으로 로그인됩니다 : ")
    print(client.user.name)
    print(client.user.id)
    print("===========")
    servers = len(client.servers)
    sum = 0
    for i in client.servers:
        sum += len(i.members)
    while True:
        await client.change_presence(game=discord.Game(name='`=도움말` 을 입력해보세요!'))
        await asyncio.sleep(10)
        await client.change_presence(game=discord.Game(name=str(servers)+'개의 서버 | '+str(sum)+'명의 유저'))
        await asyncio.sleep(10)

@client.event
async def on_message(message):
    if message.author.bot:
        return None
    
    if message.content.startswith("=도움말"):
        embed = discord.Embed(
            title = '초롱봇V3의 기능',
            description = '초롱봇V3에는 이런 기능이 있습니다.',
            colour = 0xff7f00
        )
        embed.add_field(name='=안녕', value='초롱봇이 반갑게 인사해줍니다.', inline=False)
        embed.add_field(name='=실시간검색어, =실검, =네이버실시간검색어', value='실시간 검색어를 알수 있습니다.', inline=False)
        embed.set_footer(text='문의:초롱이YT#3632')
        await client.send_message(message.channel, embed=embed)

    if message.content.startswith("=안녕"):
        embed = discord.Embed(
            title = '안녕',
            description = '반갑다',
            colour = 0xff7f00
        )
        embed.set_footer(text='문의:초롱이YT#3632')
        await client.send_message(message.channel, embed=embed)
    if message.content.startswith('=실시간검색어') or message.content.startswith('=실검') or message.content.startswith('=네이버실시간검색어'):
        url = "https://www.naver.com/"
        html = urllib.request.urlopen(url)

        bsObj = bs4.BeautifulSoup(html, "html.parser")
        realTimeSerach1 = bsObj.find('div', {'class': 'ah_roll_area PM_CL_realtimeKeyword_rolling'})
        realTimeSerach2 = realTimeSerach1.find('ul', {'class': 'ah_l'})
        realTimeSerach3 = realTimeSerach2.find_all('li')


        embed = discord.Embed(
            title='네이버 실시간 검색어',
            description='네이버의 실시간 검색어!',
            colour=0xff7f00
        )
        for i in range(0,20):
            realTimeSerach4 = realTimeSerach3[i]
            realTimeSerach5 = realTimeSerach4.find('span', {'class': 'ah_k'})
            realTimeSerach = realTimeSerach5.text.replace(' ', '')
            realURL = 'https://search.naver.com/search.naver?ie=utf8&query='+realTimeSerach
            print(realTimeSerach)
            embed.add_field(name=str(i+1)+'위', value='\n'+'[%s](<%s>)' % (realTimeSerach, realURL), inline=False) # [텍스트](<링크>) 형식으로 적으면 텍스트 하이퍼링크 만들어집니다
            embed.set_footer(text='naver.com 네이버')

        await client.send_message(message.channel, embed=embed)
    
   

client.run('NjIwOTA0MDU3MDY1NzAxMzc2.XdTDyQ.6Nw9vZfzzz8cQK9DtyPA8eZpqbc')