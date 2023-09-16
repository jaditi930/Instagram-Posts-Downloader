import instaloader
import threading
ig = instaloader.Instaloader()


# @public accounts only
# @downloads posts,videos,igtv and reels
def dp(username):
    t1 = threading.Thread(target=download_profile, args=(username,))
    t1.start()
    # t1.join()

def ds(shortcode,download_dir="reels"):
    t1 = threading.Thread(target=downloadSpecific, args=(shortcode,download_dir,))
    t1.start()

def downloadSpecific(shortcode,download_dir):
    post = instaloader.Post.from_shortcode(ig.context,shortcode)
    ig.download_post(post,target=download_dir)

#@ public and private
#@download profile pic
def download_profile(username):
    ig.download_profile(username , profile_pic_only=True)

# @public accounts only
# @downloads all posts,videos and reels
def downloadAllPosts(username):
    profile = instaloader.Profile.from_username(ig.context,username)

    for post in profile.get_posts():
        ig.download_post(post, target=profile.username)

# requires login
# @ downloads stories of public accounts

# download_profile("jaditi930")

# def downloadStories(username,password):
#     profile = ig.check_profile_id(username)

#     ig.download_stories(userids=[profile.userid])
# posts = instaloader.Profile.from_username(ig.context, "elite2002akshay").get_posts()

# print(posts)
#https://www.instagram.com/reel/CtwnoWhqv7N/?igshid=ODVjNmViNDQ0Yw==
# https://www.instagram.com/reel/CxIVxjpv1yq/?utm_source=ig_web_copy_link&igshid=MzRlODBiNWFlZA==
# https://www.instagram.com/p/CxFyxOehzC2/?utm_source=ig_web_copy_link&igshid=MzRlODBiNWFlZA==