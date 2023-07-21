import requests

class Logic:
    def run_logic():
        data = requests.get("https://prices.runescape.wiki/api/v1/osrs/latest").json()
        top10 = [1,1,1,1,1,1,1,1,1,1]
        top10_ids = [1,1,1,1,1,1,1,1,1,1]
        top10_names = []
        for i in data["data"]:
            
            try:
                data["data"][i]["margin"] = (data["data"][i]["high"]-data["data"][i]["low"])/((data["data"][i]["high"]+data["data"][i]["low"])/2)
                if data["data"][i]["margin"] > float(top10[0]):
                    top10[0] = data["data"][i]["margin"]
                    top10_ids[0] = i
                elif data["data"][i]["margin"] > float(top10[1]):
                    top10[1] = data["data"][i]["margin"]
                    top10_ids[1] = i
                elif data["data"][i]["margin"] > float(top10[2]):
                    top10_ids[2] = i
                    top10[2] = data["data"][i]["margin"]
                elif data["data"][i]["margin"] > float(top10[3]):
                    top10_ids[3] = i
                    top10[3] = data["data"][i]["margin"]
                elif data["data"][i]["margin"] > float(top10[4]):
                    top10_ids[4] = i
                    top10[4] = data["data"][i]["margin"]
                elif data["data"][i]["margin"] > float(top10[5]):
                    top10_ids[5] = i
                    top10[5] = data["data"][i]["margin"]
                elif data["data"][i]["margin"] > float(top10[6]):
                    top10_ids[6] = i
                    top10[6] = data["data"][i]["margin"]
                elif data["data"][i]["margin"] > float(top10[7]):
                    top10_ids[7] = i
                    top10[7] = data["data"][i]["margin"]
                elif data["data"][i]["margin"] > float(top10[8]):
                    top10_ids[8] = i
                    top10[8] = data["data"][i]["margin"]
                elif data["data"][i]["margin"] > float(top10[9]):
                    top10_ids[9] = i
                    top10[9] = data["data"][i]["margin"]
            except TypeError:
                pass
                

        for j in top10_ids:
            data = requests.get("http://services.runescape.com/m=itemdb_oldschool/api/catalogue/detail.json?item=" +str(j)).json()
            top10_names.append(data["item"]["name"])

        print(f"""
{top10_names[0]}: {round(top10[0], 2)}% Margin
{top10_names[1]}: {round(top10[1], 2)}% Margin
{top10_names[2]}: {round(top10[2], 2)}% Margin
{top10_names[3]}: {round(top10[3], 2)}% Margin
{top10_names[4]}: {round(top10[4], 2)}% Margin
{top10_names[5]}: {round(top10[5], 2)}% Margin
{top10_names[6]}: {round(top10[6], 2)}% Margin
{top10_names[7]}: {round(top10[7], 2)}% Margin
{top10_names[8]}: {round(top10[8], 2)}% Margin
{top10_names[9]}: {round(top10[9], 2)}% Margin
            """)
