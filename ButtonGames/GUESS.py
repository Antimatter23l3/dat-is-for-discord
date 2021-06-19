#bonus hhahahhahah


@bot.command()
async def guess(ctx):
    e = discord.Embed(title=f"{ctx.author}'s' Guessing Game!", description="> You haven't clicked on any button yet!",color=0xFFEA00)
    
    e1 = discord.Embed(title=f"{ctx.author}, You Guessed It Right!", description="> You have won!",color=0x00FF00)
    
    e3 = discord.Embed(title=f"{ctx.author}, You didn't Click on Time", description="> Timed Out!",color=discord.Color.red())

    
    e2 = discord.Embed(title=f"{ctx.author}, You Lost!", description="> You have lost!",color=discord.Color.red())
  
    
    m = await ctx.send(
        embed=e,
        components=[[Button(style=1, label="1"),Button(style=3, label="2"),Button(style=ButtonStyle.red, label="3")]
        ],
    )

    def check(res):
        return ctx.author == res.user and res.channel == ctx.channel

    try:
        res = await bot.wait_for("button_click", check=check, timeout=15)
        if res.component.label==choice(ch):
          
          await m.edit(embed=e1,components=[],)
        else: 
          await m.edit(embed=e2, components=[],)
          

    except TimeoutError:
        await m.edit(
            embed=e3,
            components=[],
        )
        
