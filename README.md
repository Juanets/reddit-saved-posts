# reddit-saved-posts
groups your saved posts by subreddit (WIP)

## usage
install Flask and PRAW (reddit's api wrapper for python)  
```
pip install -r requirements.txt
```
  
then just enter your username and password in `app/auth.py`  
after that, run 
```
python run.py
```
a flask server should start on `127.0.0.1:5000` and on route `/` you should get a dictionary containing all your saved posts, grouped by subreddit :)

## todo
* add html and css
* OAuth authentication (tokens)
