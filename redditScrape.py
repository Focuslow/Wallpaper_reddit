import praw
from prawcore.exceptions import Redirect, NotFound
import os


def scrape(text):
    if os.path.exists(text):
        if os.path.isdir(text):
            return ["dir", text]
        elif os.path.isfile(text):
            return ["file", text]

    else:
        reddit = praw.Reddit(client_id='gUbfhv6mnICeQw', \
                             client_secret='gW-1bXg3YpB-3_jD-XKxsQIXxeM', \
                             user_agent='Wallpaper_changer', \
                             username='Test_py_Runner', \
                             password='PyScrp01tst')

        if "r/" in text:
            index = text.find("r/")
            text = text[(index + 2):]

        try:
            subreddit = reddit.subreddit(text)
            icon = subreddit.icon_img
            title = subreddit.title
        except Redirect:
            return 0 #wrong rddt

        except NotFound:
            return 0 #wrong rddt

        top_posts = subreddit.top('day', limit=10)
        lst = list(top_posts)
        if len(lst)==0:
            return 1 # no posts

        for post in lst:
            if post.url[-3:] != "jpg":
                continue
            else:
                url = post.url
                return ["url",[title,url,icon]]

        return 2 # no img posts in 10 tops

