# Get instance
import instaloader
from datetime import datetime
import os
import json

now = datetime.now()
L = instaloader.Instaloader()
labeldate = now.strftime("%Y%m%d")

# Login or load session

# Print list of followees
follow_list = []
followee_list = []


def scrape(boool):
    count = 0
    f = open('uinfo.json')
    json1 = json.load(f)
    username = json1[0]
    password = json1[1]
    print("logging in to instagram\n")
    L.login(username, password)  # (login)
    # Obtain profile metadata
    print("getting metadata\n")
    profile = instaloader.Profile.from_username(L.context, username)
    f.close()
    for followee in profile.get_followers():
        print("loading\n")
        follow_list.append(followee.username)
        if boool:
            file = open(r'original\followers.txt', "a+")
        else:
            file = open(r'followers.txt', "a+")
        file.write(follow_list[count])
        file.write("\n")
        file.close()
        count = count + 1
    print("done loading\n")

def compare():
    followers_old = open(r'original\followers.txt')
    followers_new = open(r'followers.txt')

    old_content = followers_old.read()
    new_content = followers_new.read()

    for word in old_content.split():
        print("comparing\n")
        if word not in new_content:
            print(word)
            print("\n")
            file = open(f'{labeldate}compare.txt', "a+")
            file.write(word)
            file.write("\n")
            file.close()
    print("done comparing\n")
    followers_new.close()
    followers_old.close()
    main()

def main():
    pr1 = "1. Set original followers."
    pr2 = "2. Check followers."
    pr3 = "3. Set user info."
    pr5 = "4. Close"
    pr4 = "Enter option" + "\n"
    print(pr1)
    print(pr2)
    print(pr3)
    print(pr5)
    op1 = input(pr4)
    if op1 == "1":
        boool = True
        file = open(r'original\followers.txt', "a+")
        file.truncate(0)
        scrape(boool)
    if op1 == "2":
        print("Comparing")
        boool = False
        file = open(r'followers.txt', "a+")
        file.truncate(0)
        scrape(boool)
        compare()
    if op1 == "3":
        user = input("Enter instagram username. \n")
        password = input("Enter instagram password. \n")
        with open('uinfo.json', 'w') as f:
            stockdata = [user, password]
            json.dump(stockdata, f)
            main()
    if op1 == "4":
        exit()
    else:
        print("wrong value entered")
        main()

main()
