import os
import discord
from discord.ext import commands
from dotenv import load_dotenv
import asyncio

# Load environment variables from .env file (useful for local development)
load_dotenv()

# Get the token from environment variables
TOKEN = os.getenv('DISCORD_TOKEN')

# Check if the token is loaded correctly
if TOKEN is None:
    raise ValueError("DISCORD_TOKEN environment variable is not set")

# Define leveling information
leveling_info = {
    range(1, 34): ("Nisel Mountain: Mountainside", "Shell Mask", "Earth"),
    range(34, 50): ("Ancient Empress Tomb: Area 1", "Bone Dragonewt", "Dark"),
    range(50, 60): ("Land Of Chaos: Hidden boss", "Forestia (normal/hard)", "Wind"),
    range(60, 69): ("Land Of Chaos: Hidden boss", "Forestia (Nightmare)", "Wind"),
    range(70, 80): ("Land Under Cultivation: Hill", "Masked Warrior (Hard)", "Fire"),
    range(80, 90): ("Land Under Cultivation: Hill", "Masked Warrior (Nightmare)", "Fire"),
    range(90, 100): ("Gravel Terrace", "Jade Raptor (Nightmare) or Polde Ice Valley: Don-Yeti", "(Jade Wind) and (Don yeti Earth)"),
    range(100, 110): ("Land Under Cultivation: Hill", "Masked Warrior (Ultimate)", "Fire"),
    range(110, 117): ("Spring of Rebirth: Top", "Cerberus (Nightmare)", "Water"),
    range(117, 130): ("Magic Waste Site: Deepest Part", "Scrader (Ultimate)", "Dark"),
    range(130, 140): ("Spring of Rebirth: Top", "Cerberus (Ultimate)", "water"),
    range(140, 148): ("Dark Castle: Area 2", "Memecoleous (Ultimate)", "Netural"),
    range(148, 153): ("Plastida: Deepest Part", "Imitator (Ultimate)", "Fire"),
    range(154, 158): ("Small Demi Machina Factory Core", "Tyrant Machina (Ultimate)", "Neutral"),
    range(158, 164): ("Large Demi Machina Factory: Deepest Part", "Mozto Machina (Ultimate)", "Neutral"),
    range(164, 175): ("Ultimea Palace: Throne", "Venena Coenubia (Nightmare)", "Fire"),
    range(176, 184): ("Droma Square", "Ultimate Machina (Ultimate)", "Neutral"),
    range(184, 198): ("Ultimea Palace: Throne", "Venena Coenubia (Ultimate)", "Fire"),
    range(198, 208): ("Dark Dragon Shrine: Near the Top", "Finstern the Dark Dragon (Ultimate)", "Dark"),
    range(208, 220): ("Labilans Sector: Square", "Kuzto (Ultimate)", "Earth"),
    range(220, 230): ("Recetacula Sector: Depot Rooftop", "Gravicep (Ultimate)", "Netural"),
    range(230, 245): ("Arche Valley: Depths", "Arachnidemon (Ultimate)", "Dark"),
    range(245, 260): ("Operation Zone: Cockpit Area", "Trickster Dragon Mimyugon (Nightmare)", "Earth"),
    range(260, 285): ("Arstida: Depth", "Velum (Ultimate)", "Netural"),
    range(285, 295): ("Boma Konda: Village Center", "Brass Dragon Reguita", "Netural"),
    range(295, 300): ("Boss colon", "Are you baka?", "Do mq shoo"),
}

