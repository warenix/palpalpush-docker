# palpalpush-docker

##Pre-requesite

0. A twitter app at https://apps.twitter.com/
0. An android app that can receives GCM

## Build
```
sh build.sh
```

## Run
```
docker run -d --name palpalpush\
	-e TWITTER_CONSUMER_KEY=[]\
	-e TWITTER_SECRET=[]\
	-e TWITTER_ACCESS_TOKEN=[]\
	-e TWITTER_ACCESS_TOKEN_SECRET=[]\
	-e GCM_API_KEY=[]\
	-e REG_ID=[]\
	warenix/palpalpush
```
