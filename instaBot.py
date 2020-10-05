import logging.config
from selenium import webdriver
from time import sleep
import logging
import sqlite3
from random import randint
from selenium.webdriver.common.action_chains import ActionChains


accounts = [  # * Accounts to be used
    # ! "onlyfans_rw",
    "onlyfans_yt.m",
    "onlyfans_stj.m",
    "onlyfans_gt.m",
    "onlyfans_jct.m",
    # ! "onlyfans_kk.m",
]
tags = [  # * Tags to be searched
    "onlyfangirls",
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
    "feetporn"
]
comments = [  # * Comments to be posted
    u'Exotic🔥 @{}! DM💌 us @only.fans_babes 🌶️ to reach out 1M + admirers🥵.  #onlyfanspromotions #🍑',
    u'Charming💋 @{}! Let us promote❤️ you over a network of 1M+.DM💌 us @only.fans_babes 🌶️ #onlyfan #🥵',
    u'Sensational🥵 content bae❤️! @{} DM💌 us @only.fans_babes 🌶️ to get promotion🔥 #million  #sexy',
    u'Hot AF 🔥babe! @{}. Let us help❤️ you grow your audience #🥵 . DM💌 us @only.fans_babes',
    u'Salacious🤤 babe💋! @{}. DM💌 us @only.fans_babes to reach out 1M+ #🍑 admirers!',
    u'📸This shot is really so lovely @{} if you want we can share the post direct message me 📩📩💯💯'
]
messages = [  # * Messages to be sent as DM
    u'Hey babe! Great profile. Get promotion on our network of 1 Million+🔥 people from across the globe and become a sensation DM💌 us at https://instagram.com/only.fans_babes ',
    u'Great profile❤️! Let\'s get you a promotion🔥 on a network of over 2 Million 🍑 admirers from across the globe. DM💌 us at https://instagram.com/only.fans_babes 🌶️',
    u'Nice content🤤! Wanna get promotion🔥 across a network of over 1 Million 🍑 seekers😈. DM💌 us at https://instagram.com/only.fans_babes and become a sensation💋.',
    u'Great figure🍑 babe💋! We have an offer for you to reach out 1 Million+🤤 admirers 🥵 and become a sensation🔥. DM💌 us at https://instagram.com/only.fans_babes.'
]
bad_words = [  # * Words not to be interacted with
    u'promotion',
]
bad_username = [  # * Words that should not be present in username
    u'only',
    u'shoutout',
    u'promo',
    u'fan'
]


