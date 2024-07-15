import os
import discord
from discord.ext import commands
from dotenv import load_dotenv
import asyncio

load_dotenv()

TOKEN = os.getenv('DISCORD_TOKEN')

if TOKEN is None:
    raise ValueError("DISCORD_TOKEN environment variable is not set")


# Define the bot
intents = discord.Intents.default()
intents.messages = True
intents.message_content = True
bot = commands.Bot(command_prefix='/', intents=intents)


@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    
    if message.content.lower().startswith(("i need help", "hey elite", "hey guide")):
        embed = discord.Embed(
            title=f'How can I help you, {message.author.name}?',
            description='I can give you information regarding:',
            color=discord.Color.blue()
        )
        embed.add_field(name='1. Builds', value='Learn about different builds.', inline=False)
        embed.add_field(name='2. Blacksmithing', value='Information on weapon forging, armor crafting, etc.', inline=False)
        embed.add_field(name='3. Synthesis', value='This section is under development, stay tuned', inline=False)
        embed.add_field(name='4. Equipment', value='This section is under development, stay tuned', inline=False)
        embed.add_field(name='5. Leveling', value='This section is under development, stay tuned', inline=False)

        help_message = await message.channel.send(embed=embed)

        def check(m):
            return m.author == message.author and m.channel == message.channel

        try:
            response = await bot.wait_for('message', check=check, timeout=30.0)

            if response.content.lower() in ['1', 'build', 'builds']:
                await handle_builds(message, check)
            elif response.content.lower() in ['2', 'bs', 'blacksmith', 'blacksmithing']:
                await handle_blacksmithing(message, check)
            else:
                await message.channel.send("Invalid choice. Please choose a valid option from the list.")
        except asyncio.TimeoutError:
            await message.channel.send("You took too long to respond.")
     
    elif message.content.lower().startswith(("hp food buff", "hp buff")):
        embed = discord.Embed(
            title='HP Buff House Addresses',
            description='1. 음영: 1010455 LVL 10 (Fridge)\n2. Kali NW: 3191130 LVL 10 (Fridge)\n3.『RI』Ghill: 1011945 LVL 10 (Fridge)\n4. Rikka♡: 3092003 LVL 10 (Fridge)\n5. Lescziena✩ : 1234567 LVL 10 (Fridge)\n6. ★空猫: 1010032 LVL 10 (Stove)\n7. Catanic: 5030666 LVL 9 (Fridge)',
            color=discord.Color.green()
        )
        await message.channel.send(embed=embed)
    
    elif message.content.lower().startswith(("mp food buff", "mp buff")):
        embed = discord.Embed(
            title='MP Buff House Addresses',
            description='1. Rediva♡: 1010013 LVL 10 (Fridge)\n2. yuxieyoko: 3017676 LVL 10 (Fridge)\n3. Salmonella: 1010216 LVL 10 (Fridge)\n4. Epiey!!: 1011212 LVL 10 (Fridge)\n5. Shyturu: 1032222 LVL 9 (Stove)\n6. Riin34: 6070013 LVL 9 (Stove)\n7. Hisao: 4046666 LVL 9 (Fridge)\n8. Riou: 4011793 LVL 10 (Fridge)',
            color=discord.Color.blue()
        )
        await message.channel.send(embed=embed)

    elif message.content.lower().startswith(("ampr food buff", "ampr buff")):
        embed = discord.Embed(
            title='Attack MP Recovery Buff House Addresses',
            description='1. 秋湫萩: 1010092 LVL 10\n2. ///KEN///: 3201003 LVL 10\n3. 、蒼炎の焰、: 1010006 LVL 10\n4. 颯: 2110000 LVL 10\n5. LUMiNA: 5252525 LVL 10\n6. Levy: 1010050 LVL 10\n7. O kara: 1011010 LVL 10\n8.Fuzuki: 3063101 LVL 10',
            color=discord.Color.greyple()
        )
        await message.channel.send(embed=embed)
    elif message.content.lower().startswith(("critical rate buff", "crt buff", "crit buff")):
        embed = discord.Embed(
            title='Critical Rate Food Buff Codes',
            description='''
Code: 1010092 LVL 10
Code: 3201003 LVL 10
Code: 1010006 LVL 10
Code: 4040404 LVL 10
Code: 1011902 LVL 10
Code: 1010017 LVL 10
Code: 5240001 LVL 10
Code: 3062728 LVL 10
Code: 1011010 LVL 10
Code: 3063101 LVL 10
Code: 1011010 LVL 10
Code: 1010050 LVL 10
Code: 5252525 LVL 10
Code: 2110000 LVL 10
        ''',
            color=discord.Color.gold()
        )
        await message.channel.send(embed=embed)
    elif message.content.lower().startswith(("weapon atk food buff", "weapon atk buff","weapon buff","watk buff")):
        embed = discord.Embed(
            title='WEAPON ATK Food Buff Codes',
            description='''
Code: 1010029 LVL 10
Code: 1010099 LVL 10
Code: 6010024 LVL 10
Code: 1011126 LVL 10
Code: 3070028 LVL 9
        ''',
            color=discord.Color.red()
        )
        await message.channel.send(embed=embed)
    elif message.content.lower().startswith(("str food buff", "str buff")):
        embed = discord.Embed(
            title='STR Food Buff Codes',
            description='''
Code: 4016699 LVL 10
Code: 7070777 LVL 10
Code: 6240980 LVL 9
Address: Elscaro-A-1 LVL 9
        ''',
            color=discord.Color.lighter_grey()
        )
        await message.channel.send(embed=embed)
    elif message.content.lower().startswith(("dex food buff", "dex buff")):
        embed = discord.Embed(
            title='DEX Food Buff Codes',
            description='''
Code: 1010058 LVL 10
Code: 6140110 LVL 9
Code: 1234567 LVL 9
Code: 4204200 LVL 8
Code: 1050051 LVL 8
Code: 3011143 LVL 8
        ''',
            color=discord.Color.dark_grey()
        )
        await message.channel.send(embed=embed)
    elif message.content.lower().startswith(("int food buff", "int buff")):
        embed = discord.Embed(
            title='INT Food Buff Codes',
            description='''
Code: 6010701 LVL 10
Address: Elscaro-z-1234 LVL 8
        ''',
            color=discord.Color.green()
        )
        await message.channel.send(embed=embed)
    elif message.content.lower().startswith(("agi food buff", "agi buff")):
        embed = discord.Embed(
            title='AGI Food Buff Codes',
            description='''
Code: 7162029 LVL 10
Code: 4010228 LVL 8
Code: 1010050 LVL 8
        ''',
            color=discord.Color.green()
        )
        await message.channel.send(embed=embed)
    elif message.content.lower().startswith(("vit food buff", "vit buff")):
        embed = discord.Embed(
            title='VIT Food Buff Codes',
            description='''
Code: 1012144 LVL 8
Code: 1010000 LVL 8
        ''',
            color=discord.Color.green()
        )
        await message.channel.send(embed=embed)
    elif message.content.lower().startswith(("accuracy", "accuracy buff","hit buff")):
        embed = discord.Embed(
            title='Accuracy Food Buff Codes',
            description='''
Code: 1010013 LVL 9
        ''',
            color=discord.Color.green()
        )
        await message.channel.send(embed=embed)
    elif message.content.lower().startswith(("magic resist", "magical resist","magical resistance","m res","m resist")):
        embed = discord.Embed(
            title='Magical Resist Food Buff Codes',
            description='''
Code: 1010004 LVL 10
Code: 4080087 LVL 9
Code: 7222227 LVL 9
Address: Sofya - Ward A- 69
        ''',
            color=discord.Color.green()
        )
        await message.channel.send(embed=embed)
    elif message.content.lower().startswith(("phy resist", "physical resist","physical resistance","p res","p resist")):
        embed = discord.Embed(
            title='Physical Resist Food Buff Codes',
            description='''
Code: 1020001 LVL 10
Code: 6010701 LVL 9
Code: 1100000 LVL 9
        ''',
            color=discord.Color.green()
        )
        await message.channel.send(embed=embed)
    elif message.content.lower().startswith(("FRACTIONAL BARRIER", "fractional barrier","fract barrier","fract resist")):
        embed = discord.Embed(
            title='FRACTIONAL BARRIER Food Buff Codes',
            description='''
Code: 1012222 LVL 10
Code: 2202202 LVL 9
        ''',
            color=discord.Color.green()
        )
        await message.channel.send(embed=embed)
    elif message.content.lower().startswith(("Aggro+", "+aggro","+aggro buff","aggro+ buff")):
        embed = discord.Embed(
            title='AGGRO + Food Buff Codes',
            description='''
Code: 6260113 LVL 10
Code: 3158668 LVL 10
Code: 1013000 LVL 9
Code: 1010207 LVL 9
Code: 7171717 LVL 9
        ''',
            color=discord.Color.green()
        )
        await message.channel.send(embed=embed)
    elif message.content.lower().startswith(("Aggro-", "-aggro","-aggro buff","aggro- buff")):
        embed = discord.Embed(
            title='AGGRO - Food Buff Codes',
            description='''
Code: 1010038 LVL 10
Code: 1011174 LVL 10
Address: Sofya-A-2 LVL 10
Code: 3061206 LVL 8
Code: 2110000 LVL 8
        ''',
            color=discord.Color.green()
        )
        await message.channel.send(embed=embed)
    elif message.content.lower().startswith(("drop buff", "Droprate buff","luck buff","ice cream buff")):
        embed = discord.Embed(
            title='Feel free to take this potato buff if you are a potato',
            description='''
Code: 4196969 LVL 6
Code: 7057777 LVL 6
        ''',
            color=discord.Color.green()
        )
        await message.channel.send(embed=embed)
         
    elif message.content.lower().startswith(("dte fire food buff", "dte fire buff")):
        embed = discord.Embed(
            title='DTE Fire Food Buff Codes',
            description='''
1. Code: 3210106 LVL 9
2. Code: 1010799 LVL 7
            ''',
            color=discord.Color.green()
        )
        await message.channel.send(embed=embed)
    

    elif message.content.lower().startswith(("dte earth food buff", "dte earth buff")):
        embed = discord.Embed(
            title='DTE Earth Food Buff Codes',
            description='''
1. Code: 3210103 LVL 9
2. Code: 2022222 LVL 8
3. Code: 1016646 LVL 7
        ''',
        color=discord.Color.dark_green()
    )
        await message.channel.send(embed=embed)

    elif message.content.lower().startswith(("dte water food buff", "dte water buff")):
        embed = discord.Embed(
            title='DTE Water Food Buff Codes',
            description='''
1. Code: 3210100 LVL 9
2. Code: 3062111 LVL 8
3. Code: 1110111 LVL 8
        ''',
        color=discord.Color.blue()
    )
        await message.channel.send(embed=embed)
                                  
    elif message.content.lower().startswith(("dte wind food buff", "dte wind buff")):
        embed = discord.Embed(
            title='DTE Wind Food Buff Codes',
            description='''
1. Code: 3210101 LVL 9
2. Code: 3062111 LVL 8
3. Code: 1010055 LVL 7
4. Code: 4099876 LVL 7
        ''',
        color=discord.Color.teal()
    )
        await message.channel.send(embed=embed)

    elif message.content.lower().startswith(("dte dark food buff", "dte dark buff")):
        embed = discord.Embed(
            title='DTE Dark Food Buff Codes',
            description='''
1. Code: 3210104 LVL 9
2. Code: 5010092 LVL 9
3. Code: 6010003 LVL 8
        ''',
        color=discord.Color.purple()
    )
        await message.channel.send(embed=embed)

    elif message.content.lower().startswith(("dte light food buff", "dte light buff")):
        embed = discord.Embed(
            title='DTE Light Food Buff Codes',
            description='''
1. Code: 3210105 LVL 9
2. Code: 1020345 LVL 9
3. Code: 4046666 LVL 8
        ''',
        color=discord.Color.lighter_grey()
    )
        await message.channel.send(embed=embed)

    elif message.content.lower().startswith(("dte neutral food buff", "dte neutral buff")):
        embed = discord.Embed(
            title='DTE Neutral Food Buff Codes',
            description='''
1. Code: 3210102 LVL 9
2. Code: 1019696 LVL 6
        ''',
        color=discord.Color.blurple()
    )
        await message.channel.send(embed=embed)


    elif message.content.lower().startswith(("what are the good xtals for ds","good crysta for dual sword","good xtal for ds","xtal for ds","crystals for ds","crysta for ds","ds xtal")):
        embed = discord.Embed(
            title='Recommended Crysta',
            description='''
1.For Weapon
  a)Don Profundo
  b)Devil Dango
  c)Vlam the Flame Dragon
  d)Red Ash Dragon Rudis
  
2.For Armour
  a)Altadar
  b)Red Ash Dragon Rudis
  c)Dx Fighter II
  d)Baavgai
  e)Doctor Pom Pom

3.For Add
  a)Prudent Blue Shadow
  b)Alfenix
  c)Evil Lefina
  d)Royal Ox King
  
4.For Ring
  a)Torexesa
  b)Dominaredor
  c)Etoise
  d)Stellar Ooze II
  e)Red Ash Dragon Rudis
  f)Sicanokami
  g)Aubergine Dragon Auvio
        ''',
        color=discord.Color.blurple()
    )
        await message.channel.send(embed=embed)
 
 

  
    elif message.content.lower().startswith(("what are the good xtals for 2hs","good crysta for 2hs","good xtal for 2hs","xtal for 2hs","crystals for 2hs","crysta for 2hs","2hs xtal")):
        embed = discord.Embed(
            title='Recommended Crysta',
            description='''
1.For Weapon
  a)Don Profundo
  b)Devil Dango
  c)Hexter
  d)Vlam the Flame Dragon
  
2.For Armour
  a)Altadar
  b)Sibylares
  c)Bangrudom
  d)Torexesa

3.For Add
  a)Jibril III
  b)Alfenix
  c)Evil Lefina
  d)Gordo
  
4.For Ring
  a)Torexesa
  b)Dominaredor
  c)Etoise
  d)Stellar Ooze II
  e)Red Ash Dragon Rudis
  f)Sicanokami
  g)Trus
        ''',
        color=discord.Color.blurple()
    )
        await message.channel.send(embed=embed)
 
    
    elif message.content.lower().startswith(("what are the good xtals for bow","good crysta for bow","good xtal for bow","xtal for bow","crystals for bow","crysta for bow","bow xtal")):
        embed = discord.Embed(
            title='Recommended Crysta',
            description='''
1.For Weapon
  a)Trickstar Dragon Mimyugon
  b)Doridodi
  c)Devil dango
  d)Pedrio
  
2.For Armour
  a)Altadar
  b)Zapo
  c)Grim Reaper Scarecrow
  d)Sibylares
  e)Ageladanios
  f)Charugon

3.For Add
  a)Prudent Blue Shadow
  b)Falburrows
  c)Evil Lefina
  d)Alfenix
  f)Dark lord
  
4.For Ring
  a)Torexesa
  b)Broker Goblin
  c)Dominaredor
  d)Red Ash Dragon Rudis
  e)Sicanokami
        ''',
        color=discord.Color.blurple()
    )
        await message.channel.send(embed=embed)
  
    
    elif message.content.lower().startswith(("what are the good xtals for mage","good crysta for mage","good xtal for mage","xtal for mage","crystals for mage","crysta for mage","mage xtal")):
        embed = discord.Embed(
            title='Recommended Crysta',
            description='''
1.For Weapon
  a)Armasite
  b)Irestida
  c)Oculasignio
  d)Pedrio
  f)Finstern The Dark Dragon
  g)Mozoto Machina
  h)Kuzto
  i)Diark
  
2.For Armour
  a)Iron Empress
  b)Black Velly
  c)Dr Leonardo II
  d)sibylares
  e)Underwater Ruins Monster
  f)Altadar
  g)Evil Shadow
  i)Gegner

3.For Add
  a)Mage Filecia
  b)Garnache
  c)Narumi Hina
  d)Mieli
  f)Jibril
  g)Jiva
  
4.For Ring
  a)Star Wizard
  b)Seele Zauga
  c)Dominaredor
  d)Black Shadow
  e)Seele Zauga II
  f)Broker Goblin
  g)Charugon
  h)Scream shadow
  i)Torexesa
        ''',
        color=discord.Color.blurple()
    )
        await message.channel.send(embed=embed)

    elif message.content.lower().startswith(("what are the good xtals for tank","good crysta for tank","good xtal for tank","xtal for tank","crystals for tank","crysta for tank","tank xtal")):
        embed = discord.Embed(
            title='Recommended Crysta',
            description='''
1.For Weapon
  a)Hero Potum III
  b)Rhinasour
  c)Blood Smeared Crystal
  
2.For Armour
  a)Rhinasour
  b)Filrocas
  c)Iron Empress

3.For Add
  a)Gordo
  b)Amargon
  c)Candela II
  D)Dusk Machina
    
4.For Ring
  a)Etoise
  b)Broker Goblin
        ''',
        color=discord.Color.blurple()
    )
        await message.channel.send(embed=embed)
    
    elif message.content.lower().startswith(("what are the good xtals for helb","good crysta for helb","good xtal for helb","xtal for helb","crystals for helb","crysta for helb","helb xtal")):
        embed = discord.Embed(
            title='Recommended Crysta',
            description='''
1.For Weapon
  a)Devil dango
  b)
  
2.For Armour
  a)Usamochi
  b)Dx Fighter II

3.For Add
  a)Evil Lafina
  b)Royal ox king
    
4.For Ring
  a)Red ash dragon Rudis
  b)Sicanokami
        ''',
        color=discord.Color.blurple()
    )
        await message.channel.send(embed=embed)
    
    elif message.content.lower().startswith(("what are the good xtals for katana","good crysta for ktn","good xtal for ktn","xtal for ktn","crystals for ktn","crysta for ktn","katana xtal","ktn xtal","crystals for katana")):
        embed = discord.Embed(
            title='Recommended Crysta',
            description='''
1.For Weapon
  a)Devil dango
  b)Don Profundo
  c)Lilicarolla
  
2.For Armour
  a)Altadar
  b)Lilicarolla
  c)Usamochi
  d)Sibylares

3.For Add
  a)Gordo
  b)Lilicarolla
  c)Prudent Blue Shadow
  d)Evil lefina
    
4.For Ring
  a)Stellar Ooze II
  b)Etoise
  c)Lilicarolla
  d)Spectar Of Death
  e)Aubergine Dragon Auvio
        ''',
        color=discord.Color.blurple()
    )
        await message.channel.send(embed=embed)
    
    elif message.content.lower().startswith(("info Don Profundo","info don pro","info profundo")):
        embed = discord.Embed(
            title='Don Profundo [Enhancer Crysta (Red)]',
            description='''
================================
Stat/Effect              Ammount
STR %                    7
ATK %                    10
DEF %                   -27
Critical Rate %          8
================================
Upgrade for Hexter
================================
Obtained From :
Don Profundo
Abandoned District: Ruins Summit
=================================

        ''',
        color=discord.Color.blurple()
    )
        await message.channel.send(embed=embed)
        
    elif message.content.lower().startswith(("info Devil Dango","info devil","info dango")):
        embed = discord.Embed(
            title='Devil Dango [Weapon Crysta]',
            description='''
================================
Stat/Effect              Ammount
MaxMP                   -200
ATK %                    4
Physical Pierce %        20
Ailment Resistance %    -15
Aggro %                 -10
================================
Obtained From :
Devil Dango
Otsukimi Event Venue: Crater Zone
=================================
        ''',
        color=discord.Color.blurple()
    )
        await message.channel.send(embed=embed)
        
    elif message.content.lower().startswith(("info Hexter")):
        embed = discord.Embed(
            title='Hexter [Enhancer Crysta (Red)]',
            description='''
================================
Stat/Effect               Amount
STR %                     6
ATK %                     8
DEF %                    -21
Critical Rate %           6
================================
Upgrade for Gwaimol
================================
Obtained From :
Hexter
Witch's Woods Depths
=================================
Used For Don Profundo
=================================
        ''',
        color=discord.Color.blurple()
    )
        await message.channel.send(embed=embed)
        
    elif message.content.lower().startswith(("info Vlam the Flame Dragon","info vlam","info dragon")):
        embed = discord.Embed(
            title='Vlam the Flame Dragon [Enhancer Crysta (Red)]',
            description='''
================================
Stat/Effect               Amount
MaxMP                     400
Physical Pierce %         7
Short Range Damage %      6
================================
Upgrade for Ultimate Machina
================================
Obtained From :
Vlam the Flame Dragon
Divido Spring
=================================

        ''',
        color=discord.Color.blurple()
    )
        await message.channel.send(embed=embed)
        
    elif message.content.lower().startswith(("info doctor pom pom","info pom pom","info doctor")):
        embed = discord.Embed(
            title='Doctor Pom Pom [Armor Crysta]',
            description='''
================================
Stat/Effect               Amount
Critical Rate %           7
Ailment Resistance %      7
Short Range Damage %      7
================================
Obtained From :
Hero Potum Party
Archfiend's Throne
(Million download event)
=================================

        ''',
        color=discord.Color.blurple()
    )
        await message.channel.send(embed=embed)
        
    elif message.content.lower().startswith(("info Trickster Dragon Mimyugon","info Trickster","info Dragon")):
        embed = discord.Embed(
            title='Trickster Dragon Mimyugon [Enhancer Crysta (Red)]',
            description='''
================================
Stat/Effect               Amount
DEX %                     7
ATK %                     9
ASPD %                    5
================================
Upgrade for Vulture
================================
Obtained From :
Trickster Dragon Mimyugon
Operation Zone: Cockpit Area
=================================
        ''',
        color=discord.Color.blurple()
    )
        await message.channel.send(embed=embed)
        
    elif message.content.lower().startswith(("info Altadar")):
        embed = discord.Embed(
            title='Altadar [Armor Crysta]',
            description='''
================================
Stat/Effect               Amount
STR %                     6
VIT %                     6
Stability %               11
--------------------------------
Heavy Armor only:
Long Range Damage %       11
Stability %               -5
--------------------------------
Light Armor only:
Short Range Damage %      11
Stability %               -5
================================
Obtained From
Altadar
High Difficulty Boss Battle 
Event Venue
=================================
        ''',
        color=discord.Color.blurple()
    )
        await message.channel.send(embed=embed)
        
    elif message.content.lower().startswith(("info lilicarolla","info lili")):
        embed = discord.Embed(
            title='Lilicarolla [Enhancer Crysta (Blue)]',
            description='''
=================================
Stat/Effect                Amount
MaxMP                     -100
Dodge %                   -5
Unsheathe Attack %         18
Upgrade for Tappler
=================================
Obtained From
Lilicarolla
Frozen Falls: Area 1
=================================
        ''',
        color=discord.Color.blurple()
    )
        await message.channel.send(embed=embed)
        
    elif message.content.lower().startswith(("info Sibylares","info Siby")):
        embed = discord.Embed(
            title='Sibylares [Armor Crysta]',
            description='''
=================================
Stat/Effect                Amount
MaxMP                     -100
ATK %                      5
MATK %                     5
Physical Pierce %          5
Magic Pierce %             5
Critical Rate              15
=================================
Obtained From
Sibylares
Phasma Forest: Area 3
=================================
        ''',
        color=discord.Color.blurple()
    )
        await message.channel.send(embed=embed)
        
    elif message.content.lower().startswith(("info Bangrudom","info Bang")):
        embed = discord.Embed(
            title='Bangrudom [Armor Crysta]',
            description='''
=================================
Stat/Effect                Amount
MaxHP %                   -20
ATK %                      10
MATK %                     10
ASPD %                     10
CSPD %                     10
---------------------------------
Shield only:
DEX %                      5
---------------------------------
Light Armor only:
Magic Pierce %             5
=================================
Obtained From
Bangrudom 
El Scaro: Back Alley 
=================================
        ''',
        color=discord.Color.blurple()
    )
        await message.channel.send(embed=embed)
        
    elif message.content.lower().startswith(("info Sicanokami","info Sica")):
        embed = discord.Embed(
            title='Sicanokami [Enhancer Crysta (Purple)]',
            description='''
=================================
Stat/Effect                Amount
Accuracy                   50
Attack MP Recovery         20
Short Range Damage %       5
---------------------------------
Halberd only:
Long Range Damage %
5
=================================
Upgrade for Patissia
=================================
Obtained From
Sicanokami
El Scaro: Back Alley
=================================
        ''',
        color=discord.Color.blurple()
    )
        await message.channel.send(embed=embed)
        
    elif message.content.lower().startswith(("info Torexesa","info Torex")):
        embed = discord.Embed(
            title='Torexesa [Enhancer Crysta (Blue)]',
            description='''
=================================
Stat/Effect                Amount
MaxMP                     -200
ATK %                      10
MATK %                     10
Attack MP Recovery          4
=================================
Upgrade for
Black Shadow
=================================
Obtained From
Torexesa 
Aquacity: Parliament Hall
=================================
        ''',
        color=discord.Color.blurple()
    )
        await message.channel.send(embed=embed)
        
    elif message.content.lower().startswith(("info Aubergine Dragon Auvio","info Auvio","info Dragon")):
        embed = discord.Embed(
            title='Aubergine Dragon Auvio [Special Crysta]',
            description='''
=================================
Stat/Effect                Amount
MaxMP                      300
ASPD                       500
Short Range Damage %       4
Long Range Damage %        -12
---------------------------------
Ninjutsu Scroll only:
Critical Rate                5
Unsheathe Attack %           5
=================================
Obtained From
Aubergine Dragon Auvio 
Rakau Plains (Event)
=================================
        ''',
        color=discord.Color.blurple()
    )
        await message.channel.send(embed=embed)
        
    elif message.content.lower().startswith(("info ageladanios","info agel")):
        embed = discord.Embed(
            title='Ageladanios [Enhancer Crysta (Blue)]',
            description='''
=================================
Stat/Effect                Amount
ATK %                      6
Magic Resistance %        -15
Critical Damage            8
Motion Speed %            -1
=================================
Upgrade for
Lyark Master Specialist
=================================
Obtained From
Ageladanios
Ducia Coast: Area 1
=================================
Used for Wiltileaf
=================================
        ''',
        color=discord.Color.blurple()
    )
        await message.channel.send(embed=embed)
        
    elif message.content.lower().startswith(("info Wiltileaf","info Wilti")):
        embed = discord.Embed(
            title='Wiltileaf [Enhancer Crysta (Blue)]',
            description='''
=================================
Stat/Effect                Amount
ATK %                        9
Magic Resistance %         -15
Critical Damage              12
Motion Speed %               0
=================================
Upgrade for
Ageladanios
=================================
Obtained From
Wiltileaf
Eumano Village Ruins: Area 2
=================================
        ''',
        color=discord.Color.blurple()
    )
        await message.channel.send(embed=embed)
        
    elif message.content.lower().startswith(("info Charugon")):
        embed = discord.Embed(
            title='Charugon [Enhancer Crysta (Blue)]',
            description='''
=================================
Stat/Effect                Amount
STR                         6
Magic Resistance %        -12
Short Range Damage %        3
Long Range Damage %         6
=================================
Upgrade for
Flare Volg
=================================
Obtained From
Charugon 
Boma Konda: Underground Area
=================================
        ''',
        color=discord.Color.blurple()
    )
        await message.channel.send(embed=embed)
        
    elif message.content.lower().startswith(("info Alfenix")):
        embed = discord.Embed(
            title='Alfenix [Enhancer Crysta (Yellow)]',
            description='''
=================================
Stat/Effect                Amount
MaxHP %                     18
ATK %                        3
Physical Pierce %           10
Aggro %                    -15
=================================
Upgrade for
Handmade Cookie
=================================
Obtained From
Alfenix
El Scaro
=================================
        ''',
        color=discord.Color.blurple()
    )
        await message.channel.send(embed=embed)
        
    elif message.content.lower().startswith(("info dark lord","info dark")):
        embed = discord.Embed(
            title='†Dark Lord† [Enhancer Crysta (Yellow)]',
            description='''
=================================
Stat/Effect                Amount
ATK %                        5
ASPD %                      20
Aggro %                    -10
Short Range Damage %         3
=================================
Upgrade for
Yashiro Azuki's Dad
=================================
Obtained From
†Dark Lord†
Event
=================================
        ''',
        color=discord.Color.blurple()
    )
        await message.channel.send(embed=embed)
        
    elif message.content.lower().startswith(("info Gordo")):
        embed = discord.Embed(
            title='Gordo [Enhancer Crysta (Yellow)]',
            description='''
=================================
Stat/Effect                Amount
ATK %                        7
ASPD %                      80
Long Range Damage %        -15
=================================
Upgrade for
Wandering Wheel
=================================
Obtained From
Gordo
Eumano Glade
=================================
        ''',
        color=discord.Color.blurple()
    )
        await message.channel.send(embed=embed)
        
    elif message.content.lower().startswith(("info Evil Lefina")):
        embed = discord.Embed(
            title='Evil Lefina [Additional Crysta]',
            description='''
=================================
Stat/Effect                Amount
ATK %                        8
MATK %                      -4
Physical Pierce %           10
Physical Resistance %      -20
Critical Rate               12
---------------------------------
Heavy Armor only:
Physical Resistance %        24
=================================
Obtained From
Evil Lefina 
El Scaro
=================================
        ''',
        color=discord.Color.blurple()
    )
        await message.channel.send(embed=embed)
        
    elif message.content.lower().startswith(("info Jibril III","info Jibril")):
        embed = discord.Embed(
            title='Jibril III [Enhancer Crysta (Yellow)]',
            description='''
=================================
Stat/Effect                Amount
Natural MP Regen             6
Natural MP Regen %          12
MaxMP                      100
Critical Rate               16
Short Range Damage %         9
Long Range Damage %         11
Anticipate %                 3
=================================
Upgrade for
Jibril II
=================================
Obtained From
Event Collab
No game no life 
=================================
        ''',
        color=discord.Color.blurple()
    )
        await message.channel.send(embed=embed)
        
    elif message.content.lower().startswith(("info Armasite")):
        embed = discord.Embed(
            title='Armasite [Weapon Crysta]',
            description='''
=================================
Stat/Effect                Amount
MATK %                       5
Magic Pierce %              20
CSPD %                      -15
=================================
Obtained From
Armasite 
Fractum Sector: Area 1
=================================
        ''',
        color=discord.Color.blurple()
    )
        await message.channel.send(embed=embed)
        
    elif message.content.lower().startswith(("info irestida")):
        embed = discord.Embed(
            title='Irestida [Enhancer Crysta (Red)]',
            description='''
=================================
Stat/Effect                Amount
MATK %                       8
Magic Pierce %               6
MDEF %                     -24
Aggro %                     -9
=================================
Upgrade for
Shampy
=================================
Obtained From
Irestida
Nov Diela Central
=================================
        ''',
        color=discord.Color.blurple()
    )
        await message.channel.send(embed=embed)
        
    elif message.content.lower().startswith(("info oculasignio","info ocul")):
        embed = discord.Embed(
            title='Oculasignio [Enhancer Crysta (Red)]',
            description='''
=================================
Stat/Effect                Amount
MaxMP                      300
MATK %                       9
Guard Break %              13
=================================
Upgrade for
Finstern the Dark Dragon
=================================
Obtained From
Oculasignio
Mt. Vulcani: Summit
=================================
        ''',
        color=discord.Color.blurple()
    )
        await message.channel.send(embed=embed)
        
    elif message.content.lower().startswith(("info Finstern The Dark Dragon","info Finstern","info Dragon")):
        embed = discord.Embed(
            title='Finstern the Dark Dragon [Enhancer Crysta (Red)]',
            description='''
=================================
Stat/Effect                Amount
MaxMP                      300
MATK %                       7
Guard Break %              12
=================================
Upgrade for
Imitacia
=================================
Obtained From
Finstern the Dark Dragon 
Dark Dragon Shrine: Near the Top
=================================
        ''',
        color=discord.Color.blurple()
    )
        await message.channel.send(embed=embed)
        
    elif message.content.lower().startswith(("info Mozto Machina","info Mozto")):
        embed = discord.Embed(
            title='Mozto Machina [Enhancer Crysta (Red)]',
            description='''
=================================
Stat/Effect                Amount
DEX %                        4
MATK %                       6
CSPD %                       2
=================================
Upgrade for
Demon's Gate
=================================
Obtained From
Large Demi Machina Factory: 
(Deepest Part)
=================================
        ''',
        color=discord.Color.blurple()
    )
        await message.channel.send(embed=embed)
        
    elif message.content.lower().startswith(("info Iron Empress","info Iron")):
        embed = discord.Embed(
            title='Iron Empress [Armor Crysta]',
            description='''
=================================
Stat/Effect                Amount
MaxHP %                     20
MaxMP                      -300
MATK %                       5
Magic Pierce %              10
Physical Resistance %       10
CSPD %                      20
=================================
Obtained From
Ancient Empress Mezzaluna (Hell)
Event
=================================
        ''',
        color=discord.Color.blurple()
    )
        await message.channel.send(embed=embed)
        
    elif message.content.lower().startswith(("info Black Velly")):
        embed = discord.Embed(
            title='Black Velly [Enhancer Crysta (Green)]',
            description='''
=================================
Stat/Effect                Amount
MaxHP                     3000
MaxMP                      400
MATK %                       9
Evasion Recharge %         -20
=================================
Upgrade for
Evil Shadow
=================================
Obtained From
Illuminare City: Central Square
xmas event
=================================
        ''',
        color=discord.Color.blurple()
    )
        await message.channel.send(embed=embed)
        
    elif message.content.lower().startswith(("info Dr Leonardo","info Leonardo","info dr Leo")):
        embed = discord.Embed(
            title='Dr. Leonardo II [Enhancer Crysta (Green)]',
            description='''
=================================
Stat/Effect                Amount
MaxHP                     6000
MATK %                       3
Critical Rate %             20
Ailment Resistance %         5
Long Range Damage %          6
=================================
Upgrade for
Dr. Leonardo
=================================
Obtained From
Eagle Talon Collab Venue
=================================
        ''',
        color=discord.Color.blurple()
    )
        await message.channel.send(embed=embed)
        
    elif message.content.lower().startswith(("info Underwater Ruins Monster","info Underwater","info URM")):
        embed = discord.Embed(
            title='Underwater Ruins Monster[Enhancer Crysta(Yellow)]',
            description='''
=================================
Stat/Effect                Amount
MaxHP                     1000
MATK %                       8
Critical Damage              8
=================================
Upgrade for
Adaro
=================================
Heavy Armor only:
Aggro %                     20
=================================
Obtained From
Underwater Ruins: Deepest
Adaro (High Difficulty)
=================================
        ''',
        color=discord.Color.blurple()
    )
        await message.channel.send(embed=embed)
        
    elif message.content.lower().startswith(("info Narumi Hina","info Narumi")):
        embed = discord.Embed(
            title='Narumi Hina [Additional Crysta]',
            description='''
=================================
Stat/Effect                Amount
MATK %                       4
CSPD %                      20
Aggro %                    -10
Long Range Damage %          3
=================================
Obtained From
Event Yashiro azuki collab
=================================
        ''',
        color=discord.Color.blurple()
    )
        await message.channel.send(embed=embed)
        
    elif message.content.lower().startswith(("info seele")):
        embed = discord.Embed(
            title='Seele Zauga [Special Crysta]',
            description='''
=================================
Stat/Effect                Amount
Physical Resistance %        5
Magic Resistance %           5
Critical Rate               15
Item Cooldown              -1
=================================
Obtained From
Shrine of the Goddess of Species
=================================
        ''',
        color=discord.Color.blurple()
    )
        await message.channel.send(embed=embed)
        
    elif message.content.lower().startswith(("info star wiz","info star wizard")):
        embed = discord.Embed(
            title='Star Wizard [Special Crysta]',
            description='''
=================================
Stat/Effect                Amount
MATK %                       9
CSPD %                       9
Anticipate %                 9
---------------------------------
Shield only:
Aggro %                      9
Staff only:
Aggro %                     -9
=================================
Upgrade for
(To be specified)
=================================
Obtained From
(To be specified)
=================================
        ''',
        color=discord.Color.blurple()
    )
        await message.channel.send(embed=embed)
    elif message.content.lower().startswith(("info Black Shadow","info BS")):
        embed = discord.Embed(
            title='Black Shadow [Enhancer Crysta (Blue)]',
            description='''
=================================
Stat/Effect                Amount
MaxMP                      -150
ATK %                        8
MATK %                       8
Attack MP Recovery           3
=================================
Upgrade for
Tuscog
=================================
Obtained From
Rokoko City Ruins
=================================

        ''',
        color=discord.Color.blurple()
    )
        await message.channel.send(embed=embed)
    elif message.content.lower().startswith(("info diark","diark")):
        embed = discord.Embed(
            title='Diark [Enhancer Crysta (Red)]',
            description='''
=================================
Stat/Effect                Amount
MATK %                       8
Magic Pierce %              20
CSPD %                     -16
=================================
Upgrade for
(To be specified)
=================================
Obtained From
(To be specified)
=================================
        ''',
        color=discord.Color.blurple()
    )
        await message.channel.send(embed=embed)
    elif message.content.lower().startswith(("info Gegner","gener")):
        embed = discord.Embed(
            title='Gegner [Enhancer Crysta (Green)]',
            description='''
=================================
Stat/Effect                Amount
INT %                        6
MATK %                      10
CSPD %                      40
Attack MP Recovery %       10
=================================
Obtained From
(To be specified)
=================================

        ''',
        color=discord.Color.blurple()
    )
        await message.channel.send(embed=embed)
    elif message.content.lower().startswith(("info Evil Shadow")):
        embed = discord.Embed(
            title='Evil Shadow [Armor Crysta]',
            description='''
=================================
Stat/Effect                Amount
MaxHP                     1500
MaxMP                      300
MATK %                       6
Evasion Recharge %        -10
=================================
Used for
Black Velly
=================================
Obtained From
Reindeer Forest
Xmass event
=================================
        ''',
        color=discord.Color.blurple()
    )
        await message.channel.send(embed=embed)
    elif message.content.lower().startswith(("info jiva")):
        embed = discord.Embed(
            title='Jiva [Enhancer Crysta (Yellow)]',
            description='''
=================================
Stat/Effect                Amount
DEX %                        3
MATK %                       8
Accuracy %                 -20
Critical Damage              6
=================================
Obtained From
(To be specified)
=================================
        ''',
        color=discord.Color.blurple()
    )
        await message.channel.send(embed=embed)
    elif message.content.lower().startswith(("info scream shadow","info scream")):
        embed = discord.Embed(
            title='Scream Shadow [Special Crysta]',
            description='''
=================================
Stat/Effect                Amount
MaxMP                      300
DEF %                      -40
CSPD                      1000
Critical Rate %            20
=================================
Upgrade for
(To be specified)
=================================
Obtained From
(To be specified)
=================================
        ''',
        color=discord.Color.blurple()
    )
        await message.channel.send(embed=embed)
    elif message.content.lower().startswith(("info Gordo","info gordo")):
        embed = discord.Embed(
            title='Gordo [Enhancer Crysta (Yellow)]',
            description='''
=================================
Stat/Effect                Amount
ATK %                        7
ASPD %                      80
Long Range Damage %        -15
=================================
Upgrade for
Wandering Wheel
=================================
Obtained From
Eumano Glade
=================================
        ''',
        color=discord.Color.blurple()
    )
        await message.channel.send(embed=embed)
    elif message.content.lower().startswith(("info amargon","info amar")):
        embed = discord.Embed(
            title='Amargon [Enhancer Crysta (Yellow)]',
            description='''
=================================
Stat/Effect                Amount
MaxHP %                     30
MaxMP                     -300
ASPD                       800
=================================
Upgrade for
Candela II
=================================
Obtained From
El Scaro: Back Alley
=================================
        ''',
        color=discord.Color.blurple()
    )
        await message.channel.send(embed=embed)
    elif message.content.lower().startswith(("info rhinosaur","info rhino")):
        embed = discord.Embed(
            title='Rhinosaur [Enhancer Crysta (Blue)]',
            description='''
=================================
Stat/Effect                Amount
MaxHP %                     10
ATK %                        5
ASPD %                      15
=================================
Upgrade for
Minotaur
=================================
Obtained From
Fugitive Lake Swamp: Area 3
=================================
        ''',
        color=discord.Color.blurple()
    )
        await message.channel.send(embed=embed)
    elif message.content.lower().startswith(("info hero potum III")):
        embed = discord.Embed(
            title='Hero Potum III [Enhancer Crysta (Red)]',
            description='''
=================================
Stat/Effect                Amount
MaxHP %                     12
Accuracy %                  16
Aggro %                     18
Fractional Barrier %        14
=================================
Upgrade for
Hero Potum II
=================================
Obtained From
Archfiend's Throne
million download event
=================================
        ''',
        color=discord.Color.blurple()
    )
        await message.channel.send(embed=embed)
    elif message.content.lower().startswith(("info filrocas")):
        embed = discord.Embed(
            title='Filrocas [Enhancer Crysta (Green)]',
            description='''
=================================
Stat/Effect                Amount
MaxHP %                     60
Physical Resistance %       -7
Magic Resistance %          -7
=================================
Upgrade for
Eroded Pilz
---------------------------------
Knuckle only:
Aggro %                     15
1-Handed Sword only:
Aggro %                     15
=================================
Obtained From
Royal Dragon Cocoon Chamber
=================================
        ''',
        color=discord.Color.blurple()
    )
        await message.channel.send(embed=embed)
    elif message.content.lower().startswith(("info Prudent Blue Shadow","info prudent")):
        embed = discord.Embed(
            title='Prudent Blue Shadow [Enhancer Crysta (Yellow)]',
            description='''
=================================
Stat/Effect                Amount
MaxMP                     -150
Short Range Damage %         8
Long Range Damage %          8
Unsheathe Attack %           8
=================================
Upgrade for
Baphomela
=================================
Obtained From
Noeliel Castle: B4F
Dutannen (Max)
=================================

        ''',
        color=discord.Color.blurple()
    )
        await message.channel.send(embed=embed)
    elif message.content.lower().startswith(("info Blood Smeared Crystal","info blood","info smeared")):
        embed = discord.Embed(
            title='Blood Smeared Crystal [Enhancer Crysta (Red)]',
            description='''
=================================
Stat/Effect                Amount
Critical Damage              6
Aggro %                     10
Attack MP Recovery           7
=================================
Upgrade for
Evil Magic Sword
=================================
Obtained From
Avant Plastida: Area 1
Bloodie Crystal (Lv 207)
=================================

        ''',
        color=discord.Color.blurple()
    )
        await message.channel.send(embed=embed)
    elif message.content.lower().startswith(("info Torexesa","info torex")):
        embed = discord.Embed(
            title='Torexesa [Enhancer Crysta (Blue)]',
            description='''
=================================
Stat/Effect                Amount
MaxMP                     -200
ATK %                      10
MATK %                     10
Attack MP Recovery          4
=================================
Upgrade for
Black Shadow
=================================
Obtained From
Aquacity: Parliament Hall
=================================

        ''',
        color=discord.Color.blurple()
    )
        await message.channel.send(embed=embed)
    elif message.content.lower().startswith(("info Dominaredor","info domi","info dominar")):
        embed = discord.Embed(
            title='Dominaredor [Enhancer Crysta (Purple)]',
            description='''
=================================
Stat/Effect                Amount
ATK %                        8
MATK %                       8
ASPD %                      20
=================================
Upgrade for
Lalvada
---------------------------------
Reduce Dmg (Floor) %        20
=================================
Obtained From
Frozen Falls: Depths
=================================

        ''',
        color=discord.Color.blurple()
    )
        await message.channel.send(embed=embed)
    elif message.content.lower().startswith(("info Etoise")):
        embed = discord.Embed(
            title='Etoise [Enhancer Crysta (Purple)]',
            description='''
=================================
Stat/Effect                Amount
ASPD                      1100
CSPD %                     -70
Critical Rate %            40
Motion Speed %              5
=================================
Upgrade for
Volgagon
=================================
Obtained From
High Difficulty Boss Battle 
Event Venue
Etoise
=================================

        ''',
        color=discord.Color.blurple()
    )
        await message.channel.send(embed=embed)
    elif message.content.lower().startswith(("info Stellar Ooze II","info stellar")):
        embed = discord.Embed(
            title='Stellar Ooze II [Special Crysta]',
            description='''
=================================
Stat/Effect                Amount
Natural MP Regen %         15
MaxMP                      150
ATK %                       5
Physical Pierce %           5
Revive Time %              60
Unsheathe Attack %          5
---------------------------------
Reduce Dmg (Bowling) %     15
=================================
Obtained From
Stellar Ooze (Hell) (Lv 270)
Event
=================================
        ''',
        color=discord.Color.blurple()
    )
        await message.channel.send(embed=embed)
    elif message.content.lower().startswith(("info Red Ash Dragon Rudis","info red ash")):
        embed = discord.Embed(
            title='Red Ash Dragon Rudis [Enhancer Crysta (Blue)]',
            description='''
=================================
Stat/Effect                Amount
MaxHP                     -300
MaxMP                      200
Accuracy %                  5
Critical Rate              -7
Short Range Damage %        9
=================================
Upgrade for
Gravicep
=================================
Obtained From
Espuma Dome: Entrance
=================================

        ''',
        color=discord.Color.blurple()
    )
        await message.channel.send(embed=embed)
        
    elif message.content.lower().startswith(("info Trus","info trus")):
        embed = discord.Embed(
            title='Trus [Special Crysta]',
            description='''
=================================
Stat/Effect                Amount
Physical Pierce %           10
Guard Break %               10
Stun Unavailable             1
---------------------------------
2-Handed Sword only:
Guard Power %               25
Guard Recharge %            25
=================================
Upgrade for
(To be specified)
=================================
Obtained From
Propulsion System Zone: Power Tank
=================================

        ''',
        color=discord.Color.blurple()
    )
        await message.channel.send(embed=embed)
    elif message.content.lower().startswith(("info DX Fighter II")):
        embed = discord.Embed(
            title='DX Fighter II [Enhancer Crysta (Green)]',
            description='''
=================================
Stat/Effect                Amount
MaxHP                     6000
ATK %                        3
Accuracy %                  15
Short Range Damage %         6
Fractional Barrier %         5
=================================
Upgrade for
DX Fighter
=================================
Obtained From
Eagle Talon Collab Venue
=================================

        ''',
        color=discord.Color.blurple()
    )
        await message.channel.send(embed=embed)
    elif message.content.lower().startswith(("info baavgai")):
        embed = discord.Embed(
            title='Baavgai [Enhancer Crysta (Green)]',
            description='''
=================================
Stat/Effect                Amount
MaxHP                     7000
Critical Damage              7
Short Range Damage %         5
=================================
Upgrade for
Dreamy Scarlet Sakura
=================================
Obtained From
Mt. Sakuraten: Summit
=================================

        ''',
        color=discord.Color.blurple()
    )
        await message.channel.send(embed=embed)
    elif message.content.lower().startswith(("info zapo")):
        embed = discord.Embed(
            title='Zapo [Enhancer Crysta (Green)]',
            description='''
=================================
Stat/Effect                Amount
MaxHP                     -400
MaxMP                     -400
ATK %                       10
Critical Rate               10
=================================
Upgrade for
Arachnidemon
---------------------------------
Shield only:
STR %                        1
Short Range Damage %         5
=================================
Obtained From
Puerta Islands: Adit
=================================

        ''',
        color=discord.Color.blurple()
    )
        await message.channel.send(embed=embed)
    

    
         

