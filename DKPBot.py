import requests
from bs4 import BeautifulSoup
import urllib
import discord
from discord.ext import commands
bot = commands.Bot(command_prefix='!', description='I get DKP stats from the Lethality Forums!')

@bot.event
async def on_ready():
    print("Logged in as")
    print(bot.user.name)

@bot.command()
async def dkp():
    charname = 'Baldular'
    dkptotal = 'somenumber'
    url = "http://www.eqdkp.lethalitygaming.com/index.php/Character/" + charname + "-125.html?s=&with_twinks=0"
    r = requests.get(url)
    data = r.text
    soup= BeautifulSoup(data)
    print
    type(soup)

    await bot.say("Total DKP for " + " " + charname + ': ' + dkptotal)

@bot.command()
async def attendance():
    charname = 'Baldular'
    raidpercent = '40' + '%'
    await bot.say("Raid Attendance for " + charname + ': ' + raidpercent)


@bot.command()
async def drak():
    await bot.say("HEALS TO DRAK!!! HEALS TO DRAK!!! HEALS TO DRAK!!!")

bot.run('MzU3MzA4MDgwNDY5NDQyNTYx.DJoc0Q.uc_KKM7tcd6DZuISLRIOG46wyc4')

# <tr>
# <td class="twinktd">Default</td>
# <td class="twinktd"><span class="positive">252</span></td>
# <td class="twinktd"><span class="negative">90</span></td>
# <td class="twinktd"><span class="neutral">0</span></td>
# <td class="twinktd"><span class="positive">139</span></td>  # !dkp
# <td class="twinktd"><span class="positive">41% (16/39)</span></td> # !attendance
# <td class="twinktd"><span class="positive">45% (38/85)</span></td>
# <td class="twinktd"><span class="positive">40% (59/147)</span></td>
# <td class="twinktd"><span class="positive">56% (59/106)</span></td>
# </tr>
