import os
from dotenv import load_dotenv

load_dotenv()
import random

##유투브 음악 추출 관련
from yt_dlp import YoutubeDL

##디스코드 관련 
import discord
from discord.ext import commands
from discord import app_commands

intents = discord.Intents.default()
intents.message_content = True ##채팅 가능
intents.dm_messages = False    ##dm 불가능

##명령어prefix -> !
bot = commands.Bot(command_prefix=("!"), intents = intents) 

##테스트----------------------------------------------------
@bot.event
async def on_ready():
    print("봇 실행")

@bot.tree.command(name = "엄", description = "준식 임")
async def 엄(interaction: discord.Interaction):
    embed = discord.Embed(title = "test", color = 0x00ff00)
    embed.add_field(name = "test2", value = "test3", inline = False)
    await interaction.response.send_messsage(embed = embed)



# @bot.command()##def [명령어](ctx) -> 명령어라는 채팅을 읽으면 동작
# async def 엄(ctx):
#     ##ctx.send -> 해당 채널에 채팅을 보냄
    # await ctx.send("준식")


##명령어----------------------------------------------------
@bot.command()  
async def 명령어(ctx):
    await ctx.send("!룰렛: 룰렛 관련 명령어\n")


##노래 관련------------------------------------------------
# 
# /재생 [음악이름 or url]
# 
# url 일 경우, 해당 영상을 바로 queue 에 추가 
#  
# 음악 이름일경ㅈ우, 음악 이름을 유투브에 검색 -> 상단 3개를 해당 채널에 팝업.
# 3개중 선택하여 Queue 에 추가 
# 
# 이후 해당 영상에서 음악 추출
# 
# 추출 완료시 보이스챗에서 재생
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 


##룰렛 관련---------------------------------------------------
roulette = []


@bot.command()
async def 룰렛(ctx, action: str = '', *, content: str = ''):
    if action == "추가":
        if content in roulette:
            await ctx.send("이미 있음")
            return
        if content == '':
            await ctx.send("항목이름을 입력해라 게이야")
            return
        roulette.append(content)
        temp = "##룰렛에 " + content + " 가 추가됨##"
        await ctx.send(temp)

    elif action == "삭제":
        if len(roulette) == 0:
            await ctx.send("##룰렛에 아무것도 설정 되어 있지 않음##")
            return
        if content in roulette:
            roulette.remove(content)
            temp = "##룰렛에서 " + content + "삭제됨##"
            await ctx.send(temp)
        elif content == '':
            await ctx.send("항목이름을 입력해라 게이야")
            return
        else:
            await ctx.send("룰렛목록에 그런건 없음")
    
    elif action == "돌리기":
        if len(roulette) == 0:
            await ctx.send("안에 아무것도 없다 게이야")    
        else:
            result = roulette[random.randrange(0,len(roulette))]
            temp ="##" + result + " 당첨##"
            await ctx.send(temp)
            roulette.clear()
            await ctx.send("!!룰렛 초기화됨!!")

    elif action == "목록":
        if len(roulette) == 0:
            await ctx.send("룰렛에 아무것도 추가하지 않았음")
        else:
            result = str(roulette)
            temp = "룰렛 목록: " + result
            await ctx.send(temp)
    elif action == '':
        await ctx.send("룰렛 명령어 사용법\n!룰렛 추가 [항목이름] : 룰렛에 항목 추가\n!룰렛 삭제 [항목이름] : 룰렛에서 항목 삭제\n!룰렛 돌리기 : 룰렛 돌리기(한번 돌리면 초기화)\n!룰렛 목록 : 룰렛 목록 보기")
    
bot.run(os.getenv("DISCORD_API_KEY"))




