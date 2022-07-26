
# A very simple Flask Hello World app for you to get started with...

from helpers import *
from flask import Flask, render_template, request, url_for, redirect
import base64
import requests
import datetime

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello from Flask!'


'''
@app.route('/home')
def home():
    imgs = ["https://static.bangkokpost.com/media/content/20220504/c1_4297382.jpg",
            "http://c.files.bbci.co.uk/0C5B/production/_97436130_gettyimages-508496270-1.jpg"]
    dlist = [[0.0, 'Instrumentals', 'https://www.bbemusic.com/user-files/uploads/edd/2021/06/Vadim-SC-Inst-scaled.jpg', '', 0], [16.0, "She'd take the world off my shoulders\n", 'https://i.ytimg.com/vi/byuNGOzUBUE/maxresdefault.jpg', '', 1], [20.0, 'If it was ever hard to move\n', 'https://lirp.cdn-website.com/08d31351/dms3rep/multi/opt/312375-2-largest-container-ship-the-ever-ace-3dd763ab-640w.jpg', '', 2], [25.0, "She'd turn the rain to a rainbow\n", 'https://cdn-icons-png.flaticon.com/512/25/25645.png', '', 3], [29.0, 'When I was living in the blue\n', 'https://assets.ltkcontent.com/images/889472/If-I-Was-or-If-I-Were_0066f46bde.jpg', '', 4], [33.0, "Why then, if she's so perfect?\n", 'https://www.lifeprint.com/asl101/signjpegs/s/so1.jpg', '', 5], [37.0, 'Do I still wish that it was you?\n', 'https://icons.iconarchive.com/icons/iconarchive/red-orb-alphabet/256/Letter-I-icon.png', '', 6], [42.0, "Perfect don't mean that it's working\n", 'https://therodinhoods.com/wp-content/uploads/2017/01/perfect.png', '', 7], [45.0, 'So what can I do? (Ooh)\n', 'https://www.oma.org.au/sites/default/files/imagecache/article_thumb/uploaded-content/field_f_content_thumbnail/tik_tok_international_ooh_poster.png', '', 8], [49.0, 'Instrumentals', 'https://www.bbemusic.com/user-files/uploads/edd/2021/06/Vadim-SC-Inst-scaled.jpg', '', 9], [49.0, "When you're out of sight in my mind\n", 'https://wpe.hoffmanacademy.com/wp-content/uploads/2021/02/become-a-great-sight-reader.jpg', '', 10], [57.0, 'Instrumentals', 'https://www.bbemusic.com/user-files/uploads/edd/2021/06/Vadim-SC-Inst-scaled.jpg', '', 11], [58.0, "'Cause sometimes I look in her eyes\n", 'https://i.ytimg.com/vi/pAgnJDJN4VA/maxresdefault.jpg', '', 12], [62.0, "And that's where I find a glimpse of us\n", 'https://www.nationsonline.org/maps/USA-map.jpg', '', 13], [67.0, 'And I try to fall for her touch\n', 'https://cdn.cnn.com/cnnnext/dam/assets/210908195724-best-fall-candle-scents-lead.jpg', '', 14], [70.0, "But I'm thinking of the way it was\n", 'https://st.depositphotos.com/1403216/2573/i/950/depositphotos_25733133-stock-photo-right-way.jpg', '', 15], [75.0, 'Said, "I\'m fine" and said, "I moved on"\n', 'https://images.twinkl.co.uk/tw1n/image/private/t_630_eco/image_repo/5d/2b/T-L-4940-Said-Synonyms-Word-Mat_ver_1.jpg', '', 16], [79.0, "I'm only here passing time in her arms\n", 'https://www.goodnewspilipinas.com/wp-content/uploads/2021/04/HER-Music-Oscars.jpg', '', 17], [83.0, "Hoping I'll find a glimpse of us\n", 'https://cdn-icons-png.flaticon.com/512/25/25645.png', '', 18], [91.0, 'Instrumentals', 'https://www.bbemusic.com/user-files/uploads/edd/2021/06/Vadim-SC-Inst-scaled.jpg', '', 19], [93.0, 'Tell me he savors your glory\n', 'https://images-na.ssl-images-amazon.com/images/I/51JruWmdF7L.jpg', '', 20], [96.0, 'Does he laugh the way I did?\n', 'https://ichef.bbci.co.uk/images/ic/1920x1080/p07hblcn.jpg', '', 21], [101.0, 'Is this a part of your story?\n', 'https://images.firstpost.com/wp-content/uploads/2019/12/GettyImages-1124573573a.jpg', '', 22], [105.0, 'One that I had never lived\n', 'https://images.theabcdn.com/i/37236260/600x600/c.jpg', '', 23], [110.0, "Maybe one day you'll feel lonely\n", 'https://corp.smartbrief.com/wp-content/uploads/2022/04/BeFunky-photo323-726x420.jpg', '', 24], [
        113.0, "And in his eyes, you'll get a glimpse\n", 'https://www.kirkeyecenter.com/wp-content/uploads/2020/04/eye-img.jpg', '', 25], [119.0, "Maybe you'll start slippin' slowly and find me again\n", 'https://image.shutterstock.com/image-vector/letter-me-luxury-logo-template-260nw-1070440982.jpg', '', 26], [126.0, 'Instrumentals', 'https://www.bbemusic.com/user-files/uploads/edd/2021/06/Vadim-SC-Inst-scaled.jpg', '', 27], [126.0, "When you're out of sight in my mind\n", 'https://wpe.hoffmanacademy.com/wp-content/uploads/2021/02/become-a-great-sight-reader.jpg', '', 28], [134.0, 'Instrumentals', 'https://www.bbemusic.com/user-files/uploads/edd/2021/06/Vadim-SC-Inst-scaled.jpg', '', 29], [135.0, "'Cause sometimes I look in her eyes\n", 'https://icons.iconarchive.com/icons/iconarchive/red-orb-alphabet/256/Letter-I-icon.png', '', 30], [138.0, "And that's where I find a glimpse of us\n", 'https://i.ytimg.com/vi/UePtoxDhJSw/maxresdefault.jpg', '', 31], [143.0, 'And I try to fall for her touch\n', 'https://cdn.cnn.com/cnnnext/dam/assets/210908195724-best-fall-candle-scents-lead.jpg', '', 32], [147.0, "But I'm thinking of the way it was\n", 'https://pics.filmaffinity.com/The_Book_of_Boba_Fett_TV_Series-736176382-large.jpg', '', 33], [152.0, 'Said, "I\'m fine" and said, "I moved on"\n', 'https://images.twinkl.co.uk/tw1n/image/private/t_630_eco/image_repo/5d/2b/T-L-4940-Said-Synonyms-Word-Mat_ver_1.jpg', '', 34], [156.0, "I'm only here passing time in her arms\n", 'https://here-we-are.jp/renewal2022/wp-content/uploads/2022/02/logo.png', '', 35], [160.0, "Hoping I'll find a glimpse of us\n", 'https://pics.filmaffinity.com/The_Book_of_Boba_Fett_TV_Series-736176382-large.jpg', '', 36], [168.0, 'Instrumentals', 'https://www.bbemusic.com/user-files/uploads/edd/2021/06/Vadim-SC-Inst-scaled.jpg', '', 37], [168.0, 'Ooh-ooh-ooh\n', 'https://i.imgflip.com/52xno6.jpg', '', 38], [173.0, 'Ooh-ooh-ooh\n', 'https://i.imgflip.com/52xno6.jpg', '', 39], [180.0, 'Instrumentals', 'https://www.bbemusic.com/user-files/uploads/edd/2021/06/Vadim-SC-Inst-scaled.jpg', '', 40], [181.0, "'Cause sometimes I look in her eyes\n", 'https://images.ctfassets.net/a9odgsv44wmq/1f0qt7M73iQYFdcxuabGiW/005cc435368d8e84a7db745b0c11c44e/Secondary_Tile_Cluck.jpg', '', 41], [185.0, "And that's where I find a glimpse of us\n", 'https://www.worldatlas.com/r/w1200/upload/0b/46/30/shutterstock-1669675267.jpg', '', 42], [190.0, 'And I try to fall for her touch\n', 'https://icons.iconarchive.com/icons/iconarchive/red-orb-alphabet/256/Letter-I-icon.png', '', 43], [194.0, "But I'm thinking of the way it was\n", 'https://i.ytimg.com/vi/MKdw7E9yn3M/maxresdefault.jpg', '', 44], [198.0, 'Said, "I\'m fine" and said, "I moved on"\n', 'https://d3qdvvkm3r2z1i.cloudfront.net/media/catalog/product/cache/1/thumbnail/85e4522595efc69f496374d01ef2bf13/f/i/fine_thumb.png', '', 45], [202.0, "I'm only here passing time in her arms\n", 'https://i.ytimg.com/vi/MKdw7E9yn3M/maxresdefault.jpg', '', 46], [206.0, "Hoping I'll find a glimpse of us\n", 'https://thumbs.dreamstime.com/b/woman-eyes-closed-praying-hoping-best-closeup-portrait-young-asking-forgiveness-miracle-isolated-white-36989897.jpg', '', 47], [214.0, 'Instrumentals', 'https://www.bbemusic.com/user-files/uploads/edd/2021/06/Vadim-SC-Inst-scaled.jpg', '', 48]]
    return render_template("home.html", imgs=imgs, dlist=dlist)
'''


