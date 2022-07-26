import datetime
import json
import random
import datetime
def signup(qq:str): 
    try:
        with open("./data/"+str(qq)+".json","r",errors='ignore') as f:
            data2 = json.load(f)
            coin=data2['coin']
            signtimes=data2['sign_times']
            last_sign=data2['last_sign']
            f.close()
        tsnow=datetime.datetime.now().strftime("%Y-%m-%d")
        ts=datetime.datetime.strptime(tsnow, "%Y-%m-%d")
        tspast=datetime.datetime.strptime(str(last_sign),"%Y-%m-%d")
        if (ts-tspast).days > 0.5:
            coin = coin + random.randint(100,200)
            signtimes += 1
            last_sign =datetime.datetime.now().strftime("%Y-%m-%d")
            with open("./data/"+str(qq)+".json","w") as f:
                data={"qq": qq, "coin": coin, "sign_times": signtimes, "last_sign": last_sign}
                json.dump(data,f)
                f.close()
            return [coin,signtimes,last_sign]
        else:
            return ["Already signed"]
    except FileNotFoundError as fnfe:
        with open("./data/"+str(qq)+".json","w") as f:
            data = {
                'qq' : qq,
                'coin' : random.randint(0,100),
                'sign_times' : 1,
                'last_sign': str(datetime.datetime.now().strftime("%Y-%m-%d"))
            }
            json_str = json.dump(data,f)
            f.close()
        with open("./data/"+str(qq)+".json","r",errors='ignore') as f:
            data2 = json.load(f)
            coin=data2['coin']
            signtimes=data2['sign_times']
            last_sign=data2['last_sign']
            f.close()
        return [coin,signtimes,last_sign]

