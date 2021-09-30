import praw
import urllib.request
import os
import ctypes
import json

reddit = praw.Reddit(
    client_id='HF3AWm2G4HOV52cL1XKi4A',
    client_secret = 'bhLuvw4cs_bJYr9zYfrAZaHu1gEMJw',
    password = 'DontHackMe!123&Nohacking123',
    user_agent = 'RddtTTSTikTok by /u/park240',
    username = 'park240')


subReddit = reddit.subreddit('AskReddit')
submissionsJson = []

def getTopPostsJson():
    submissionsList = []
    for submission in subReddit.top(limit=5, time_filter="day"):
        submission.comment_sort = "top"
        commentList = []

        try:
            for comment in range(5):
                commentList.append(submission.comments[comment].body)
        except:
            pass
        finally:
            submissionsList.append({"title": submission.title, 
                "selfText": submission.selftext, 
                "comments": commentList})

    global submissionsJson 
    submissionsJson = json.dumps(submissionsList)

def main():
    getTopPostsJson()
    print(submissionsJson)

if __name__ == '__main__':
    main()

