from app.reddit import oauth, get_posts, group_by_subreddit, set_user
from flask import render_template, url_for, redirect, request
from app import app


@app.route('/')
def index():
	return render_template('index.html')


@app.route('/oauth')
def authentication():
	return redirect(oauth())


@app.route('/oauth_callback')
def oauth_callback():
	code = request.args.get('code')
	set_user(code)

	return redirect(url_for('get_saved'))


@app.route('/saved')
def get_saved():
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