async def handle_builds(message, check):
    build_embed = discord.Embed(
        title='Builds',
        description='Choose a build category:(type build number from the list only)',
        color=discord.Color.green()
    )
    build_embed.add_field(name='1. 0HS Tank', value='Information on 0HS Tank build.', inline=False)
    build_embed.add_field(name='2. 0HS DPS', value='Information on 0HS DPS build.', inline=False)
    build_embed.add_field(name='3. 2HS', value='Information on 2HS build.', inline=False)
    build_embed.add_field(name='4. Bow', value='Information on Bow build.', inline=False)
    build_embed.add_field(name='5. BWG', value='Information on BWG build.', inline=False)
    build_embed.add_field(name='6. KTN', value='Information on KTN build.', inline=False)
    build_embed.add_field(name='7. HB', value='Information on HB build.', inline=False)
    build_embed.add_field(name='8. KNX Tank', value='Information on KNX Tank build.', inline=False)
    build_embed.add_field(name='9. KNX DPS', value='Information on KNX DPS build.', inline=False)
    build_embed.add_field(name='10. Barehand', value='Information on Barehand build.', inline=False)
    build_embed.add_field(name='11. Support', value='Information on Support build.', inline=False)

    await message.channel.send(embed=build_embed)

    try:
        build_response = await bot.wait_for('message', check=check, timeout=30.0)

        build_info = {
            '1': "Here's information on 0HS Tank build: https://youtu.be/M03qVi9_vdI?si=suIdBXH8ckJaGcPT",
            '2': "Here's information on 0HS DPS build: https://youtu.be/h_ZvZluqJi4?si=ih9B7oM8-df0ilRa",
            '3': "Here's information on 2HS build: https://youtu.be/Ig0wwr15Ysc?si=VGHA1M3HQ0RLysP2",
            '4': "Here's information on Bow build: https://youtu.be/aVQRczWLieE?si=3L0wJZb7z7oEzZIN",
            '5': "Here's information on BWG build: https://youtu.be/mqOQy_gUd6s?si=s59CO6iJyBQLZH_i",
            '6': "Here's information on KTN build: https://youtu.be/GkKh8mr5Jz4?si=ez9sYm1t6hBC-1-X",
            '7': "Here's information on HB build: https://youtu.be/OANNpTI_w3w?si=yEK7cXksdeT_9ma9",
            '8': "Here's information on KNX Tank build: https://youtu.be/NlqC8QSREN0?si=6M2TQpH5A-tsMt8j",
            '9': "Here's information on KNX DPS build: https://youtu.be/4AcqxRXtWns?si=Z2X7D4n3BjN6Kbj9",
            '10': "Here's information on Barehand build: https://youtu.be/yD5_ahA980I?si=XSATYm4iq6nG13-r",
            '11': "Here's information on Support build: https://youtu.be/-uqsK4f2LSU?si=MZ7_is8vP6Ny3RiB"
        }

        response_text = build_info.get(build_response.content.lower(), "Please provide the number from the list to see the build info. Try again.")
        await message.channel.send(response_text)
    except asyncio.TimeoutError:
        await message.channel.send("You took too long to choose a build.")

