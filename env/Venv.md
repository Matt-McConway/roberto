# Venv Instructions
---
## Building The Virtual Environment:

### Prerequisites
* Have Python 3
* Have Pip up to date
* Have virtualenv installed `pip install virtualenv`

### Instructions

1. Create the virtual environment:
    * `python -m virtualenv name-of-environment-directory`


2. cd to this directory


3. Run the virtual environment:
    * Mac: source `/mac-env/bin/activate`
    * Windows 10: `win-env\Scripts\activate`
    * Should have something like this:
        * (win-env) M:\Code\GitHub\Slackbot\roberto\env>
            * (Name of your environment in parentheses)


4. Run `pip install -r requirements.txt`


5. Now you will need to load in the API tokens as virtual environment variables so that they aren't shared in your code! You will need tokens from the following:

| Source                                         | Variable Name      |
| ---------------------------------------------- |:------------------:|
| [Slack](https://api.slack.com/apps)            | SLACK_BOT_TOKEN    |
| [Cat API](http://thecatapi.com/)               | CAT_API_KEY        |
| [Open Weather Map](https://openweathermap.org/)| OPENWEATHERMAP_KEY |
| [JSON Whois](https://jsonwhois.io/)            | WHO_IS_KEY         |

6. Now add each token as below:
    * With the environment running, use:
        * `export VARIABLENAME=APITOKEN`
        * NOTE: If you are on windows use: `set VARIABLENAME=APITOKEN`


**Now that your virtual environment is set up, in the future you simply need to run the environment!**

---
## Running the Virtual Environment
* Mac: source `/mac-env/bin/activate`
* Windows 10: `win-env\Scripts\activate`
* Should have something like this:
    * (win-env) M:\Code\GitHub\Slackbot\roberto\env>
        * (Name of your environment in parentheses)

Once the environment is running, you simply run the app with `python bot.py` *when you are in the src directory.*
