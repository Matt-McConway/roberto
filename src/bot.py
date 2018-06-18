# Builtin libraries
import os
import sys
import time
import re

# 3rd Party Libraries
from slackclient import SlackClient

# Bot Modules
from open_weather_map import Weather
from cats import Cat
from whois import Who

"""
    Acknowledgement for bot.py source:
    https://www.fullstackpython.com/blog/build-first-slack-bot-python.html
    Credit to Matt Makai of Full Stack Python
"""


# Instantiate the Slack client
# (SLACK_BOT_TOKEN is stored in my virtual environment)
slack_client = SlackClient(os.environ.get('SLACK_BOT_TOKEN'))
# The bots user ID is assigned after the bot starts up
bot_id = None

# CONSTANTS
RTM_READ_DELAY = 1  # 1 second delay between reading from RealTimeMessage API
EXAMPLE_COMMAND = "do"
MENTION_REGEX = "^<@(|[WU].+?)>(.*)" # Captures @bot_id + command(s)


def parse_bot_commands(slack_events):
    """
        Parses a list of events coming from the Slack RTM API to find bot
        commands.

        If a bot command is found, this function returns a tuple of command and
        channel.

        If it's not found, then this function returns None, None.
    """
    for event in slack_events:
        if event["type"] == "message" and not "subtype" in event:
            user_id, message = parse_direct_mention(event["text"])
            if user_id == bot_id:
                return message, event["channel"]
    return None, None


def parse_direct_mention(message_text):
    """
        Finds a direct mention (a mention that is at the beginning) in the
        message text and returns the user ID which was mentioned.

        If there is no direct mention, returns None
    """
    matches = re.search(MENTION_REGEX, message_text)
    # Group 1 contains the username, group 2 contains the message/command
    return (matches.group(1), matches.group(2).strip()) if matches else (None, None)


def handle_command(command, channel):
    """
        Executes bot command if the command is known.
    """
    # Default response is help text for the user
    default_response = "I don't know that. Pester @mmcconway to implement it!"

    # Finds and executes the given command, filling in the response
    response = None
    if command.startswith(EXAMPLE_COMMAND):
        response = command
    if command.startswith("weather") or command.startswith("Weather"):
        weather = Weather()
        city = command[command.find(" ")+1:]
        temp = weather.getWeather(city)
        response = "It is currently {} in {}.".format(temp,city)
    if command.startswith("cat") or command.startswith("Cat"):
        CatGetter = Cat()
        response = CatGetter.getCat()
    if command.startswith("whois") or command.startswith("Whois"):
        who = Who()
        domain = command[command.find(" ")+1:command.rfind(" ")]
        tld = command[command.find(domain)+len(domain)+1:]
        response = who.getWhois(domain, tld)
    if command.startswith("check") or command.startswith("Check"):
        who = Who()
        domain = command[command.find(" ")+1:command.rfind(" ")]
        tld = command[command.find(domain)+len(domain)+1:]
        response = who.getRegistration(domain, tld)

    # Sends the response back to the channel
    slack_client.api_call(
        "chat.postMessage",
        channel=channel,
        text=response or default_response
    )


if __name__ == "__main__":
    if slack_client.rtm_connect(with_team_state=False):
        print("Roberto has connected and is now running!")
        # Read bot's user ID by calling Web API method `auth.test`
        bot_id = slack_client.api_call("auth.test")["user_id"]
        while True:
            command, channel = parse_bot_commands(slack_client.rtm_read())
            if command:
                handle_command(command, channel)
            time.sleep(RTM_READ_DELAY)
    else:
        print("Connection failed. Exception traceback printed above.")