async def handle_blacksmithing(message, check):
    blacksmith_embed = discord.Embed(
        title='Blacksmithing',
        description='Choose a blacksmithing category:',
        color=discord.Color.orange()
    )
    blacksmith_embed.add_field(name='1. Crafting', value='Crafting in the game involves creating weapons from materials. Player-crafted equipment emphasizes ATK, stability, and DEF stats. Rather than predefined stats, items feature potential points that can be converted into statistics (refer to section C). To engage in crafting, players require the \'Create Equipment\' EX Skill, which unlocks the crafting menu. Advancing this skill enhances crafting success rates. Notably, skills such as \'Careful Creation\' and \'Expert\'s Creation,\' when maxed at level 10, increase an item\'s potential by 10% (rounded down).', inline=False)
    blacksmith_embed.add_field(name='2. Refine', value='Refining in the game strengthens weapons or armor. Each +N refine for weapons increases damage by N^2% and adds +N bonus attack. For armor, additional gear, and shields, each refine reduces damage taken by 1%. For example, refining a weapon with 100 base attack to +6 results in +(6^2% × 100) and +6 bonus attack, totaling 142 attack power.', inline=False)
    blacksmith_embed.add_field(name='3. Statting', value='Statting in the game converts potential points into stat points for player-crafted equipment, with up to 8 customizable stat slots and limits based on character level, total Customization skill levels, and stat caps.', inline=False)
    blacksmith_embed.add_field(name='4. Enhancement', value='Information on enhancements', inline=False)
    await message.channel.send(embed=blacksmith_embed)

    try:
        blacksmith_response = await bot.wait_for('message', check=check, timeout=15.0)

        if blacksmith_response.content.lower() == '1' or blacksmith_response.content.lower() == 'crafting':
            await handle_crafting(message, check)
        elif blacksmith_response.content.lower() == '2' or blacksmith_response.content.lower() == 'refine':
            await handle_refine(message, check)
        elif blacksmith_response.content.lower() == '3' or blacksmith_response.content.lower() == 'statting':
            await message.channel.send("The statting section is currently under development. Please check back later.")
        elif blacksmith_response.content.lower() == '4' or blacksmith_response.content.lower() == 'enhancement':
            await message.channel.send("The enhancement section is currently under development. Please check back later.")
        else:
            await message.channel.send("Invalid choice. Please choose a valid option from 1 to 4.")
    except asyncio.TimeoutError:
        await message.channel.send("You took too long to choose a blacksmithing category.")

