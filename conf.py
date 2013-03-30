import os

class Config(object):
	os.environ['FACEBOOK_APP_ID']= '511702678887759'
	os.environ['FACEBOOK_SECRET']= '955265ef335bacc58715bfe3e399e0f5'
	DEBUG = True
	TESTING = False
	LOG_LEVEL = os.environ.get('LOG_LEVEL', 'DEBUG')
	FBAPI_APP_ID = os.environ.get('FACEBOOK_APP_ID') 
	print FBAPI_APP_ID
	FBAPI_APP_SECRET = os.environ.get('FACEBOOK_SECRET')
	FBAPI_SCOPE = ['user_likes', 'user_photos', 'user_photo_video_tags']
