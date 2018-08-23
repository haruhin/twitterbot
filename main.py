from requests_oauthlib import OAuth1Session
import json
import requests
from datetime import datetime
from pytz import timezone


def auto_tenki():
    utc = datetime.now(timezone('UTC'))
    jst = utc.astimezone(timezone('Asia/Tokyo'))

    weather_key = "4a3c14a6eb735cc4e3d45ead00f3c8b5"

    CK = 'dsFjpEeS0lXFg2LJYuU5E0s3K'
    CS = '7C3U5MaH0aJ05GwHuLCEieqskFn4ksjq0qEmuoPIsGPHJIddI2'
    AT = '886660687212101632-pPXKAfxxI0Fu1wrVy8Pa5qpV9cpYwS7'
    AS = 'aoUNCIfTCfAFJWXGSmtZLLEaaVx1M75Hgj787dj46WiCw'
    twitter = OAuth1Session(CK, CS, AT, AS)

    twitter_url = "https://api.twitter.com/1.1/account/update_profile.json"
    city_name = "Matsumoto"
    weather_url = "http://api.openweathermap.org/data/2.5/weather?q={city}&APPID={key}&units=metric"
    weather_url = weather_url.format(city=city_name, key=weather_key)

    username = 'Tsuchiya'

    weather_req = requests.get(weather_url)
    weather_data = json.loads(weather_req.text)
    weather_id = weather_data["weather"][0]["id"]

    username = username.format(temp = weather_data["main"]["temp"])

    if weather_id == 800:
        if jst >= 18 and jst <= 23 or jst >= 0 and jst <= 5:
            username = username + "🌕"
        else:
            username = username + "☀"
    elif weather_id >= 801:
        if jst >= 18 and jst <= 23 or jst >= 0 and jst <= 5:
            username = username + "🌕☁"
        else:
            username = username + "☀☁"

    elif weather_id >= 802 and weather_id <= 804:
        username = username + "☁"
    elif weather_id >= 300 and weather_id <= 321:
        username = username + "🌂"
    elif weather_id >= 500 and weather_id <= 531:
        username = username + "☔"
    elif weather_id >= 200 and weather_id <= 232:
        username = username + "⚡☔"
    elif weather_id >= 600 and weather_id <= 622:
        username = username + "⛄"
    elif weather_id >= 900:
        username = username + "🌀"

    params = {"name": username}

    # update Twitter username.
    twitter_req = twitter.post(twitter_url, params=params)

    if twitter_req.status_code == 200:
        print('OK')

    else:
        print('ERROR')

    return


if __name__ == '__main__':
    auto_tenki()
