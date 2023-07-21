import requests

data = requests.get("https://prices.runescape.wiki/api/v1/osrs/latest").json()
print(len(data["data"]))

for i in range(0, len(data["data"])):
    data["data"][i]["margin"] = (data["data"][i]["high"]-data["data"][i]["low"])/((data["data"][i]["high"]+data["data"][i]["low"])/2)

