
import json
from kafka import SimpleProducer, KafkaClient
import tweepy
import configparser


class TweeterStreamListener(tweepy.StreamListener):
    """ A class to read the twitter stream and push it to Kafka"""

    def __init__(self, api):
        self.api = api
        super(tweepy.StreamListener, self).__init__()
        client = KafkaClient("localhost:9092")
        self.producer = SimpleProducer(client, async = True,
                          batch_send_every_n = 1000,
                          batch_send_every_t = 10)

    def on_status(self, status):
        """ This method is called whenever new data arrives from live stream.
        We asynchronously push this data to kafka queue"""
        msg =  status.text.encode('utf-8')
        try:
            self.producer.send_messages(b'twitterstream', msg)
            print("SUCCESS")
        except Exception as e:
            print(e)
            return False
        return True

    def on_error(self, status_code):
        print("Error received in kafka producer")
        return True # Don't kill the stream

    def on_timeout(self):
        return True # Don't kill the stream




if __name__ == '__main__':

    # Read the credententials from 'twitter-app-credentials.txt' file
    '''config = configparser.ConfigParser()
    config.read('twitter-app-credentials.txt')
    consumer_key = config['DEFAULT']['consumerKey']
    consumer_secret = config['DEFAULT']['consumerSecret']
    access_key = config['DEFAULT']['accessToken']
    access_secret = config['DEFAULT']['accessTokenSecret']
    '''
    consumer_key = 'XEtO7Su9CPuzK348pVDTZ6PM7'
    consumer_secret = 'PXCl2azADOIHgPSquNdZ6sK9LN7SEZNp0j3zHMCOXT5sB1mz5d'
    access_key = '3322175381-XpS7iCfaFgTDPtAJ7TFl00UYFwUI42ghqgD1t68'
    access_secret = '2nJSu26YytePWVQo1sjIKLiQKl2COirF6p93wq8YUIf2A'
    
    # Create Auth object
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_key, access_secret)
    api = tweepy.API(auth)

    print("API", api)
    
    stream = tweepy.Stream(auth, listener = TweeterStreamListener(api))
    stream.filter(track=['python'])

    # Create stream and bind the listener to it
    #stream = tweepy.Stream(auth, listener = TweeterStreamListener(api))

    #Custom Filter rules pull all traffic for those filters in real time.
    #stream.filter(track = ['love', 'hate'], languages = ['en'])
    #stream.filter(locations=[-180,-90,180,90], languages = ['en'])