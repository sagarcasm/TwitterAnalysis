import tweepy
from tweepy import OAuthHandler
from pymongo import MongoClient


#your constants for the twitter API
CONSUMER_KEY = '----USE YOUR CONSUMER_KEY----- '
CONSUMER_SECRET_KEY = '----USE YOUR CONSUMER_SECRET_KEY----- '
ACCESS_TOKEN = '----USE YOUR ACCESS_TOKEN----- '
ACCESS_SECRET_KEY = '----USE YOUR ACCESS_SECRET_KEY----- '

class TweepyAuth:

    def __init__(self, CONSUMER_KEY, CONSUMER_SECRET_KEY, ACCESS_TOKEN, ACCESS_SECRET_KEY):
        self.CONSUMER_KEY = CONSUMER_KEY
        self.CONSUMER_SECRET_KEY = CONSUMER_SECRET_KEY
        self.ACCESS_TOKEN = ACCESS_TOKEN
        self.ACCESS_SECRET_KEY = ACCESS_SECRET_KEY

    def authTweepy(self):
        auth = OAuthHandler(self.CONSUMER_KEY, self.CONSUMER_SECRET_KEY)
        auth.set_access_token(self.ACCESS_TOKEN, self.ACCESS_SECRET_KEY)
        api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)
        return api


class mongoDbconnect:

    def __init__(self,  url, port):
        self.url = url
        self.port = port

    def mongoConnection(self):
        try:
            client = MongoClient(self.url, self.port)
            return client
        except ValueError:
            return ValueError

    def insertRecords(self,connectObj, data):
         #twitter db name
        database = connectObj.twitter

        for tweet in data:
            # inserting data
            database.twitterCollection.insert(tweet._json)

#creating an object for the tweepy auth
twA = TweepyAuth(CONSUMER_KEY,CONSUMER_SECRET_KEY,ACCESS_TOKEN,ACCESS_SECRET_KEY)

#passing the obejct to authTweepy for login token
authObj = twA.authTweepy()

#check if the authentication is right
if (not authObj):
    print ("Cannot Authenticate the given credentials")
else:

    # Getting Geo ID for any Country
    places = authObj.geo_search(query="USA", granularity="country")
    place_id = places[0].id
    #print('INDIA id is: ', place_id)

    #adding the location ID here
    #place :96683cc9126741d1 is for USA
    searchQuery = 'place:'+place_id+' murder OR theft OR drugs OR' \
                  'larceny OR rape OR homicide'

    # checking if the data has returned a from home timeline sucessful status
    for status in tweepy.Cursor(authObj.home_timeline).items(1):
        # Process a single status
        print(status.text)

    # add your hashtags here in the below array
    items = 100000

    #itemCount =0
    # dont forget the limit per 15 mins so run accordingly
    hashtagTweets = tweepy.Cursor(authObj.search, q=searchQuery).items(items)


    #mongodb connection parameters I have used the default for the mongodb
    mongoUrl = 'localhost'
    port = 27017
    #data name
    db = 'twitter'

    # mongodb class object
    mongoObj = mongoDbconnect(mongoUrl, port)
    mongoConn = mongoObj.mongoConnection()
    mongoObj.insertRecords(mongoConn,hashtagTweets)





