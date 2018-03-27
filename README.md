# Twitter data extraction using Using MongoDb and Python

Script to download twitter data bsed on hashtags and geolocation using Python Tweepy library and loading it on a MongoDB database for further analysis.

## Prerequisite
Python

MongoDB installed locally


## Usage

### Replacing the constants
Replace the below constants by registering your app on the twitter API (apps.twitter.com)

```
CONSUMER_KEY = '----USE YOUR CONSUMER_KEY----- '
CONSUMER_SECRET_KEY = '----USE YOUR CONSUMER_SECRET_KEY----- '
ACCESS_TOKEN = '----USE YOUR ACCESS_TOKEN----- '
ACCESS_SECRET_KEY = '----USE YOUR ACCESS_SECRET_KEY----- '
```
Mongodb connection parameters have been kept at default feel free to change the parameters if you hava a different environment.

### Make your own search Query using hastags and Geolocation
Make changes to the search terms and geolocation according to your needs.
```
places = authObj.geo_search(query="USA", granularity="country")
place_id = places[0].id

#adding the location ID here
#place :96683cc9126741d1 is for USA
searchQuery = 'place:'+place_id+' murder OR theft OR drugs OR' \
                  'larceny OR rape OR homicide'
```
Further code is self-explanatory.
## Contributing

Please read [CONTRIBUTING.md](https://gist.github.com/PurpleBooth/b24679402957c63ec426) for details on our code of conduct, and the process for submitting pull requests to us.
