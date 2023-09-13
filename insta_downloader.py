import instaloader

ig = instaloader.Instaloader()

# @public accounts only
# @downloads posts,videos,igtv and reels
def downloadSpecific(shortcode,download_dir):
    post = instaloader.Post.from_shortcode(ig.context,"CtwnoWhqv7N")
    ig.download_post(post,target="reels")

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


# def downloadStories(username,password):
#     profile = ig.check_profile_id(username)

#     ig.download_stories(userids=[profile.userid])
# posts = instaloader.Profile.from_username(ig.context, "elite2002akshay").get_posts()

# print(posts)
#https://www.instagram.com/reel/CtwnoWhqv7N/?igshid=ODVjNmViNDQ0Yw==
# https://www.instagram.com/reel/CxIVxjpv1yq/?utm_source=ig_web_copy_link&igshid=MzRlODBiNWFlZA==
# https://www.instagram.com/p/CxFyxOehzC2/?utm_source=ig_web_copy_link&igshid=MzRlODBiNWFlZA==