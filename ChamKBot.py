import os
from dotenv import load_dotenv

load_dotenv()

import random
import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True
intents.dm_messages = False

bot = commands.Bot(command_prefix=("!"), intents = intents) 

@bot.command()
async def 엄(ctx):
    await ctx.send("준식")

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




