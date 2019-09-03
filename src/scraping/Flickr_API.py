from flickrapi import FlickrAPI
from urllib.request import urlretrieve
from pprint import pprint
import os, time, sys

# API キーの情報
#APIキーはFlickrで取得
key = "b0a3396cc06eedc211a6b7e6930ffbf9" #APIキー
secret = "809221a760343f2b" #secretキー

wait_time = 1

animalname = sys.argv[1]

# 画像を保存するディレクトリを指定
#自身の前のディレクトリにあるファイルを参照
savedir = "./" + animalname

flickr = FlickrAPI(key, secret, format='parsed-json')
result = flickr.photos.search(
    text = animalname,
    per_page = 500, #取得するデータ件数(500がMAX)
    media = 'photos',
    sort = 'relevance',
    safe_search = 1,
    extras = 'url_q, licence'
)

# 結果を表示(URL)
photos = result['photos']
pprint(photos)

#画像を保存
for photo in photos['photo']:
    url_q = photo['url_q']
    filepath = savedir + '/' + photo['id'] + '.jpg'

    if os.path.exists(filepath): continue
    urlretrieve(url_q, filepath)
    time.sleep(wait_time)
