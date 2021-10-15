import pandas as pd

table=pd.DataFrame(columns=("ID","NAME"))
table.loc[0]=1,"Joy"
table.loc[1]=2,"Jisha"
print(table)