import requests
from bs4 import BeautifulSoup
import re

print("""\033[91m
                              
                (     (                      
                )\ )  )\    )     )      (   
               (()/( ((_)( /(    (      ))\  
                /(_)) _  )(_))   )\  ' /((_) 
               (_) _|| |((_)_  _((_)) (_))   
                |  _|| |/ _` || '  \()/ -_)  
                |_|  |_|\__,_||_|_|_| \___|  
                                             
""")

def get_bio(soup):
    bio_tag = soup.find('meta', property='og:description')
    bio_text = bio_tag['content'] if bio_tag else "N/A"
    return bio_text

def get_comments_count(soup):
    comments_tag = soup.find('span', class_='g47SY')
    comments_text = comments_tag.text if comments_tag else "N/A"
    return comments_text

def get_followers_count(soup):
    followers_section = soup.find('meta', property='og:description')['content']
    followers_count = re.search(r'(\d+)[^\d]*(\d+)', followers_section).group(1)
    return followers_count

def get_following_count(soup):
    followers_section = soup.find('meta', property='og:description')['content']
    following_count = re.search(r'(\d+)[^\d]*(\d+)', followers_section).group(2)
    return following_count

def get_posts_count(soup):
    posts_count = soup.find('span', class_='g47SY').text
    return posts_count

def get_profile_pic_url(soup):
    profile_pic_url = soup.find('meta', property='og:image')['content']
    return profile_pic_url

def get_instagram_info(username, option):
    # تكوين رابط الحساب باستخدام اسم المستخدم
    profile_url = f"https://www.instagram.com/{username}/"

    # إرسال طلب للحصول على محتوى الصفحة
    response = requests.get(profile_url)
    soup = BeautifulSoup(response.content, 'html.parser')

    if option == '1':
        print("\033[93m" + "Bio:", get_bio(soup))
    elif option == '2':
        print("\033[93m" + "Comments count:", get_comments_count(soup))
    elif option == '3':
        print("\033[93m" + "Followers count:", get_followers_count(soup))
    elif option == '4':
        print("\033[93m" + "Following count:", get_following_count(soup))
    elif option == '5':
        print("\033[93m" + "Posts count:", get_posts_count(soup))
    elif option == '6':
        print("\033[93m" + "Profile picture URL:", get_profile_pic_url(soup))
    elif option == '99':
        print("\033[93m" + "Exiting...")
    else:
        print("\033[93m" + "Invalid option.")

print("\033[93m" + "My Instagram: https://www.instagram.com/2k__.p")

print("\033[93m" + "Choose an option:")
print("\033[93m" + "1. Copy bio")
print("\033[93m" + "2. Search for total comments count")
print("\033[93m" + "3. Followers count")
print("\033[93m" + "4. Following count")
print("\033[93m" + "5. Posts count")
print("\033[93m" + "6. Profile picture URL")
print("\033[93m" + "99. Exit")

while True:
    choice = input("\033[93m" + "Enter your choice: ")

    if choice == '99':
        break
    elif choice in ['1', '2', '3', '4', '5', '6']:
        username = input("\033[93m" + "Enter the Instagram username: ")
        get_instagram_info(username, choice)
    else:
        print("\033[93m" + "Invalid choice. Please enter a valid option.")