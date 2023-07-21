import requests

data = requests.get("https://prices.runescape.wiki/api/v1/osrs/latest").json()
top3 = [1,1,1]
top3_ids = [1,1,1]
top3_names = []
for i in data["data"]:
    
    try:
        data["data"][i]["margin"] = (data["data"][i]["high"]-data["data"][i]["low"])/((data["data"][i]["high"]+data["data"][i]["low"])/2)
        if data["data"][i]["margin"] > float(top3[0]):
            top3[0] = data["data"][i]["margin"]
            top3_ids[0] = i
        elif data["data"][i]["margin"] > float(top3[1]):
            top3[1] = data["data"][i]["margin"]
            top3_ids[1] = i
        elif data["data"][i]["margin"] > float(top3[2]):
            top3_ids[2] = i
            top3[2] = data["data"][i]["margin"]
        
    except TypeError:
        pass
        #print("typerror")

for j in top3_ids:
    data = requests.get("http://services.runescape.com/m=itemdb_oldschool/api/catalogue/detail.json?item=" +j).json()
    top3_names.append(data["item"]["name"])

print(f"""
{top3_names[0]}: {round(top3[0], 2)}% Margin
{top3_names[1]}: {round(top3[1], 2)}% Margin
{top3_names[2]}: {round(top3[2], 2)}% Margin
      """)
