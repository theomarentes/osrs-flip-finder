import requests

data = requests.get("https://prices.runescape.wiki/api/v1/osrs/latest").json()
print(len(data["data"]))
top3 = [1,1,1]
for i in range(0, len(data["data"])):
    data["data"][i]["margin"] = (data["data"][i]["high"]-data["data"][i]["low"])/((data["data"][i]["high"]+data["data"][i]["low"])/2)

    if data["data"][i]["margin"] > top3[0]:
        top3[0] = data["data"][i]["margin"] + " " + i
    if data["data"][i]["margin"] > top3[1]:
        top3[1] = data["data"][i]["margin"] + " " + i
    if data["data"][i]["margin"] > top3[2]:
        top3[2] = data["data"][i]["margin"] + " " + i
print(top3)