from instapy import InstaPy
from time import sleep
accounts = ["onlyfans_rw",
            "onlyfans_jct",
            "onlyfans_gt",
            "onlyfans_kk",
            "onlyfans_yt",
            "onlyfans_stj"]
tags = ["onlyfangirls",
        "girlsofonlyfans",
        "onlyfan",
        "onlyfanz",
        "onlyfanspromotions",
        "onlyfangirl",
        "onlyfanaccount",
        "onlyfanaccounts",
        "onlyfanpage",
        "feetfetishworld",
        "findom",
        "footfetish",
        "feetporn"]
comments = [u'Exotic🔥! DM💌 us @ only.fans_babes 🌶️ to reach out 1M + admirers🥵.  # onlyfanspromotions #🍑',
            u'Charming💋! Let us promote❤️ you over a network of 1M+.DM💌 us @only.fans_babes 🌶️ #onlyfan #🥵',
            u'Sensational🥵 content bae❤️! DM💌 us @only.fans_babes 🌶️ to get promotion🔥 #million  #sexy',
            u'Hot AF babe! @{}. Let us help❤️ you grow your audience #🥵 . DM💌 us @only.fans_babes',
            u'Salacious🤤 babe💋! @{}. DM💌 us @only.fans_babes to reach out 1M+ #🍑 admirers!']

for i in range(len(accounts)):
    ID = accounts[i]
    session = InstaPy(username=ID, password="OnlyFans@20")
    session.login()
    session.set_relationship_bounds(enabled=True, max_followers=500)
    session.set_do_follow(True, percentage=50)
    session.set_do_comment(enabled=True, percentage=50)
    session.set_comments(comments)
    session.like_by_tags(tags=tags, amount=8, skip_top_posts=True)
    session.end()
    sleep(3600)
