#-*-coding:utf-8-*-
import requests
import json
class apis:
    """
        The definition of MCSM apis.
    """
    def __init__(self,url:str,key:str ):
        # key='7310b8070617431eb9ba191a70bce730'
        # url='http://192.168.1.12:23333/api/'
        global keys
        global urls
        keys = key
        urls = url
    def overview(self):
        url = urls+'overview?apikey='+keys
        bodys = requests.get(url)
        result = json.loads(bodys.text)
        version = result['data']['version']
        memory = result['data']['process']['memory']
        cwd = result['data']['process']['cwd']
        logined_record = result['data']['record']['logined']
        Illegal_access = result['data']['record']['illegalAccess']
        Login_failed = result['data']['record']['loginFailed']
        System_time = result['data']['system']['time']
        totalmem = result['data']['system']['totalmem']
        freemem = result['data']['system']['freemem']
        system_type = result['data']['system']['type']
        system_version = result['data']['system']['version']
        node_ver = result['data']['system']['node']
        hostname =  result['data']['system']['hostname']
        load_avg0 =  result['data']['system']['loadavg'][0]
        load_avg1 =  result['data']['system']['loadavg'][1]
        load_avg2 =  result['data']['system']['loadavg'][2]
        system_platform = result['data']['system']['platform']
        release = result['data']['system']['release']
        uptime = result['data']['system']['uptime']
        sys_cpu = result['data']['system']['cpu']
        remote_count = result['data']['remoteCount']['available']
        total_count = result['data']['remoteCount']['total']
        return [version,memory,cwd,logined_record,Illegal_access,Login_failed,
         System_time,totalmem,freemem,system_type,system_version,node_ver,hostname,
         [load_avg0,load_avg1,load_avg2],system_platform,release,uptime,sys_cpu,
         remote_count,total_count]
    def sittings(self):
        url = urls+'overview/setting/?apikey='+keys
        bodys = requests.get(url)
        result = json.loads(bodys.text)
        http_port = result['data']['httpPort']
        http_ip = result['data']['httpIp']
        data_port = result['data']['dataPort']
        forward_type = result['data']['forwardType']
        cross_domain = result['data']['crossDomain']
        gzip = result['data']['gzip']
        max_compress = result['data']['maxCompress']
        max_donwload = result['data']['maxDonwload']
        zip_type = result['data']['zipType']
        login_check_ip = result['data']['loginCheckIp']
        return [http_port,http_ip,data_port,forward_type,cross_domain,gzip,
        max_compress,max_donwload,zip_type,login_check_ip]
        