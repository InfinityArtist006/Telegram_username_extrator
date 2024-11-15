import time
import asyncio
from telethon import TelegramClient
from telethon.tl.types import InputPeerEmpty
from telethon.tl.functions.messages import GetDialogsRequest
from telethon.errors import FloodWaitError
from pyfiglet import figlet_format
from termcolor import colored

# Display the stylish intro
def display_intro():
    intro_text = figlet_format("Welcome!", font="slant")
    print(colored(intro_text, "cyan"))
    print(colored("Telegram Username Extractor", "yellow"))
    print(colored("By: Infinity Artist", "green"))
    print(colored("="*50, "magenta"))
    time.sleep(2)
    print(colored("This tool extracts all usernames from the channels and groups you've joined.", "cyan"))
    print(colored("Let's get started!\n", "yellow"))

# Use your own values from my.telegram.org
def get_user_input():
    print(colored("Please enter your Telegram API credentials below.", "magenta"))
    API_ID = input("Enter Api ID: ")
    API_HASH = input("Enter Api hash: ")
    PHONE_NUMBER = input("Enter phone number like +12344567890: ")
    return API_ID, API_HASH, PHONE_NUMBER

# Create a new Telegram client
async def extract_usernames(client):
    await client.start()

    chats = []
    last_date = None
    chunk_size = 200

    try:
        result = await client(GetDialogsRequest(
            offset_date=last_date,
            offset_id=0,
            offset_peer=InputPeerEmpty(),
            limit=chunk_size,
            hash=0
        ))

        chats.extend(result.chats)
        print(colored('Fetching usernames from all groups and channels...', "blue"))

        with open("usernames.txt", "w") as f:
            for chat in chats:
                try:
                    if (hasattr(chat, 'megagroup') and chat.megagroup) or (hasattr(chat, 'broadcast') and chat.broadcast):
                        print(colored(f"Processing group/channel: {chat.title}", "green"))
                        if chat.username:
                            f.write(chat.username + "\n")
                        else:
                            print(colored(f"No username for {chat.title} (ID: {chat.id})", "red"))
                except FloodWaitError as e:
                    print(colored(f"Rate limit exceeded, sleeping for {e.seconds} seconds.", "yellow"))
                    await asyncio.sleep(e.seconds)
                except Exception as e:
                    print(colored(f"Could not access chat: {chat.title} - {str(e)}", "red"))

        print(colored("Usernames have been saved to usernames.txt", "green"))

    except Exception as e:
        print(colored(f"An error occurred: {str(e)}", "red"))

if __name__ == '__main__':
    display_intro()
    API_ID, API_HASH, PHONE_NUMBER = get_user_input()
    client = TelegramClient('session_name', API_ID, API_HASH)

    with client:
        client.loop.run_until_complete(extract_usernames(client))
