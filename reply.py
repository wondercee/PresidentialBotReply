import tweepy, time, sys

consumer_key="4gAOb9cxg1e06O88SqWWZpiYK"
consumer_secret="y943Pjh8AkFbQEZqK1yeRLtXFqGIZkEn1PoGobH2FnVR98Tgu2"
access_token="844581311000035328-pJ9SX281GockJiIwHegchPkrhZSqKmD"
access_token_secret="vgQdtFYJxBV7A47uXEcn6Ja81jRNk6jncq7Eq7toMUlw4"

#Connect to Twitter
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

twts = api.search(q="#Presidentielle2017")

#list of specific strings we want to check for in Tweets
t = ['#Presidentielle2017']

for s in twts:
    for i in t:
        if i == s.text:
            sn = s.user.screen_name
            m = "@%s Suivez la campagne de tous les candidats a la presidentielle ici." % (sn)
            s = api.update_status(status=m)
