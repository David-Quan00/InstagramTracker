# InstagramTracker

Sometimes people unfollow you on Instagram and that's life; people grow apart.  You see your following count decrease and can't help but wonder who unfollowed you.

Unfortunately there is no feature on Instagram to see who has unfollowed you, only third party trackers, in which privacy should be a concern.

This script will parse the json files for my following and followers files (downloaded and obtained via instagram), compare the two lists, and output users that only appear in one of the lists.

---------------
# Testing the Code:

I uploaded some test JSON files rather than my actual following and follower data.  Here we had:

Followers: jlin7, jeremyzucker, teddysphotos, nikizefanya

Following: taylorswift, jlin7, jeremyzucker, nikizefanya, therock

Output should be who appears in our following list but no longer is in our followers list, so taylorswift and therock.
