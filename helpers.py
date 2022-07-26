import time
import random
import pandas as pd
from botnoi import scrape as sc
import re
import base64
import requests
import datetime

from bs4 import BeautifulSoup


def returnEmbed(inputSongName, inputArtistName):
    client_id = 'c2a7548b4b23475097744cd218f4aae6'
    client_secret = 'a5bd1adf7a46467aab83f36b70fed1fe'

    class SpotifyAPI(object):
        access_token = None
        access_token_expires = datetime.datetime.now()
        access_token_did_expire = True
        client_id = None
        client_secret = None
        token_url = "https://accounts.spotify.com/api/token"

        def __init__(self, client_id, client_secret, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.client_id = client_id
            self.client_secret = client_secret

        def get_client_credentials(self):
            """
            Returns a base64 encoded string
            """
            client_id = self.client_id
            client_secret = self.client_secret
            if client_secret == None or client_id == None:
                raise Exception("You must set client_id and client_secret")
            client_creds = f"{client_id}:{client_secret}"
            client_creds_b64 = base64.b64encode(client_creds.encode())
            return client_creds_b64.decode()

        def get_token_headers(self):
            client_creds_b64 = self.get_client_credentials()
            return {
                "Authorization": f"Basic {client_creds_b64}"
            }

        def get_token_data(self):
            return {
                "grant_type": "client_credentials"
            }

        def perform_auth(self):
            token_url = self.token_url
            token_data = self.get_token_data()
            token_headers = self.get_token_headers()
            r = requests.post(token_url, data=token_data,
                              headers=token_headers)
            if r.status_code not in range(200, 299):
                return False
            data = r.json()
            now = datetime.datetime.now()
            access_token = data['access_token']
            expires_in = data['expires_in']  # seconds
            expires = now + datetime.timedelta(seconds=expires_in)
            self.access_token = access_token
            self.access_token_expires = expires
            self.access_token_did_expire = expires < now
            return True

    spotify = SpotifyAPI(client_id, client_secret)
    spotify.perform_auth()

    access_token = spotify.access_token
    # print(access_token)

    # The most popular
    from urllib.parse import urlencode
    headers = {
        "Authorization": f"Bearer {access_token}"
    }
    endpoint = "https://api.spotify.com/v1/search"
    #q ='q=as it was harry styles&type=track'

    q = "q="+inputSongName+" " + inputArtistName+"&type=track"

    lookup_url = f"{endpoint}?{q}"
    # print(lookup_url)
    r = requests.get(lookup_url, headers=headers)
    # print(r.status_code)

    response = r.json()
    # return(response)

    URI = response['tracks']['items'][0]['uri']
    #URI = URI.replace("spotify", '')
    #URI = URI.replace(":", '/')
    #embed_url = f'https://open.spotify.com/embed{URI}?utm_source=generator&theme=0'
    # return(embed_url)
    return(URI)

# base functions


def get_link2lyrics(song_artist):
    URL = f'https://www.lyricsify.com/search?q={song_artist}'
    user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.114 Safari/537.36'
    r = requests.get(URL, headers={'User-Agent': user_agent})
    url_contents = r.content
    soup = BeautifulSoup(url_contents, 'html.parser')
    a = soup.find_all('a', {"class": "title"})
    link2song = a[0]['href']
    return link2song


def get_lyrics(link2song):
    URL = f"https://www.lyricsify.com{link2song}"
    user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.114 Safari/537.36'
    r = requests.get(URL, headers={'User-Agent': user_agent})
    url_contents = r.content
    soup = BeautifulSoup(url_contents, 'html.parser')
    div = soup.select('div#entry')
    div = [row.text for row in div]
    lyrics = div[0]
    lyrics = lyrics.split('\n')
    line_start = r'\[\d\d:\d\d.\d\d\].+$'
    adv_lrc = '\<.*?\>'
    twice = '\[\dx]'
    cleaned_lyrics = []
    for line in lyrics:
        line = line.strip()
        if re.match(line_start, line):
            if not re.match(adv_lrc, line):
                if not re.match(twice, line):
                    cleaned_lyrics.append(line)
    return cleaned_lyrics

# base functions


def returnPandasLyrics(lyrics):
    # set up dataframe
    df = pd.DataFrame(columns=['timeStamp', 'lyrics'])
    for line in lyrics:
        #print(f'line {count}: {line}')
        timeStamp = line[line.find("[")+1:line.find("]")]
        lyrics = line[10:]
        df.loc[len(df.index)] = [timeStamp, lyrics]
    return(df)
    print(df)


def change_timeStamp(df):
    df["milliseconds"] = " "
    for i in range(len(df.index)):
        timeStampString = df.iloc[i]['timeStamp']
        after_Dot = (timeStampString[6:])
        x = time.strptime(timeStampString.split('.')[0], '%M:%S')
        seconds = datetime.timedelta(
            hours=x.tm_hour, minutes=x.tm_min, seconds=x.tm_sec).total_seconds()
        milliseconds = (seconds*1000) + (int(after_Dot)*10)

        #df.iloc[i]['timeStamp'] = seconds
        print(milliseconds)
        df.iloc[i, df.columns.get_loc('milliseconds')] = milliseconds
        #df.iloc[i]['timeStamp'] = seconds
        print(df.iloc[i]['milliseconds'])
        i = i+1
    print(df)
    return(df)


def get_carouselSleep(df):
    # get sleep time
    df["sleep"] = " "
    for i in range(len(df.index)-1):
        timeStart = df.loc[i]['milliseconds']
        timeStop = df.loc[i+1]['milliseconds']
        x = (timeStop-timeStart)
        df.iloc[i, df.columns.get_loc('sleep')] = x
        #df.loc[i]['sleep'] = x
        i = i+1
    df.loc[len(df.index)-1]['sleep'] = 0
    return(df)


def delete_null(df):
    df = df.replace(r'^\s*$', "Instrumentals", regex=True)
    return(df)


def find_imageSRC(df):
    df["src"] = " "
    for i in range(len(df.index)):
        s = df.loc[i]['lyrics']
        words = list(map(str, s.split()))
        temp = random.choice(words)
        img = sc.get_image_urls(temp, 1)
        # break from img
        selectedImg = img[1]
        df.iloc[i, df.columns.get_loc('src')] = selectedImg
        #df.loc[i]['src'] = selectedImg
        # print(i)
        i = i+1
    return(df)


def help(df):
    df = delete_null(df)
    df = change_timeStamp(df)
    df = get_carouselSleep(df)
    df = find_imageSRC(df)
    dList = df.values.tolist()
    return(dList)


'''
link2song = get_link2lyrics('taylor swift')
lyrics = get_lyrics(link2song)
df = returnPandasLyrics(lyrics)
dList = help(df)
# print(lyrics)
# print(df)
print(dList)
'''

#0 - timestamp
#1- lyrics
#2- millisecond
#3 - sleep
#4 - src

'''
embedLink = returnEmbed('as it was', 'harry styles')
print(embedLink)
print(type(embedLink))
'''
