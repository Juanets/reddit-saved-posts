import praw
import pprint
from auth import *
from collections import defaultdict

r = praw.Reddit(user_agent='get and organize your saved posts')


def login():
    """Login via username and password (deprecated)."""
    r.login(username, password, disable_warning=True)


def get_posts():
    """Get saved posts. Returns list of dicts (posts)."""
    data = []
    for post in r.user.get_saved(limit=None, time='all'):
        if not hasattr(post, 'title'):
            post.title = post.link_title
        try:
            subreddit = str(post.subreddit)
        except AttributeError:
            subreddit = "None"

        data.append({
                'link': post.permalink,
                'title': post.title,
                'sub': subreddit
        })

    return data


def group_by_subreddit(data):
    """Aggregates data by grouping posts by subreddit."""
    grouped = defaultdict(list)
    for post in data:
        grouped[post['sub']].append(
                                {
                                    'link': post['link'],
                                    'title': post['title']
                                }
                            )

    return dict(grouped)


def main():
    login()
    grouped_by_sub = group_by_subreddit(get_posts())
    try:
        pprint.pprint(grouped_by_sub)
    except UnicodeEncodeError:
        pass


if __name__ == '__main__':
    main()
