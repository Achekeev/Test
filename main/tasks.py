from main.models import Post
import schedule
import time


def set_default():
    votes_count = Post.objects.all().update(amounts_of_upvotes=0)
    return votes_count


schedule.every().day.at("11:30").do(set_default)
while True:
    schedule.run_pending()
    time.sleep(360)