async def handle_crafting(message, check):
    crafting_embed = discord.Embed(
        title='Crafting',
        description='Choose a crafting category:',
        color=discord.Color.blue()
    )
    crafting_embed.add_field(name='1. One-Handed Swords (ohs)', value='Information on crafting one-handed swords', inline=False)
    crafting_embed.add_field(name='2. Two-Handed Swords (2hs)', value='Information on crafting two-handed swords', inline=False)
    crafting_embed.add_field(name='3. Halberds', value='Information on crafting halberds', inline=False)
    crafting_embed.add_field(name='4. Katanas', value='Information on crafting katanas', inline=False)
    crafting_embed.add_field(name='5. Staffs', value='Information on crafting staffs', inline=False)
    crafting_embed.add_field(name='6. Magic Devices', value='Information on crafting magic devices', inline=False)
    crafting_embed.add_field(name='7. Bows', value='Information on crafting bows', inline=False)
    crafting_embed.add_field(name='8. Bow Guns', value='Information on crafting bow guns', inline=False)
    crafting_embed.add_field(name='9. Armors', value='Information on crafting armors', inline=False)
    crafting_embed.add_field(name='10. Additionals', value='Information on crafting additionals', inline=False)

    await message.channel.send(embed=crafting_embed)

    try:
        crafting_response = await bot.wait_for('message', check=check, timeout=15.0)

        intro_info = ("For effective smithing, focus on maxing Create Equipment, Careful Creation, and Expert's Creation.\n\n"
                      "Then, learn Anvil skills as needed to improve your proficiency.\n\n"
                      "Each character has a Blacksmith Proficiency Level, visible under Menu > Character > Stat > Production.\n\n"
                      "The Blacksmith Proficiency Level can be increased by crafting items, with a default cap of 50.\n\n"
                      "Each level of Novice's, Craftsman's, Blacksmith's, and Master's Anvil skill raises this cap by 5,\n\n"
                      "allowing a maximum cap of 250 when all four skills are maxed, although maxing all four skills immediately is not necessary.\n\n\n"
                      "Each item has both a level and a difficulty, each serving distinct purposes. The item's level determines how much proficiency experience (EXP) you gain when crafting it. To efficiently level up your proficiency, choose items with levels higher than your current proficiency level. If an item's level is lower than your proficiency level by 11 or more, no EXP is gained.\n\n\n"
                      "An item's difficulty indicates how challenging it is to craft. You cannot craft an item if its difficulty exceeds your own.\n"
                      "Crafted items' potential increases with the crafter's base stat, without bonuses from equipment, skills, food, or avatars. For certain items, each 10 points in this stat add 1 potential.\n\n")

        crafting_info = {
            '1': f"Here's information on crafting one-handed swords (ohs):\n{intro_info}\n"
            "To craft 1handed sword put STR+DEX in your players stat. \n\n"
            "Potential = (total no of STR + total no of DEX) / 20",
            '2': f"Here's information on crafting two-handed swords (2hs):\n{intro_info}"
            "To craft 2handed swords put STR in your players stat. \n\n"
            "Potential = Total no. of STR / 10",
            '3': f"Here's information on crafting halberds:\n{intro_info}"
            "To craft halberds put STR+AGI in your players stats. \n\n"
            "Potential = Total number of STR+AGI / 20",
            '4': f"Here's information on crafting katanas:\n{intro_info}"
            "To craft katanas put DEX+AGI in your players stats \n\n"
            "Potential = Total no of DEX+AGI / 20",
            '5': f"Here's information on crafting staffs:\n{intro_info}"
            "To craft staffs put INT in your players stats\n\n"
            "Potential = Total no of INT / 10",
            '6': f"Here's information on crafting magic devices:\n{intro_info}"
            "To craft magic devices put INT+AGI in your players stats \n\n"
            "Potential = Total no of INT+AGI / 20",
            '7': f"Here's information on crafting bows:\n{intro_info}"
            "To craft Bows put STR+DEX in your players stats\n\n"
            "Potential = Total no of STR+DEX / 20",
            '8': f"Here's information on crafting bow guns:\n{intro_info}"
            "To craft bowguns put DEX in players stats.\n\n"
            "Potential = Total no of DEX / 10",
            '9': f"Here's information on crafting armors:\n{intro_info}"
            "To craft Armors put VIT in your players stats\n\n"
            "Potential = Total no of VIT / 10",
            '10': "Currently, crafting additionals is not possible with player crafting skills. You can either get it by farming or from NPC Blacksmiths in safe towns."
        }

        response_text = crafting_info.get(crafting_response.content.lower(), "Please provide the number from the list to see the crafting info. Try again.")
        await message.channel.send(response_text)
    except asyncio.TimeoutError:
        await message.channel.send("You took too long to choose a crafting category.")

