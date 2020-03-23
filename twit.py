import tweepy

# Authenticate to Twitter
auth = tweepy.OAuthHandler("i0fnpu89sMI8QMnyGKHJkdyYS",
    "ruWDxELm9PSAwnbrz6PcxZ7TFaPfQqPeoLn7g2rYuN2PsRisyv")
auth.set_access_token("1106313860460568576-wVk6Olx2T3dmwMB8A4iDGC7jmzWkhk",
    "9iGV5ruDnAw4bcTxf5Slpwu9NqvsugDSqJtHJXGJNTK4i")

api = tweepy.API(auth)

try:
    api.verify_credentials()
    print("Authentication OK")
except:
    print("Error during authentication")