@app.route('/index')
def index():
    imgs = ["https://static.bangkokpost.com/media/content/20220504/c1_4297382.jpg",
            "http://c.files.bbci.co.uk/0C5B/production/_97436130_gettyimages-508496270-1.jpg"]
    return render_template("index.html", imgs=imgs)


@app.route('/input', methods=['GET', 'POST'])
def input():
    if request.method == 'POST':
        inputSongName = request.form["inputSongName"]
        inputArtistName = request.form["inputArtistName"]
        # songParameters = inputSongName + " " + inputArtistName
        return redirect(url_for('carousel', inputSongName=inputSongName, inputArtistName=inputArtistName))
    return render_template('input.html')


'''
@app.route("/carousel", methods=['GET', 'POST'])
def carousel():
    inputSongName = request.form.get('inputSongName', None)
    inputArtistName = request.form.get('inputArtistName', None)
    songParameters = inputSongName + " " + inputArtistName
    link2song = get_link2lyrics(songParameters)
    lyrics = get_lyrics(link2song)
    df = returnPandasLyrics(lyrics)
    dList = helpers(df)
    return render_template("carousel.html", dList=dList)
'''

'''
@app.route("/result", methods=['GET', 'POST'])
def result():
    # getting variable from the input.html
    embedLink = request.form.get('embedLink')
    inputSongName = request.form.get("inputSongName")
    inputArtistName = request.form.get("inputArtistName")
    embedLink = returnEmbed(inputSongName, inputArtistName)
    # using macky function to do this one la
    return render_template("result.html", embedLink=embedLink, inputSongName=inputSongName, inputArtistName=inputArtistName)
'''


@app.route("/macsong", methods=['GET', 'POST'])
def macsong():
    '''
    inputSongName = request.form.get('inputSongName', None)
    inputArtistName = request.form.get('inputArtistName', None)
    songParameters = inputSongName + " " + inputArtistName
    link2song = get_link2lyrics(songParameters)
    lyrics = get_lyrics(link2song)
    df = returnPandasLyrics(lyrics)
    dList = helpers(df)
    '''
    URI = returnEmbed('lover', 'taylor swift')
    # embedLink = returnEmbed(inputSongName, inputArtistName)
    return render_template("macsong.html", URI=URI)


@app.route('/playsbaby')
def playsbaby():
    return render_template("playsbaby.html")
