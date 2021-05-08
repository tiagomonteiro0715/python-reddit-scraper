import praw
import csv

reddit = praw.Reddit(client_id='c2QPqxiW92oiHQ', client_secret='8K3ZZNs9X_eadeKPEqZrZU8x_sOMyg', user_agent='top-1000-posts')

top_posts = reddit.subreddit('Entrepreneur').top(limit=500)

with open('top_1000.csv', 'w', newline='') as csvfile:
    fieldnames = ['title','score','num_comments','author']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for post in top_posts:
        writer.writerow({
            'title': post.title,
            'score': post.score,
            'num_comments': post.num_comments,
            'author': post.author
            })