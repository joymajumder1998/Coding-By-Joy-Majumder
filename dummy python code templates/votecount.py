def majorityVote(votes):
    vote_count={}
    for vote in votes:
        if(vote in vote_count):
            vote_count[vote]+=1
        else:
            vote_count[vote]=1
    maxvote=max(vote_count.values())
    winners=[]
    for item,vote in vote_count.items():
        if(vote==maxvote):
            winners.append(item)
    return random.choice(winners)
