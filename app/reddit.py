import praw
from app.auth import *
from collections import defaultdict

r = praw.Reddit(user_agent='get and organize your saved posts')


def oauth():
    """Get reddit's authentication url."""
    r.set_oauth_app_info(client_id = client_id,
                        client_secret = client_secret,
                        redirect_uri = redirect_uri)
    
    oauth_url = r.get_authorize_url('lopezdoriga', 'identity history', True)

    return oauth_url

def set_user(token):
    try:
        r.get_access_information(token)
        return True
    except Exception as e:
        return str(e)

def get_posts():
    """Get saved posts. Returns list of dicts (posts)."""
    data = []
    for post in r.user.get_saved(limit = None, time = 'all'):
        if not hasattr(post, 'title'):
            post.title = post.link_title
        try:
            subreddit = str(post.subreddit)
        except AttributeError:
            subreddit = "None"

        data.append({
                'link': post.permalink,
                'title': post.title,
                'sub': subreddit,
                'score': post.score
        })

    return data


def group_by_subreddit(data):
    """Aggregates data by grouping posts by subreddit."""
    grouped = defaultdict(list)
    for post in data:
        grouped[post['sub']].append(
                                {
                                    'link': post['link'],
                                    'title': post['title'],
                                    'score': int(post['score'])
                                }
                            )

    return dict(grouped)