async def handle_refine(message, check):
    refine_embed = discord.Embed(
        title='Refinement',
        description='Choose a refinement category:',
        color=discord.Color.gold()
    )
    refine_embed.add_field(name='1. Weapon', value='Information on refining weapons')
    refine_embed.add_field(name='2. Shield, Armor, Additionals', value='Information on refining shields, armor, and additionals')
    await message.channel.send(embed=refine_embed)

    try:
        refine_response = await bot.wait_for('message', check=check, timeout=15.0)

        refine_info = {
            '1': "Here's information on refining weapons:\n\n"
            "Refining enhances weapons by increasing their damage output and bonus attack.\n"
            "Each +N refine adds N^2% damage and +N bonus attack.\n\n"
            "Example: A weapon with 100 base attack refined to +6 gains +(6^2% × 100) and +6 bonus attack, totaling 142 attack power.\n\n"
            "Character level doesn't affect success rates, but capping TEC is advised for refining, statting, and alchemy. LUK prevents refinement degradation.\n\n"
            "For effective refinements (use tech to reach +B) and from (+B to +S) use a luck character.",
            '2': "Here's information on refining shields, armor, and additionals:\n"
            "For armor, additional, or shields, refining will only reduce damage taken from attacks. It won't boost your attacks.\n\n"
            "If you are only focusing on damage, then refine only weapons."
        }

        response_text = refine_info.get(refine_response.content.lower(), "Please provide a valid number from the list to see the refinement info. Try again.")
        await message.channel.send(response_text)
    except asyncio.TimeoutError:
        await message.channel.send("You took too long to choose a refinement category.")

    await bot.process_commands(message)
bot.run(TOKEN)
