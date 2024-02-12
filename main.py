from discord.ext import commands
import discord
import cloudscraper

s = cloudscraper.create_scraper()
bot = commands.Bot(command_prefix='.', intents=discord.Intents.all())

def crashPoint(num):
    info = s.get('https://api.bloxflip.com/games/crash').json()['history'][num]['crashPoint']
    return info

@bot.command()
async def crash(ctx):
    one = crashPoint(0)
    two = crashPoint(1)
    three = crashPoint(2)

    pst3 = [one, two, three]

    #get average of paste 3 games
    average = sum(pst3) / len(pst3)
    prediction = (1 / (average - 2) / 1)
    if prediction < 1:
        prediction = 1. + prediction
    safe = ''
    if prediction > 3:
        safe = 'Above 2x'
    elif prediction < 3:
        safe = "Less than 1.5x"
    elif prediction > 4:
        safe = 'Above 4x'
    prediction = "{:.2f}".format(prediction)
    em = discord.Embed(color=0xff55ff)
    em.add_field(name=f"**Prediction: {prediction}x**", value=f"Average: {int(average)}\nSafe Bet: {safe}")
    await ctx.reply(embed=em)


bot.run('MTIwNjQyMjA0ODQxNTY4MjU2MA.GblgOQ.lI0yZ3vhuQJgvo0C-xsxTIxF3tYomSlvyYqkvw')