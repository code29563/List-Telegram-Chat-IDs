# List Telegram Chat IDs
This is a script to output a list of your dialogs in Telegram, your contacts, and the channels/supergroups you've left, with their corresponding IDs.

The environment variables are to be given in a .env file. An example is shown in example.env.

1. Make an app with the Telegram API: [https://my.telegram.org/apps](https://my.telegram.org/apps) and fill in the API\_ID and API\_HASH environment variables in the .env file with the App api\_id and App api\_hash respectively.
2. Obtain a Pyrogram session string for your account, e.g. using option 1 of [this script](https://github.com/code29563/Telethon-Pyrogram-session-strings). Fill the envrionment variable SESSION_STRING with this session string.
3. Install the requirements if they're not already installed by running ‘pip install -r requirements.txt’, then run the script using 'python app.py'

The output is a list of your current dialogs, followed by a line break, followed by 'Contacts:', followed by a list of your contacts, followed by a line break, followed by 'Left Channels/supergroups:', followed by a list of the channels/supergroups you've left.

Channels and supergroups (including those that you've left) are listed in this format:
```
{title} {username} --- ID
```
Bot chats are listed in this format:
```
{bot name} {username} --- ID
```
Contacts and private chats with users are listed in this format:
```
{first name} {last name} {username} --- ID
```
The script doesn't output anything for regular (non-super) groups.

Wherever a field doesn't exist for a particular user/bot/supergroup/channel, the output is `None`. For a deleted user account, you might find `{first name}`, `{last name}` and `{username}` all come out as `None`.