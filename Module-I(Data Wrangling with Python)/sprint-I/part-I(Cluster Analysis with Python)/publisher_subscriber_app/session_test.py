from pubsub import *
from pprint import pprint

def main():
    post_message("ibsa", "hello this is me posting first message")
    post_message("ibsa", "hello this is me posting second message")
    post_message("kena", "hello this is kena posting first message")

    # follower
    follow('ibsa', 'kena')


if __name__=="__main__":
    main()
    # pprint(user_posts['ibsa'])
    pprint(followers)