class Bot:
    def __init__(self):
        self.elements = {
            "home_to_login_button": ".WquS1 a",
            "username_field": "div.-MzZI:nth-child(1) > div:nth-child(1) > label:nth-child(1) > input:nth-child(2)",
            "password_field": "div.-MzZI:nth-child(2) > div:nth-child(1) > label:nth-child(1) > input:nth-child(2)",
            "button_login": ".L3NKy",
            "search_field": "input.XTCLo.x3qfX.focus-visible",
            "search_user": "queryBox",
            "select_user": "div._7UhW9.xLCgt.qyrsm.KV-D4.uL8Hv",
            "select_userB": ".cB_4K",
            "textarea": ".ItkAi > textarea:nth-child(1)",
            "send": "div.JI_ht:nth-child(3) > button:nth-child(1)",
            "profile_button": "span.qNELH > img:nth-child(1)",
            "logout_button": "div._7UhW9.xLCgt.MMzan.KV-D4.fDxYl"
        }

        self.driver = webdriver.Firefox()
        # self.driver.set_window_position(0, 0)
        # self.driver.minimize_window()

    def login(self, username, password):  # * successful
        drive = self.driver
        drive.get('https://www.instagram.com')
        try:
            drive.find_element_by_css_selector(
                self.elements['username_field']).send_keys(username)
            print('Username filled')
            drive.find_element_by_css_selector(
                self.elements['password_field']).send_keys(password)
            print('Pass filled')
            drive.find_element_by_css_selector(
                self.elements['button_login']).click()
            print('Login Clicked')
        except Exception as e:
            print(e)
        sleep(2)

    def logout(self):  # * successful
        try:
            drive = self.driver
            drive.find_element_by_css_selector(
                self.elements['profile_button']).click()
            drive.find_elements_by_css_selector(
                self.elements['logout_button'])[7].click()
            sleep(2)
        except Exception as e:
            input("An error occured in log-out!")
            print(e)

    def search_hashtag(self, hashtag):  # * successful
        drive = self.driver
        drive.get('https://www.instagram.com/explore/tags/'+hashtag+'/')
        sleep(2)

    def get_links_by_tag(self, hashtag: str, amount=50):  # * successful
        insta.search_hashtag(hashtag)
        posts = set()
        try:
            Recent = self.driver.find_element_by_css_selector(
                '.KC1QD > div:nth-child(3) > div:nth-child(1)')
            Cposts = Recent.find_elements_by_tag_name(
                'a')
            for elem in Cposts:
                posts.add(elem.get_attribute('href'))
            while len(posts) < amount+20:
                self.driver.execute_script(
                    "window.scrollTo(0, document.body.scrollHeight);")
                sleep(4)
                Recent = self.driver.find_element_by_css_selector(
                    '.KC1QD > div:nth-child(3) > div:nth-child(1)')
                Cposts = Recent.find_elements_by_tag_name(
                    'a')
                for elem in Cposts:
                    posts.add(elem.get_attribute('href'))
                print('posts:', len(posts))
        except Exception as e:
            print("Error in getting links")
            print(e)
        return list(posts)

    def list_usernames(self, amount=50):  # * successful
        drive = self.driver
        count = 0
        hashtag = input('Enter Hashtag: ')
        try:
            posts = self.get_links_by_tag(hashtag)
            for element in posts:
                drive.get(str(element))
                try:
                    username = drive.find_element_by_css_selector(
                        '.e1e1d > span:nth-child(1) > a:nth-child(1)').text
                except:
                    continue
                try:
                    data.insert_in_accounts(username)
                    count += 1
                    print(count, ':', 'Link:', element,
                          '| username:', username, flush=True)
                except Exception as e:
                    print('Error in DB saving')
                    print(e)
        except Exception as e:
            input("An error occured in listing!")
            print(e)

    def sendMessage(self, user, message):  # ! Issue of "notification" pop-up from Instagram
        self.driver.get('https://www.instagram.com/direct/new/')
        self.driver.find_element_by_name(
            self.elements['search_user']).send_keys(user)
        sleep(1.5)
        # Select user
        self.driver.find_element_by_css_selector(
            self.elements['select_user']).click()
        sleep(1)
        # Go to page
        self.driver.find_element_by_css_selector(
            self.elements['select_userB']).click()
        sleep(1)
        self.driver.find_element_by_css_selector(
            self.elements['textarea']).send_keys(message)
        sleep(1)
        self.driver.find_element_by_css_selector(
            self.elements['send']).click()
        sleep(1)
        """ if self.conn != None:
            self.cursor.execute(
                'INSERT INTO message (username, message) VALUES(?, ?)', (user, message))
            self.conn.commit() """

    def bulkDM(self, num: int):
        try:
            count = 0
            users = data.cursor.execute(
                'SELECT username FROM accounts').fetchall()
            for user in users:
                if data.getDM(user) == 0:
                    p = randint(0, 3)
                    message = messages[p]
                    self.sendMessage(user, message)
                    data.insert_in_dm(user)
                    print("Sent", p, "to", user)
                    count += 1
                    if count % 5 == 0:
                        sleep(200)
        except Exception as e:
            input("Error in Bulk DM!")
            print(e)
        print('Updated', count, 'DMs into data!')

    def comment(self, count=0):
        drive = self.driver
        try:
            for element in posts[count:]:
                if count == 18:
                    break
                drive.get(str(element))
                try:
                    username = drive.find_element_by_css_selector(
                        '.e1e1d > span:nth-child(1) > a:nth-child(1)').text
                except:
                    continue
                check = [i for i in bad_username if i in username]
                if check:
                    continue
                try:
                    data.insert_in_accounts(username)
                except Exception as e:
                    print(e)
                try:
                    if data.getComment(username) == 0:
                        comment = comments[randint(0, len(comments)-1)]
                        cBox = drive.find_element_by_css_selector(
                            '.Ypffh')
                        like = drive.find_element_by_css_selector(
                            '.fr66n > button:nth-child(1) > div:nth-child(1) > span:nth-child(1) > svg:nth-child(1)')
                        postButton = drive.find_element_by_css_selector(
                            '.X7cDz > button:nth-child(2)')
                        ActionChains(drive).move_to_element(
                            like).click().move_to_element(
                            cBox).click().send_keys(comment.format(username)).move_to_element(postButton).click().perform()
                        sleep(2)
                        count += 1
                        print('count:', count, flush=True)
                        try:
                            data.insert_in_comments(username, element)
                            data.updateComment(username)
                            data.DB.commit()
                        except Exception as e:
                            print(e)
                            input("Error in DB comments update!")
                except:
                    pass
                if count % 6 == 0:
                    sleep(150)
        except Exception as e:
            input("An error occured in Commenting!")
            print(e)
        print('Updated', count, 'comments into data!')
        data.DB.commit()
        return count


