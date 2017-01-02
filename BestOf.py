#ProRevenge Best of 2016 script by /u/pun-master-general
#Returns nominations and scores for ProRevenge Best of 2016 contest
#Written in python v3.5.2, PRAW v.4.1.0

import praw
ofp = open('bestof2016.txt', 'w')
reddit = praw.Reddit(client_id='[client id]',
                     client_secret='[client secret]',
                     user_agent='Best of script v1.0 by /u/pun-master-general',
                     username='[username]',
                     password='[password]')
submission = reddit.submission(id='[id]') #ID of the Best Of submission
categories = list(submission.comments)
for comment in categories: #top level comments are categories
    if (comment.id != '[excluded comment ID]' and comment.id != '[excluded comment ID]'): #excludes certain comments (ie. general discussion)
        ofp.write("___________\n**" + comment.body + "**\n\n")
        noms = comment.replies #replies to categories are nominations
        nom = {}
        for reply in noms:
            nom[reply.score] = reply.body
        i = 3 #returns the top 3 in each category
        for key in sorted(nom.keys(), reverse = True):
            if i > 0:
                s = str(key)
                ofp.write('* ' + s + ' ' + nom[key] + '\n\n')
                i = i - 1
ofp.close()
print('Success!')
