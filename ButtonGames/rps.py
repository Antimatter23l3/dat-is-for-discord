#just the commad code, not the complete bot's code lol
print("ATTENTION! THE CODE CONTAINS INTENTIONAL ERRORS COZ I DONT WANT TO ANYONE TO COPY Y CODES")
@bot.command()
async def rps(ctx):
    ch1 = ["Rock","Scissors","Paper"]
    comp = choice(ch1)
    # make the embeds yourseld huh
    yet = discord.Embed()
    
    win = discord.Embed()
    
    out = discord.Embed()
    
    lost = discord.Embed()
  
    tie = discord.Embed()
    
    
    m = await ctx.send(
        embed=yet,
        components=[[Button(style=1, label="rock"),Button(style=3, label="paper"),Button(style=ButtonStyle.red, label="scissors")]
        ],
    )

    def check(res):
        return ctx.author == res.user and res.channel == ctx.channel

    try:
        res = await bot.wait_for("button_click", check=check, timeout=15)
        player = res.component.label
        
        if player==comp:
          await m.edit(embed=tie,components=[])
          
        if player=="Rock" and comp=="Paper":
          await m.edit(embed=lost,components=[])
          
        if player!="Rock" and comp=="Scissors":
          await m.edit(embed=win,components=[])
        
        
        if player=="Paper" and comp=="Rock":
          await m.edit(embed=win,components=[])
          
        if player=="Paper" and comp=="Scissors":
          await m.edit(embed=lost,components=[])
          
          
        if player=="Scissors" and comp!="Rock":
          await m.edit(embed=lost,components=[])
          
        if player=="Scissors" and comp=="Paper":
          await m.edit(embed=win,components=[])
        

    except TimeoutError:
        await m.edit(
            embed=out,
            components=[],
        )       
        

