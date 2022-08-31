import funcs


def command_apply(bot):
    @bot.command()
    async def quote(ctx):
        await ctx.author.send(f'quote for {ctx.author.mention}:\n{funcs.get_quote()}')

    @bot.command()
    async def ping(ctx):
        await ctx.send(f'pong! {ctx.author.mention}')
