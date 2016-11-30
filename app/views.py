from app.reddit import login, get_posts, group_by_subreddit
from flask import render_template
from app import app


@app.route('/')
def index():
	login()
	saved = group_by_subreddit(get_posts())
	return render_template('index.html', saved=saved)


# 404
@app.errorhandler(404)
def page_not_found(e):
	return 'Not Found (404)', 404


# 500
@app.errorhandler(500)
def internal_error(e):
	return 'Internal Server Error (500)', 500
