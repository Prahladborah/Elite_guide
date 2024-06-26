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
    range(70, 80): ("Land Under Cultivation: Hill", "Masked Warrior (Hard)", "Earth"),
    range(80, 90): ("Land Under Cultivation: Hill", "Masked Warrior (Nightmare)", "Earth"),
    range(90, 100): ("Gravel Terrace", "Jade Raptor (Nightmare) or Polde Ice Valley: Don-Yeti", "Water"),
    range(100, 110): ("Land Under Cultivation: Hill", "Masked Warrior (Ultimate)", "Earth"),
    range(110, 117): ("Spring of Rebirth: Top", "Cerberus (Nightmare)", "Fire"),
    range(117, 130): ("Magic Waste Site: Deepest Part", "Scrader (Ultimate)", "Dark"),
    range(130, 140): ("Spring of Rebirth: Top", "Cerberus (Ultimate)", "Fire"),
    range(140, 148): ("Dark Castle: Area 2", "Memecoleous (Ultimate)", "Dark"),
    range(148, 153): ("Plastida: Deepest Part", "Imitator (Ultimate)", "Water"),
    range(154, 158): ("Small Demi Machina Factory Core", "Tyrant Machina (Ultimate)", "Neutral"),
    range(158, 164): ("Large Demi Machina Factory: Deepest Part", "Mozto Machina (Ultimate)", "Neutral"),
    range(164, 175): ("Ultimea Palace: Throne", "Venena Coenubia (Nightmare)", "Dark"),
    range(176, 184): ("Droma Square", "Ultimate Machina (Ultimate)", "Neutral"),
    range(184, 198): ("Ultimea Palace: Throne", "Venena Coenubia (Ultimate)", "Dark"),
    range(198, 208): ("Dark Dragon Shrine: Near the Top", "Finstern the Dark Dragon (Ultimate)", "Dark"),
    range(208, 220): ("Labilans Sector: Square", "Kuzto (Ultimate)", "Dark"),
    range(220, 230): ("Recetacula Sector: Depot Rooftop", "Gravicep (Ultimate)", "Dark"),
    range(230, 245): ("Arche Valley: Depths", "Arachnidemon (Ultimate)", "Dark"),
    range(245, 260): ("Operation Zone: Cockpit Area", "Trickster Dragon Mimyugon (Nightmare)", "Dark"),
    range(260, 285): ("No info", "Do main quest", "N/A"),
    range(285, 295): ("Boss colon", "Boss colon", "N/A"),
    range(295, 300): ("Boss colon", "Boss colon", "N/A"),
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

            if response.content.lower() == '1':
                build_embed = discord.Embed(
                    title='Builds',
                    description='Choose a build category:(type build number)',
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

                    response_text = build_info.get(build_response.content.lower(), "I'm sorry, I didn't understand your choice.")
                    await message.channel.send(response_text)

                except asyncio.TimeoutError:
                    await message.channel.send("You took too long to choose a build.")
            elif response.content.lower() == '2':
                await message.channel.send("This section is under development! uwu")
            elif response.content.lower() == '3':
                await message.channel.send("This section is under development! uwu")
            elif response.content.lower() == '4':
                await message.channel.send("This section is under development! uwu")
            else:
                await message.channel.send("This section is under development! uwu")

        except asyncio.TimeoutError:
            await message.channel.send("You took too long to respond.")

    await bot.process_commands(message)

bot.run(TOKEN)
