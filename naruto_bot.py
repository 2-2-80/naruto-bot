# インストールした discord.py を読み込む
import discord

# 自分のBotのアクセストークンに置き換えてください
TOKEN = (process.env.TOKEN)

# 接続に必要なオブジェクトを生成
client = discord.Client()

# 起動時に動作する処理
@client.event
async def on_ready():
    # 起動したらターミナルにログイン通知が表示される
    print('ログインしました')

# メッセージ受信時に動作する処理
@client.event
async def on_message(message):
    # メッセージ送信者がBotだった場合は無視する
    if message.author.bot:
        return
    # 「ナルト」と発言したら返る処理
    if message.content == 'ナルト':
        await message.channel.send('''[舞踏会にて]

トニー : まさか私が別人だと思っているの？

マリア : 私はあなたがそうでないことを知ってる。

トニー : それとも以前に会ったことがあるとでも？

マリア : 私たちがそうでないことは知っている。

トニー : 私は感じた...今までにないことが起こると思っていました。しかし、これはそれ以上のものだ。

マリア : 私の手は冷たいわ。

マリア : あなたの手もね。

マリア : とても暖かい。

トニー : とても美しい。

マリア : 美しい。

トニー : 信じられないくらいです。冗談じゃないのかい？

マリア : 私はまだそのような冗談の言い方を学んでいないわ。今では一生できないと思う。

ベルナルド : 手を離せ、アメリカ人!

マリア : ナルト！？

ベルナルド : 私の妹に近づかないでください。

トニー : 妹？

ベルナルド: 彼が彼らの一員であることがわからなかったのですか？

マリア：私には彼しか見えませんでした。

ベルナルド : 彼らが求めるものは一つプエルトリコ人の女の子に求めているものがあります。

トニー : それは嘘だよ

リフ：あとでね、トニー

チノ：逃げろ

トニー ：聞くなよ。

ベルナルド : 彼女は君の話を聞く前に僕の話を聞くよ。
      
: もし二人が解決したいなら...

: 頼むよ、君たち！すべてがうまくいっていたのに。さあ、来てください。みんなで楽しく過ごそうじゃないか。

マリア : ナルド...

ベルナルド : 彼女をここから連れ出してください。私たちは家に帰ります。

マリア : ナルド、私の最初のダンスです。

ベルナルド : お願いです。私たちは家族です。さあ、行ってください。

チノ : さあ、マリア。

トニー : ああ、マリア...。

ベルナルド : お前には会いたくない。

リフ : 君に話したいんだけどね。（二人だけになる）

リフ : 戦術会議にあなたが欲しいのです。ジェッツとシャーク。

ベルナルド : 喜びは私のものです。

リフ：外に出よう。

ベルナルド : あなたのような人がいると、ここの女性たちを一人にしておけないわ。あなたのような人がいると、女性を一人にしておけません。

ベルナルド : 真夜中に会おう。

リフ : ドックのお菓子屋さん？その前にジャズはやめてね。 

ベルナルド : ルールは理解している。ネイティブボーイ。

リフ : アイス！''')

# 「naruto」と発言したら返る処理
    if message.content == 'naruto':
        await message.channel.send('''[at the ball]

Tony : Don't tell me you think I'm someone else?

Maria : I know you're not.

Tony : Or do you think we've met before?

Maria : I know we haven't.

Tony : I felt... I knew something was going to happen that had never happened before. But this is more than that.

Maria : My hands are cold.

Maria : So are your hands.

Maria : Very warm.

Tony : So beautiful.

Maria : Beautiful.

Tony : It's unbelievable. Are you kidding me?

Maria : I haven't learned how to joke like that yet. I don't think I could ever do it now.

Bernardo : Get your hands off me, American!

Maria : Naruto!

Bernardo : Stay away from my sister.

Tony : Your sister?

Bernardo : Didn't you see that he was one of them?

Maria : He was all I could see.

Bernardo : There is one thing they are looking for in a Puerto Rican girl.

Tony : That's a lie.

Riff : See you later, Tony.

Chino : Run.

Tony : Don't listen to her.

Bernardo : She'll listen to me before she listens to you.

: If you two want to work this out...

: Please, you guys! Everything was going so well. Come on, come on. Let's have a good time together, shall we?

Maria : Naldo...

Bernardo : Please take her out of here. We're going home.

Maria : Naldo, this is my first dance.

Bernardo : Please. We're a family. Now, please go.

Chino : Come on, Maria.

Tony : Oh, Maria...

Bernardo : I don't want to see you.

Riff : I'd like to talk to you. (It's just the two of us)

Riff : I want you at the tactical meeting. Jets and Sharks.

Bernardo : The pleasure is mine.

Riff : Let's go outside.

Bernardo : With someone like you, I can't leave the women here alone. I can't leave the women alone with someone like you.

Bernardo : I'll see you at midnight.

Riff : The candy store on the dock? But first, don't jazz me up. 

Bernardo : I understand the rules. Native Boy.

Riff : Ice!''')
                                   
# Botの起動とDiscordサーバーへの接続
client.run(TOKEN)
