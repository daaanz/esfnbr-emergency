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

res = requests.get(url, headers = headers).json()
emergency = res['emergencynotice']['news']['messages']

playlist = emergency[0]['playlistId']
body = emergency[0]['body']
title = emergency[0]['title']

while 1:
    emergencyNew = res['emergencynotice']['news']['messages']
    if emergencyNew != emergency:
        try:
            print('Se ha detectado ' + emergencyNew[0]['title'])
            api.update_with_media('assets/emergency.png', title + ' (' + playlist + ')' '\n\n' + body)
            print('Publicado correctamente.')
            emergency = res['emergencynotice']['news']['messages']
        except:
            print('No se ha podido enviar el Tweet.')
    else:
        print('No se detectan cambios en Emergency Notice. Buscando de nuevo en 60 segundos.')

    time.sleep(setDelay)


    
