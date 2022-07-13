import miraicle
import requests
import json
from configparser import ConfigParser# 读取配置, 加载配置项
import blacklistsutil
import signutil
import transfur
def getport():
    config = ConfigParser()
    config.read('./config/main.conf', encoding='UTF-8')
    return str(config['flaskconf']['port'])
def getFursuitRand():
    r =  requests.get("http://127.0.0.1:"+getport()+"/getFursuitRand")
    json_str = json.loads(r.text)
    return json_str
def getFursuitByName(name):
    r =  requests.get("http://127.0.0.1:"+getport()+"/getFursuitByName/"+name)
    json_str = json.loads(r.text)
    return json_str
def getFursuitByID(furid):
    r =  requests.get("http://127.0.0.1:"+getport()+"/getFursuitByID/"+furid)
    json_str = json.loads(r.text)
    return json_str
def DailyFursuitByID(furid):
    r =  requests.get("http://127.0.0.1:"+getport()+"/DailyFursuit/id/"+furid)
    json_str = json.loads(r.text)
    return json_str
def DailyFursuitByName(name):
    r =  requests.get("http://127.0.0.1:"+getport()+"/DailyFursuit/name/"+name)
    json_str = json.loads(r.text)
    return json_str
def DailyFursuitRand():
    r =  requests.get("http://127.0.0.1:"+getport()+"/DailyFursuit/Rand/")
    json_str = json.loads(r.text)
    return json_str
def permutil(qq:str,req:int):
    try:
        foo = ConfigParser()
        foo.read('./config/main.conf', encoding='UTF-8')
        level = foo['admin'][str(qq)]
        if int(level) >= req:
            return True
    except KeyError as ke:
        return False
@miraicle.Mirai.receiver('GroupMessage')
def hello_to_group(bot: miraicle.Mirai, msg: miraicle.GroupMessage):
    if msg.plain in ['help', '.help','/help','~help','帮助','.帮助','/帮助','~帮助']:
            helper = ConfigParser()
            helper.read('./config/main.conf', encoding='UTF-8')
            bot.send_group_msg(group=msg.group, msg=[miraicle.Plain(helper['mirai']['help'])])
        #if msg.plain in [str("来只 "+re.fullmatch('(?<=来只 ).*$', msg.plain)[0])]:
    try:
        if msg.plain in ["来只 "+msg.plain.split(" ")[1]]:
                # r =  requests.get("http://192.168.1.12:9000/getFursuitByName/"+str(re.fullmatch('(?<=来只 ).*$', msg.plain)[0]))
                # json_str = json.loads(r.text)
            json_raw = getFursuitByName(msg.plain.split(" ")[1])
            furid = json_raw['data']['id']
            name=json_raw['data']['name']
            thumb=json_raw['data']['url']
            bot.send_group_msg(group=msg.group, msg=[miraicle.Plain('--- 每日吸毛 Bot ---\n今天你吸毛了嘛？\nFurID:'+str(furid)+'\n毛毛名字：'+name+'\n搜索方法：模糊\n'),miraicle.Image(url=thumb)])
        if msg.plain in ["找毛图 "+msg.plain.split(" ")[1]]:
            json_raw = getFursuitByID(msg.plain.split(" ")[1])
            furid = json_raw['data']['id']
            name=json_raw['data']['name']
            thumb=json_raw['data']['url']
            bot.send_group_msg(group=msg.group, msg=[miraicle.Plain('--- 每日吸毛 Bot ---\n今天你吸毛了嘛？\nFurID:'+str(furid)+'\n毛毛名字：'+name+'\n搜索方法：精确\n'),miraicle.Image(url=thumb)])
        if msg.plain in [msg.plain.split(" ")[0]+" 期每日鉴毛"]:
            json_raw = DailyFursuitByID(msg.plain.split(" ")[0])
            furid = json_raw['data']['id']
            name=json_raw['data']['name']
            thumb=json_raw['data']['url']
            bot.send_group_msg(group=msg.group, msg=[miraicle.Image(url=thumb)])
        if msg.plain in [msg.plain.split(" ")[0]+" 的每日鉴毛"]:
            json_raw = DailyFursuitByName(msg.plain.split(" ")[0])
            furid = json_raw['data']['id']
            name=json_raw['data']['name']
            thumb=json_raw['data']['url']
            bot.send_group_msg(group=msg.group, msg=[miraicle.Image(url=thumb)])
        if msg.plain in ["查云黑 "+msg.plain.split(" ")[1]]:
                # r =  requests.get("http://192.168.1.12:9000/getFursuitByName/"+str(re.fullmatch('(?<=来只 ).*$', msg.plain)[0]))
                # json_str = json.loads(r.text)
            qq=msg.plain.split(" ")[1]
            try:
                level=blacklistsutil.blacklist(qq)[0]
                time=blacklistsutil.blacklist(qq)[1]
                reason=blacklistsutil.blacklist(qq)[2]
                bot.send_group_msg(group=msg.group, msg=[miraicle.Plain('查询QQ：'+qq+"\n等级："+str(level)+"\n上黑时间："+time+"\n上黑原因："+reason)])
            except IndexError as outoflisterror:
                notfound=blacklistsutil.blacklist(qq)[0]
                bot.send_group_msg(group=msg.group, msg=[miraicle.Plain('查询QQ：'+qq+"\n"+notfound)])
        if msg.plain.startswith(".upload "):
            if permutil(msg.sender,2) == True:
                if msg.first_image != None:
                    bot.send_group_msg(group=msg.group, msg=[miraicle.Plain("上传完毕: \n"+str(msg.images[0])[51:len(str(msg.images[0]))-1])])
            else:
                    bot.send_group_msg(group=msg.group, msg=[miraicle.Plain('权限不足，执行该命令需要权限≥2')])
    except IndexError as e:
        if msg.plain in ['来只毛','.transfur']:
            json_raw=getFursuitRand()
            furid = json_raw['data']['id']
            name=json_raw['data']['name']
            thumb=json_raw['data']['url']
            bot.send_group_msg(group=msg.group, msg=[miraicle.Plain('--- 每日吸毛 Bot ---\n今天你吸毛了嘛？\nFurID:'+str(furid)+'\n毛毛名字：'+name+'\n搜索方法：全局随机\n'),miraicle.Image(url=thumb)])
        if msg.plain in ['签到','.签到','/签到','~签到']:
            raw=signutil.signup(msg.sender)
            if raw[0] == 'Already signed':
                bot.send_group_msg(group=msg.group, msg=[miraicle.Plain('您已经签到过了')])
            else:
                coin=raw[0]
                signtimes=raw[1]
                last_sign=raw[2]
                bot.send_group_msg(group=msg.group, msg=[miraicle.Plain('--- 签到成功 ---\n爪币数:'+str(coin)+'\n签到次数:'+str(signtimes)+"\n签到时间:"+last_sign)])
        if msg.plain in ["随机每日鉴毛","每日鉴毛"]:
            json_raw = DailyFursuitRand()
            furid = json_raw['data']['id']
            name=json_raw['data']['name']
            thumb=json_raw['data']['url']
            bot.send_group_msg(group=msg.group, msg=[miraicle.Image(url=thumb)])
    
        if msg.plain in [".lists"]:
            if permutil(msg.sender,5) == True:
                    groups={}
                    rawdata=bot.group_list()
                    for i in range(0,10001,1):
                        try:
                            groups[rawdata['data'][i]['id']]=[rawdata['data'][i]['name'],rawdata['data'][i]['permission']]
                        except:
                            break
                    string=""
                    for x in groups.keys():
                       string += "\n"+groups[x][0]+" "+groups[x][1]
                    bot.send_group_msg(group=msg.group, msg=[miraicle.Plain('已加入的群聊:\n'+string)])
            else:
                bot.send_group_msg(group=msg.group, msg=[miraicle.Plain('权限不足，执行该命令需要权限＝5')])
    except KeyError as er:
        helper = ConfigParser()
        helper.read('./config/main.conf', encoding='UTF-8')
        bot.send_group_msg(group=msg.group, msg=[miraicle.Plain(helper['mirai']['furry_not_found'])])

