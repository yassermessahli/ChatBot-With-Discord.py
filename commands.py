import funcs


def command_apply(bot):
    @bot.command(name='quote', help='Get a random quote')
    async def quote(ctx):
        quote = funcs.get_quote()
        await ctx.channel.send(f'> `{quote}`')

    @bot.command(name='ping', help='Get the bot\'s ping')
    async def ping(ctx):
        await ctx.reply(f'pong! {ctx.author.mention}')

    @bot.command(name='trans', help='Translate text')
    async def trans(ctx, *, text):
        await ctx.channel.send(f'`{funcs.translate(text, "ar")}`')


    @bot.command(brief='this is a meme', name='meme', help='Get a random empty meme')
    async def meme(ctx):
        meme = funcs.get_meme()
        await ctx.send(f'{meme["url"]}')

    @bot.command(name='dog', help='Get a random dog')
    async def dog(ctx):
        dog = funcs.get_dog()
        await ctx.send(f'{dog}')

    @bot.command(name='cat', help='Get a random cat')
    async def cat(ctx):
        cat = funcs.get_cat()
        await ctx.send(f'{cat}')

    @bot.command(name='joke', help='Get a random joke')
    async def joke(ctx):
        joke = funcs.get_joke()
        await ctx.send(f'{joke}')\


    @bot.command(name='helpme', help='Get help')
    async def helpme(ctx):
        await ctx.channel.send(f'''
> **Commands:**

>>> `!quote` - Get a random quote
`!ping` - Get the bot's ping
`!trans <text>` : translate a text to arabic language
`!meme` : Get a random meme
`!dog` : Get a random image of a dog
`!cat` : Get a random image of a cat
`!joke` : Get a random joke
`!help` : Get help''')
