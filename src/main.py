import json
from RedditApi import api as RedditApi
from TTS import tts as TTS

topPosts = json.loads(RedditApi.getTopPostsJson())




def main():
    # TTS.Test()
    TTS.Read(topPosts[0]['title'])
    for comment in topPosts[0]['comments']:
        TTS.Read(comment)

if __name__ == '__main__':
    main()