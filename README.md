# Roberto
The friendly Slack bot for MERCURIOUS :)

Roberto can do many things!

## Current Features:
* Fetch weather for a city (Just temperature at this stage)
* Fetch a random cat image!
* Domain whois
* Domain lookup

## How to run the bot:
To build and run the app see: [Venv instructions](./env/Venv.md)

You'll then need to add Roberto to your slack team too (Manually/dev mode only for now): [Slack bot user](https://api.slack.com/slack-apps)

## Commands:
**Weather: **
* weather cityname OR Weather cityname
    * E.g. `@roberto weather Auckland` gives "It is currently 20 in Auckland" (Degrees Celsius), data sourced from [Open Weather Map](http://openweathermap.org).

**Cats: **
* cat OR Cat
    * E.g. `@roberto Cat` will give an image of a cat from the [Cat API](http://thecatapi.com/)

**Domain whois: **
* whois url OR Whois url
    * E.g. `@roberto Whois www.mercurious.nz` will give "I can't lookup .nz domains :'(" (Will have to build own API for this!)
    * E.g. `@roberto whois www.google.com` will give the registration details for Google's domain.

**Domain Lookup: **
* check OR Check
    * E.g. `@roberto check www.mercurious.nz` will give "mercurious.nz is registered :("

## Planned Changes:

* Proper error handling
* Code optimisation, reduction
* Integration with domain registrar
* Integration with WHMCS
* Migration to Docker from Venv - I want to learn this technology!
* .nz domain lookup (Need to build own API for this)
* More weather features

Feel free to contribute or use this project as a template of sorts!