class sqlDB:
    def __init__(self, file: str):
        self.DB = sqlite3.connect(file)
        self.cursor = self.DB.cursor()

    def insert_in_accounts(self, username: str):
        sql = 'INSERT INTO accounts (username) VALUES (?)'
        self.cursor.execute(sql, (username,))

    def insert_in_comments(self, username: str, postLink: str):
        userID = self.getID(username)
        sql = 'INSERT INTO comments (userID,postLink) VALUES (?,?)'
        self.cursor.execute(sql, (userID, postLink,))

    def insert_in_dm(self, username: str):
        userID = self.getID(username)
        sql = 'INSERT INTO comments (userID) VALUES (?)'
        self.cursor.execute(sql, (userID,))

    def getID(self, username: str):
        try:
            return self.cursor.execute('SELECT id FROM accounts WHERE username=?', (username,)).fetchone()[0]
        except:
            return False

    def getComment(self, username: str):
        return self.cursor.execute('SELECT commentFlag FROM accounts WHERE username=?', (username,)).fetchone()[0]

    def getDM(self, username: str):
        return self.cursor.execute('SELECT dmFlag FROM accounts WHERE username=?', (username,)).fetchone()[0]

    def updateDM(self, username: str):
        self.cursor.execute(
            'UPDATE accounts SET dmFlag=1 WHERE username=?', (username,))

    def updateComment(self, username: str):
        self.cursor.execute(
            'UPDATE accounts SET commentFlag=1 WHERE username=?', (username,))


logging.config.fileConfig(fname='logger.conf')
log = logging.getLogger(__name__)
data = sqlDB('InstaBot.db')
insta = Bot()
posts = insta.get_links_by_tag(tags[randint(0, len(tags)-1)])
insta.driver.implicitly_wait(10)
for username in accounts:
    log.info(f'Starting by ID: {username}')
    count = 0
    insta.login(username, 'OnlyFans@20')
    """ k = 3  # int(input('What to do:\n1. Listing\n2. DM\n3. Comments\n'))
    if k == 2:
        insta.bulkDM(int(input("Enter intial point of user: ")))
    elif k == 3: """
    count = insta.comment(count)
    log.info(f'Commented on {count} posts from "{username} account')
    sleep(1)
    insta.logout()
insta.driver.close()
