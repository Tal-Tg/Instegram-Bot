# from anyio import sleep
from threading import main_thread
from instabot import Bot
import time



my_bot = Bot();



# login
my_bot.login(username="tal_golan4",password="Katika1q1wK")
# my_bot.logout();
# result2 = my_bot.logout(username="tal_golan4",password="Katika1q1wK")

# follow user
# my_bot.follow("username")

# follow multi users
# my_bot.follow_users(["",""])

# unfollow the non followers
# my_bot.unfollow_non_followers();

# uplaod a photo
# my_bot.upload_photo("pyhon.jpg", captions="Pytube | Creates your own youtube video downloader using python");


# send message to user
# my_bot.send_message("content", "usename")

# like a post              
                            #user 2 last post can do it by array also []   
# my_bot.like_user("user_id",amount=2);



# comment
# user_id = my_bot.get_user_id_from_username("dana_sh15")
# media_id = my_bot.get_last_user_medias(user_id)
# my_bot.comment(media_id," אוהב אותך ")


# get list of followers of anyone
followers_list = my_bot.get_user_followers("dana_sh15")

for count,each_followers in enumerate(followers_list):
    if count > 4:
        continue;
    time.sleep(20)
    print(my_bot.get_username_from_user_id(each_followers))
    
    
# get list of following of anyone
following_list = my_bot.get_user_following("dana_sh15")

for count1,each_following in enumerate(following_list):
    if count1 > 4:
        continue;
    time.sleep(20)
    print(my_bot.get_username_from_user_id(each_following))
    
my_bot.logout();