@miraicle.Mirai.receiver('FriendMessage')
def hello_to_friend(bot: miraicle.Mirai, msg: miraicle.FriendMessage):
    if msg.plain in ['help', '.help','/help','~help','帮助','.帮助','/帮助','~帮助']:
        helper = ConfigParser()
        helper.read('./config/main.conf', encoding='UTF-8')
        bot.send_friend_msg(qq=msg.sender, msg=helper['mirai']['help'])
@miraicle.Mirai.filter('BlacklistFilter')
def blacklist(bot: miraicle.Mirai, msg: miraicle.GroupMessage, flt: miraicle.BlacklistFilter):
    try:
        if msg.plain in ["拉黑 "+msg.plain.split(" ")[1]]:
            if permutil(msg.sender,4) == True:
                    qq=msg.plain.split(" ")[1]
                    flt.append(qq)
                    bot.send_group_msg(group=msg.group, msg=[miraicle.Plain('添加成功。')])
            else:
                bot.send_group_msg(group=msg.group, msg=[miraicle.Plain('权限不足，执行该命令需要权限≥4')])
        if msg.plain in ["解除拉黑 "+msg.plain.split(" ")[1]]:
            if permutil(msg.sender,4) == True:
                    qq=msg.plain.split(" ")[1]
                    flt.remove(qq)
                    bot.send_group_msg(group=msg.group, msg=[miraicle.Plain('移除成功。')])
            else:
                bot.send_group_msg(group=msg.group, msg=[miraicle.Plain('权限不足，执行该命令需要权限≥4')])
    except IndexError as ie:
        pass


miraiconf = ConfigParser()
miraiconf.read('./config/main.conf', encoding='UTF-8')
qq = miraiconf['mirai']['qq']       # 你登录的机器人 QQ 号
verify_key = miraiconf['mirai']['verifykey']     # 你在 setting.yml 中设置的 verifyKey
port = miraiconf['mirai']['port']                 # 你在 setting.yml 中设置的 port (http)
admin = miraiconf['mirai']['port'] 
bot = miraicle.Mirai(qq=qq, verify_key=verify_key, port=port)
bot.set_filter(miraicle.BlacklistFilter('./config/blacklist.json'))
transfur.run_app()
bot.run()
