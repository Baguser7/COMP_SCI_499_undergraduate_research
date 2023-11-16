# importing the pandas library 
import pandas as pd 

data = {}
data2 = {}
# reading the csv file 
df = pd.read_csv(r"Dataset\obs_list.csv")
fd = pd.read_csv(r"Dataset\tox_class.csv")  

for n in df.columns:
    data['text'] = df['text']
    data['value'] = df['severity_rating']

for n in fd.columns:
    data2['text'] = fd['comment_text']
    data2['value'] = (fd['toxic'] + fd['severe_toxic'] + fd['obscene'] + fd['threat'] + fd['insult'] + fd['identity_hate'])/2
  
udt = pd.DataFrame(data)
udt2 = pd.DataFrame(data2)
# writing into the file 
udt.to_csv(r"Dataset Updated\obs_list_updt.csv", index=False) 
udt2.to_csv(r"Dataset Updated\tox_class_updt.csv", index=False) 

print(udt)
print(udt2) 