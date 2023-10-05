'''
    Description: Sometimes people unfollow you on Instagram and that's life; people grow apart.
                 You see your following count decrease and can't help but wonder who unfollowed you.
                 Unfortunately there is no feature to see who has unfollowed you, only third party trackers.
                 This script will read the json files for my following and followers files (obtained by instagram).
                 Then will compare the two.
    Date: July 23, 2022
    Authour: David Q
'''

import json

### For the followers File ###
# Opening JSON file
f = open('followers.json')
  
# returns JSON object as a dictionary
data = json.load(f)
  
# Create a list for followers
lst_followers = []

# Parse the json file, extract all my followers, and place in the list: lst_followers
for i in data['relationships_followers']:
    for j in i["string_list_data"]:
        lst_followers.append(j["value"])

print("List of my Follwoers:")
print(lst_followers)
print()

# Closing file
f.close()

print("Now Looking at the people I follow:")

### For the followers File ###
f = open('following.json')
data = json.load(f)
lst_following = []
for i in data['relationships_following']:
    for j in i["string_list_data"]:
        lst_following.append(j["value"])
print(lst_following)
print()
# Closing file
f.close()

# Loose verification to see if my code worked
print("Number of followers:")
print(len(lst_followers))
print("Number following:")
print(len(lst_following))
print()
# Checks out with my current followers vs following count

# Create a master list containing my followers AND following
both_lst = []
both_lst = lst_followers + lst_following
# print(both_lst)

# Iterate through and print the accounts that I follow, but dont follow me.
# Really this is either one of two cases:
# (1) I follow and they don't follow me back OR (2) They follow me and I don't follow back (which I don't unfollow people)
print("The individuals that either: Only I follow (they dont follow me back), or they follow me (and I dont follow back):")
# Compare:
for element in both_lst:
    if element not in lst_followers and element in lst_following:
        print(element)
        
