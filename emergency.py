import requests
import tweepy
import time
import os
from os import environ

auth = tweepy.OAuthHandler(environ["CONSUMER_TOKEN"], environ["CONSUMER_SECRET"])
auth.set_access_token(environ["KEY"], environ["SECRET"])
api = tweepy.API(auth)

url = 'https://fortnitecontent-website-prod07.ol.epicgames.com/content/api/pages/fortnite-game'
headers = {'Accept-Language': 'es-ES'}

setDelay = 60

res0 = requests.get(url, headers = headers).json()
emergency = res0['emergencynotice']['news']['messages']

while 1:
    try:
        playlist = emergency['playlistId']
        body = emergency['body']
        title = emergency['title']
        res1 = requests.get(url, headers = headers).json()
        emergencyNew = res1['emergencynotice']['news']['messages']
        if emergencyNew != emergency:
            try:
                for i in emergencyNew:
                    print('Se ha detectado ' + emergencyNew + i['title'])
                    api.update_with_media('assets/emergency.png', i['title'] + ' (' + i['playlist'] + ')' '\n\n' + i['body'])
                    print('Publicado correctamente.')
                res2 = requests.get(url, headers = headers).json()
                emergency = res2['emergencynotice']['news']['messages']
            except:
                print('No se ha podido enviar el Tweet.')
        else:
            print('No se detectan cambios en Emergency Notice. Buscando de nuevo en 60 segundos.')
    except:
        print('No hay un aviso de emergencia.')

    time.sleep(setDelay)


    