# Helper function to get leveling information
def get_leveling_info(level):
    for level_range, info in leveling_info.items():
        if level in level_range:
            return info
    return ("Level out of range", "Please provide a valid level", "N/A")

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

    if message.content.lower().startswith("where should i level") or message.content.lower().startswith("where to level"):
        await message.channel.send("Please provide your current level:")

        def check(msg):
            return msg.author == message.author and msg.channel == message.channel and msg.content.isdigit()

        try:
            msg = await bot.wait_for('message', check=check, timeout=30)
            level = int(msg.content)
            place, monster, element = get_leveling_info(level)

            embed = discord.Embed(title=f"Grinding Info for Level {level}", color=discord.Color.blue())
            embed.add_field(name="Level", value=f"{level}", inline=True)
            embed.add_field(name="Place", value=f"{place}", inline=True)
            embed.add_field(name="Monster", value=f"{monster}", inline=True)
            embed.add_field(name="Element", value=f"{element}", inline=True)

            await message.channel.send(embed=embed)
        except asyncio.TimeoutError:
            await message.channel.send("You took too long to respond! Please try again.")

    if message.content.lower().startswith("i need help") or message.content.lower().startswith("hey elite") or message.content.lower().startswith("hey guide"):
        embed = discord.Embed(
            title=f'How can I help you, {message.author.name}?',
            description='I can give you information regarding:',
            color=discord.Color.blue()
        )
        embed.add_field(name='1. Builds', value='Learn about different builds.')
        embed.add_field(name='2. Blacksmithing', value='Information on weapon forging, armor crafting, etc.')
        embed.add_field(name='3. Synthesis', value='Material and synthesis, enchantments.')
        embed.add_field(name='4. Equipment', value='Information on various types of equipment.')

        help_message = await message.channel.send(embed=embed)

        def check(m):
            return m.author == message.author and m.channel == message.channel

        try:
            response = await bot.wait_for('message', check=check, timeout=30.0)

            if response.content.lower() in ['1', 'build', 'builds']:
                build_embed = discord.Embed(
                    title='Builds',
                    description='Choose a build category:(type build number from the list only)',
                    color=discord.Color.green()
                )
                build_embed.add_field(name='1. 0HS Tank', value='Information on 0HS Tank build.')
                build_embed.add_field(name='2. 0HS DPS', value='Information on 0HS DPS build.')
                build_embed.add_field(name='3. 2HS', value='Information on 2HS build.')
                build_embed.add_field(name='4. Bow', value='Information on Bow build.')
                build_embed.add_field(name='5. BWG', value='Information on BWG build.')
                build_embed.add_field(name='6. KTN', value='Information on KTN build.')
                build_embed.add_field(name='7. HB', value='Information on HB build.')
                build_embed.add_field(name='8. KNX Tank', value='Information on KNX Tank build.')
                build_embed.add_field(name='9. KNX DPS', value='Information on KNX DPS build.')
                build_embed.add_field(name='10. Barehand', value='Information on Barehand build.')
                build_embed.add_field(name='11. Support', value='Information on Support build.')
                await message.channel.send(embed=build_embed)

                try:
                    build_response = await bot.wait_for('message', check=check, timeout=30.0)

                    build_info = {
                        '1': "Here's information on 0HS Tank build"
                        "https://youtu.be/M03qVi9_vdI?si=suIdBXH8ckJaGcPT",
                        '2': "Here's information on 0HS DPS build."
                        "https://youtu.be/h_ZvZluqJi4?si=ih9B7oM8-df0ilRa",
                        '3': "Here's information on 2HS build."
                        "https://youtu.be/Ig0wwr15Ysc?si=VGHA1M3HQ0RLysP2",
                        '4': "Here's information on Bow build."
                        "https://youtu.be/aVQRczWLieE?si=3L0wJZb7z7oEzZIN",
                        '5': "Here's information on BWG build."
                        "https://youtu.be/mqOQy_gUd6s?si=s59CO6iJyBQLZH_i",
                        '6': "Here's information on KTN build."
                        "https://youtu.be/GkKh8mr5Jz4?si=ez9sYm1t6hBC-1-X",
                        '7': "Here's information on HB build."
                        "https://youtu.be/OANNpTI_w3w?si=yEK7cXksdeT_9ma9",
                        '8': "Here's information on KNX Tank build."
                        "https://youtu.be/NlqC8QSREN0?si=6M2TQpH5A-tsMt8j",
                        '9': "Here's information on KNX DPS build."
                        "https://youtu.be/4AcqxRXtWns?si=Z2X7D4n3BjN6Kbj9",
                        '10': "Here's information on Barehand build."
                        "https://youtu.be/yD5_ahA980I?si=XSATYm4iq6nG13-r",
                        '11': "Here's information on Support build."
                        "https://youtu.be/-uqsK4f2LSU?si=MZ7_is8vP6Ny3RiB"
                    }

                    response_text = build_info.get(build_response.content.lower(), "Please provide the number from the list to see the build info..try again")
                    await message.channel.send(response_text)

                except asyncio.TimeoutError:
                    await message.channel.send("You took too long to choose a build.")
            
            elif response.content.lower() in ['2', 'bs', 'blacksmith', 'blacksmithing']:
    blacksmith_embed = discord.Embed(
        title='Blacksmithing',
        description='Choose a blacksmithing category:',
        color=discord.Color.orange()
    )
    blacksmith_embed.add_field(name='1. Crafting', value='Crafting in the game involves creating weapons from materials. Player-crafted equipment emphasizes ATK, stability, and DEF stats. Rather than predefined stats, items feature potential points that can be converted into statistics (refer to section C). To engage in crafting, players require the "Create Equipment" EX Skill, which unlocks the crafting menu. Advancing this skill enhances crafting success rates. Notably, skills such as "Careful Creation" and "Expert's Creation," when maxed at level 10, increase an item's potential by 10% (rounded down).''')
    blacksmith_embed.add_field(name='2. Refine', value='Refining in the game strengthens weapons or armor. Each +N refine for weapons increases damage by N^2% and adds +N bonus attack. For armor, additional gear, and shields, each refine reduces damage taken by 1%. For example, refining a weapon with 100 base attack to +6 results in +(6^2% × 100) and +6 bonus attack, totaling 142 attack power.''')
    blacksmith_embed.add_field(name='3. Statting', value='Statting in the game converts potential points into stat points for player-crafted equipment, with up to 8 customizable stat slots and limits based on character level, total Customization skill levels, and stat caps.')
    blacksmith_embed.add_field(name='4. Enhancement', value='Information on enhancements')

    await message.channel.send(embed=blacksmith_embed)

    try:
        blacksmith_response = await bot.wait_for('message', check=check, timeout=15.0)

        if blacksmith_response.content.lower() == '1' or blacksmith_response.content.lower() == 'crafting':
            crafting_embed = discord.Embed(
                title='Crafting',
                description='Choose a crafting category:',
                color=discord.Color.blue()
            )
            crafting_embed.add_field(name='1. One-Handed Swords (ohs)', value='Information on crafting one-handed swords')
            crafting_embed.add_field(name='2. Two-Handed Swords (2hs)', value='Information on crafting two-handed swords')
            crafting_embed.add_field(name='3. Helberds', value='Information on crafting helberds')
            crafting_embed.add_field(name='4. Katanas', value='Information on crafting katanas')
            crafting_embed.add_field(name='5. Staffs', value='Information on crafting staffs')
            crafting_embed.add_field(name='6. Magic Devices', value='Information on crafting magic devices')
            crafting_embed.add_field(name='7. Bows', value='Information on crafting bows')
            crafting_embed.add_field(name='8. Bow Guns', value='Information on crafting bow guns')
            crafting_embed.add_field(name='9. Armours', value='Information on crafting armours')
            crafting_embed.add_field(name='10. Additionals', value='Information on crafting additionals')

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
          "TO craft 2handed swords put Str in your players stat. \n\n"
          "Potential = Total no. of Str / 10",
    '3': f"Here's information on crafting helberds:\n{intro_info}"
          "To craft helberds put STR+AGI in your players stats. \n\n"
          "Potential = Total number of STR+AGI / 20",
    '4': f"Here's information on crafting katanas:\n{intro_info}"
          "To craft katanas put DEX+AGI in your players stats \n\n"
          "Potential = Total no of DEX+AGI / 20",
    '5': f"Here's information on crafting staffs:\n{intro_info}"
          "To craft staffs put Int in your players stats\n\n"
          "Potential = Total no of Int / 10",
    '6': f"Here's information on crafting magic devices:\n{intro_info}"
          "To craft magic devices put INT+AGI in your players stats \n\n"
          "Potential = Total no of INT+AGI / 20",
    '7': f"Here's information on crafting bows:\n{intro_info}"
          "To craft Bows put STR+DEX in your players stats\n\n"
          "Potential = Total no of STR+DEX / 20",
    '8': f"Here's information on crafting bow guns:\n{intro_info}"
          "To craft bowguns put dex on players stats.\n\n"
          "Potential = Total no of Dex\10",
    '9': f"Here's information on crafting armours:\n{intro_info}"
          "To craft Armours put Vit in your Players stats\n\n"
          "Potential = Total no of Vit / 10",
    '10': f"Here's information on crafting additionals:\n"
           "Currently Crafting additionals are not possible with players crafting skills.\n\n You can Either get it by farming or from NPC Blacksmiths from safetowns"
}

                response_text = crafting_info.get(crafting_response.content.lower(), "Please provide the number from the list to see the crafting info. and Try again type ""hey Elite""")
                await message.channel.send(response_text)

            except asyncio.TimeoutError:
                await message.channel.send("You took too long to choose a crafting category.")

        elif blacksmith_response.content.lower() == '2' or blacksmith_response.content.lower() == 'refine':
    refine_embed = discord.Embed(
        title='Refinement',
        description='Choose a refinement category:',
        color=discord.Color.gold()
    )

    refine_embed.add_field(name='1. Weapon', value='Information on refining weapons')
    refine_embed.add_field(name='2. Shield, Armour, Additionals', value='Information on refining shields, armor, and additionals')

    await message.channel.send(embed=refine_embed)

    try:
        refine_response = await bot.wait_for('message', check=check, timeout=15.0)

        refine_info = {
            '1': "Here's information on refining weapons:\n\n"
                 "Refining enhances weapons by increasing their damage output and bonus attack.\n"
                 "Each +N refine adds N^2% damage and +N bonus attack.\n\n"
                 "Example: A weapon with 100 base attack refined to +6 gains +(6^2% × 100) and +6 bonus attack, totaling 142 attack power.\n\n"
                 "Character level doesn't affect success rates, but capping TEC is advised for refining, statting, and alchemy. LUK prevents refinement degradation.\n\n"
                 "For effective refinements (use tech to reach +b) and from (+b to +s) use luck char ",
            '2': "Here's information on refining shields, armor, and additionals:\n"
                 "In case of armor, additional, or shields, it will only reduce damage taken from attacks. It won't boost your attacks.\n\n"
                 "So if you are only focusing on damage, then refine only weapons."
        }

        response_text = refine_info.get(refine_response.content.lower(), "Please provide a valid number from the list to see the refinement info. Try again.")
        await message.channel.send(response_text)

    except asyncio.TimeoutError:
        await message.channel.send("You took too long to choose a refinement category.")

        elif blacksmith_response.content.lower() == '3' or blacksmith_response.content.lower() == 'statting':
    await message.channel.send("The statting section is currently under development. Please check back later.")


        elif blacksmith_response.content.lower() == '4' or blacksmith_response.content.lower() == 'enhancement':
    await message.channel.send("The enhancement section is currently under development. Please check back later.")


        else:
            await message.channel.send("Invalid choice. Please choose a valid option from 1 to 4")

    except asyncio.TimeoutError:
        await message.channel.send("You took too long to choose a blacksmithing category.")

            elif response.content.lower() == '3':
                await message.channel.send("This section is under development! uwu")
            elif response.content.lower() == '4':
                await message.channel.send("This section is under development! uwu")
            else:
                await message.channel.send("Enter the numbers and try again muwhahahahaha... type "hey elite" to trigger from begining")

        except asyncio.TimeoutError:
            await message.channel.send("You took too long to respond.Type "hey elite" to trigger from begining")

    await bot.process_commands(message)

bot.run(TOKEN)
