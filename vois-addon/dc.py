import discord 
from discord.ext import commands
from discord.file import File

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='/', intents=intents)
async def prin_b(ctx):
    await ctx.send("procesing...")
    
def admin():
    async def predicate(ctx):
        return ctx.author.id == 787016738859778099
    return commands.check(predicate)

from base import*
from node import*
#from pyautogui import*
from PIL import Image, ImageDraw
import pyautogui
from time import*
from keyboard import*
unpreass=0
import threading
from file_os import bot_screan
bot_screan=bot_screan()
@bot.event

async def on_command_completion(ctx):
        if bot_screan.read()=="0":
            return
        sleep(1)
        file_path = "data/cache/screan_chace.png"
        pyautogui.screenshot(file_path)
        image = Image.open(file_path)


        x, y = pyautogui.position()
        t=-10
        for i in range(21):
            try:
                image.putpixel((x-t, y), (255, 255, 255))
                t+=1
            except:
                t+=1
            
        t=-10
        for i in range(21):
            try:
                image.putpixel((x, y-t), (255, 255, 255))
                t+=1
            except:
                t+=1


        image.save(file_path)

        await ctx.send(file=File(file_path))
        


@bot.event
async def on_ready():
    channel_id = 1180509673821057127  # замініть це значення на ID вашого каналу
    channel = bot.get_channel(channel_id)

    if channel:
        await channel.send("My PC connected <@787016738859778099>")
    else:
        print(f"Unable to find the channel with ID {channel_id}")

        

@bot.command(name="move")
@admin()
async def bot_move(ctx, mode:str=None, b:int=0, x=None, y=None):
    await prin_b(ctx)
    if mode=="right":
        move(3, b)
    elif mode=="left":
        move(2, b)
    elif mode=="up":
        move(0, b)
    elif mode=="down":
        move(1, b)
    elif mode in ["center", "center-up", "center-down", "center-left",
                  "center-reight", "left-up", "up-left", "right-up",
                  "up-right", "right-down", "down-right", "left-down",
                  "down-left"]:
        move_xy(pos=mode) 
    elif x!=None and y!=None:
        move_xy(x=x, y=y)
         
    else:
        await ctx.send("not found arg")

@bot.command(name="click")
@admin()
async def bot_click(ctx):
    await prin_b(ctx)
    click()

@bot.command(name="rightclick")
@admin()
async def bot_right_click(ctx):
    await prin_b(ctx)
    rightClick()

@bot.command(name="centerclick")
@admin()
async def bot_center_click(ctx):
    await prin_b(ctx)
    click(button='middle')
    
@bot.command(name="dubleclick")
@admin()
async def bot_dable_click(ctx):
    await prin_b(ctx)
    click()
    click()
    
def hy():
    mouseDown(button="left")
    while True:
        pass

@bot.command(name="leftdown")
@admin()
async def bot_left_mouse_down(ctx):
    await prin_b(ctx)
    threading.Thread(target=hy).start()

@bot.command(name="leftup")
@admin()
async def bot_left_mouse_up(ctx):
    await prin_b(ctx)
    mouseUp(button="left")

@bot.command(name="write")
@admin()
async def bot_write(ctx, *text):
    text = ' '.join(text)
    await prin_b(ctx)
    write(text)

@bot.command(name="press")
@admin()
async def bot_press_button(ctx, button):
    await prin_b(ctx)
    button=button.split("+")
    hotkey(*button)
    
@bot.command(name="google")
@admin()
async def bot_google_open(ctx):
    await prin_b(ctx)
    google()
    
@bot.command(name="cmd")
@admin()
async def bot_open_cmd(ctx):
    await prin_b(ctx)
    hotkey("win", "r")
    write("cmd")
    hotkey("enter")
    
@bot.command(name="exit")
@admin()
async def bot_exit_window(ctx):
    await prin_b(ctx)
    hotkey("alt", "f4")
    
@bot.command(name="screanshot")
@admin()
async def bot_screanshot(ctx, mode:str="read"):
    await prin_b(ctx)
    if mode=="read":
        await ctx.send(bot_screan.read())
    elif mode=="True":
        bot_screan.write()
    elif mode=="False":
        bot_screan.write(0)
    else:
        await ctx.send("error args")
        
@bot.command(name="vois-node")
@admin()
async def bot_vois_node(ctx, text:str):
    lines=command.read()
    comman=[]
    lines=lines.split("\n")
    for line in lines:
        comman.append(line.split(", "))
    if comman[0][0]!="die": online(a=3, p="command")
    autput(text, comman)

"""
@bot.command()


@bot.command()


@bot.command()


@bot.command()
"""






















def test():
    print(mouseInfo())




def start_bot(bot):
    bot.run("MTA3MzIxMjc3MjU3MTE3Mjk5NQ.GqQnak.TjMdUjGbUg-PhHXOgBa2dV3djRUw-ydVDRdUxE")
    
#test()
start_bot(bot)
