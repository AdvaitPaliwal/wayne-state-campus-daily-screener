# Automate Your Wayne State Campus Daily Screener

`wayne-state-campus-daily-screener` is a cloud-hosted program for Wayne State University students. It autofills https://forms.wayne.edu/covid-19-screening/ and texts you the scannable QR code everyday at 12 am in your declared time zone.

## Getting Started

#### Create a GitHub Account [Here](https://github.com/join)
Required to fork a copy of this repository
#### Create a Gmail Account [Here](https://accounts.google.com/signup)
Required to send an MMS to your number
#### Create a Heroku Account [Here](https://signup.heroku.com/)
Required to host the program

## Setting up GitHub
[Fork](https://github.com/AdvaitPaliwal/wayne-state-campus-daily-screener/fork) this repository. This will create a copy of this repository on your account that you will host on Heroku.

## Setting up the MMS service
Obtain and save an [app password](https://myaccount.google.com/apppasswords). You'll be using this later.

## Setting up Heroku
1. In the [app dashboard](https://dashboard.heroku.com/apps), click `New` and `Create new app`
2. Click `Create app` and Heroku will generate a random app name for you
3. Go to `Settings` and click `Add buildpack`
4. Select `python` and save changes

## Setting up the variables
Navigate to your app settings in Heroku, click `Reveal Config Vars` and input the following key-value pairs:
* `text_email` - This is your email created earlier 
* `text_password` - This is the app password for your email 
* `accessid` - Your Wayne State access id 
* `password` - Your Wayne State password 
* `phone_num` The phone number that will receive the texts 
* `phone_provider` - Your phone provider from the [list](https://github.com/AdvaitPaliwal/wayne-state-campus-daily-screener/blob/main/phone_providers.txt) 
* `TZ` - A timezone selection from the [database](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones) under `TZ database name`

## Deploying the app
1. Click `Deploy` and select `GitHub` as your deployment method
2. On the same page, click `Connect to GitHub`
3. Once your GitHub account is authorized, your username is displayed and you can search for repositories stored within your account
4. In the `repo-name` input, search `wayne state campus daily screener`
5. Once the name of your repo appears, click `Connect`
6. Scroll down, `Enable Automatic Deploys`, and `Deploy Branch`
7. Finally, go to `Resources`, click the pencil icon under `Free Dynos`, and toggle the switch on

## Debugging
1. On the top-right section in your app, click `More`
2. Select `View logs`
3. If there are any errors in the inputted variables, the `Application Logs` will let you know
4. Otherwise, you're all set and the app will text you a QR code every midnight