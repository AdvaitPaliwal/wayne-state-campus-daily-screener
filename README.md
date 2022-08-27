<p align="center">
    <img src="https://user-images.githubusercontent.com/66044327/186369540-f968a8b8-d30c-4ce9-99f4-cc44d64d462a.jpg" width="1100"/>
    <br>
<p>

`wayne-state-campus-daily-screener` is a free cloud-hosted program for Wayne State University students. It autofills https://forms.wayne.edu/covid-19-screening/ and texts you the scannable QR code every midnight in your declared time zone. No more freezing in the cold, struggling to complete your daily screener. Bliss.

## Note

The program selects `No` for the last three questions. Do not use it if your responses vary. I am not liable for your inaccuracies.

<p>
<img width="759" src="https://user-images.githubusercontent.com/66044327/185913984-6ca00068-9a7b-406c-9078-7028297f4907.png">
</p>

## Getting Started

#### Create a GitHub Account [Here](https://github.com/join)

Required to fork a copy of this repository.

#### Create a Gmail Account [Here](https://accounts.google.com/signup)

Required to send free MMS messages to your number through email.

#### Create a Heroku Account [Here](https://signup.heroku.com/)

Required to host the program for free.

## Setting up GitHub

[Fork](https://github.com/AdvaitPaliwal/wayne-state-campus-daily-screener/fork) this repository. It allows you to freely experiment with changes and host it without affecting the original project.

## Setting up the MMS service

Obtain and save an [app password](https://myaccount.google.com/apppasswords). This will grant email access to the program.

## Setting up Heroku

1. In the [app dashboard](https://dashboard.heroku.com/apps), click `New` and `Create new app`.
2. Click `Create app` and Heroku will generate a random app name for you.
3. Go to `Settings` and click `Add buildpack`.
4. Select `python` and save changes.

## Setting up the variables

Navigate to your app settings in Heroku, click `Reveal Config Vars` and input the following key-value pairs:

- `text_email` - This is your email created earlier
- `text_password` - This is the app password for your email
- `accessid` - Your Wayne State access id
- `password` - Your Wayne State password
- `phone_num` The phone number that will receive the texts
- `phone_provider` - Your phone provider verbatim from [phone_providers.txt](https://github.com/AdvaitPaliwal/wayne-state-campus-daily-screener/blob/main/phone_providers.txt)
- `TZ` - A timezone selection from the [database](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones) under `TZ database name`

All config vars are stored in an encrypted form as they are designed to contain sensitive information.

## Deploying the app

1. Click `Deploy` and select `GitHub` as your deployment method.
2. On the same page, click `Connect to GitHub`.
3. Once your GitHub account is authorized, your username is displayed and you can search for repositories stored within your account.
4. In the `repo-name` input, search `wayne state campus daily screener`.
5. Once the name of your repo appears, click `Connect`.
6. Scroll down, `Enable Automatic Deploys`, and `Deploy Branch`.
7. Finally, go to `Resources`, click the pencil icon under `Free Dynos`, and toggle the switch on (toggle it off to end the process).

## Debugging

1. On the top-right section in your app, click `More`.
2. Select `View logs`.
3. If there are any errors in the inputted variables, the `Application Logs` will let you know.
4. If there are any errors in the program, please create an [issue](https://github.com/AdvaitPaliwal/wayne-state-campus-daily-screener/issues/new/choose).
5. Otherwise, you're all set and the app will text you a QR code every midnight.
