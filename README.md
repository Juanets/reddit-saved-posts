# reddit-saved-posts
groups your saved posts by subreddit (WIP)

## usage
install PRAW (reddit's api wrapper for python)    
```
pip install -r requirements.txt
```
or simply  
```
pip install praw==3.6
```
  
then just enter your username and password in `auth.py`  
after that, run 
```
run.py
```
you should get a dictionary containing all your saved posts, grouped by subreddit :)

## todo
* OAuth authentication (tokens)
* web app that shows your saved posts
