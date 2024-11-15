Usage Guide: Telegram Username Extractor
Getting Started
Clone or Download the Repository
Begin by cloning or downloading this repository to your local machine.

Navigate to the Project Directory
Open a terminal and move to the project folder using the cd command.

Run the Script
Execute the following command in your terminal to start the extractor:

bash
Copy code
python TG_Channel&Groups_Usernames_Extractor.py  
Provide Telegram API Credentials
When prompted, enter your Telegram API details:

API ID
API Hash
Phone Number (e.g., +1234567890)
Output
The script will process your groups and channels, then save the extracted usernames in a file named usernames.txt.

Setting Up Telegram API Credentials
To use this tool, you'll need to generate API credentials:

Visit Telegram API.
Log In using your Telegram account.
Navigate to "API Development Tools" and create a new application.
Copy the API ID and API Hash provided.
Project Structure
TG_Channel&Groups_Usernames_Extractor.py: The main script for extracting usernames.
usernames.txt: A text file where the extracted usernames are saved.
Error Handling
Rate Limits (FloodWaitError):
The script automatically detects and handles rate limits by pausing for the required duration before resuming.

Invalid or Missing Inputs:
If incorrect credentials or inputs are provided, the script will prompt you to re-enter them.

License
This project is licensed under the MIT License. Feel free to use, modify, and share it as needed.

Acknowledgments
Telethon Library for providing a robust interface to interact with Telegram's API.
Infinity Artist for the vision and implementation of this project.
Contact
For inquiries or support, reach out to us on Telegram: t.me/@Spider006.
