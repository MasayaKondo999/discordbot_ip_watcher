import discord
import requests


client = discord.Client()

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------ログイン成功------')


@client.event
async def on_message(message):
    # チャットの文字解析
    if message.content.startswith("/ip"):
        # 送り主がBotだった場合反応したくないので
        if client.user != message.author:
            # 発言
            res = requests.get('http://inet-ip.info/ip')
            m = "ipアドレスは  " + res.text +  "    だよ"
            # メッセージが送られてきたチャンネルへメッセージを送ります
            await message.channel.send(m)


# Discordのデベロッパサイトで取得したトークンを入れてください
client.run("-------------トークンを入力-----------")
