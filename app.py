
# A very simple Flask Hello World app for you to get started with...

from helpers import *
from flask import Flask, render_template, request, url_for, redirect
import base64
import requests
import datetime

app = Flask(__name__)

# commit 21 aug


@app.route('/', methods=['GET', 'POST'])
def input():
    if request.method == 'POST':
        inputSongName = request.form["inputSongName"]
        inputArtistName = request.form["inputArtistName"]
        # songParameters = inputSongName + " " + inputArtistName
        return redirect(url_for('carousel', inputSongName=inputSongName, inputArtistName=inputArtistName))
    return render_template('input.html')



@app.route("/main", methods=['GET', 'POST'])
def main():
    inputSongName = request.form.get('inputSongName', None)
    inputArtistName = request.form.get('inputArtistName', None)
    songParameters = inputSongName + " " + inputArtistName
    link2song = get_link2lyrics(songParameters)
    lyrics = get_lyrics(link2song)
    df = returnPandasLyrics(lyrics)
    dList = help(df)

    embedLink = returnEmbed(inputSongName, inputArtistName)
    #embedLink = returnEmbed(inputSongName, inputArtistName)
    return render_template("main.html", dList=dList, embedLink=embedLink)

