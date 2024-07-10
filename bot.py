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
    elif message.content.lower().startswith(("weapon atk food buff", "weapon atk buff","weapon buff")):
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
    elif message.content.lower().startswith(("magic resist", "magical resist","magical resistance")):
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
    elif message.content.lower().startswith(("phy resist", "physical resist","physical resistance")):
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
        ''',  # Properly closing the multiline string
        color=discord.Color.green()  # Assuming you want to set a color
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
        await message.channel.send(embed=embed
                                  
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
