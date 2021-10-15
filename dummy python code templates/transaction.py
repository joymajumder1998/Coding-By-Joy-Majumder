def transaction(transactions):
    ts1=int(transactions[0].split(",")[1])
    ts2=int(transactions[1].split(",")[1])
    money1=int(transactions[0].split(",")[2])
    money2=int(transactions[1].split(",")[2])
    name1=transactions[0].split(",")[0]
    name2=transactions[1].split(",")[0]
    city1=transactions[0].split(",")[3]
    city2=transactions[1].split(",")[3]
    if(ts2-ts1<60):
        if(name1==name2):
            if(city1!=city2):
                return transactions
            else:
                return [transactions[1]]
    if(money1>1000):
        return [transactions[0]]
    elif(money2>1000):
        return [transactions[1]]
    elif(money1>1000 and money2>1000):
        return transactions