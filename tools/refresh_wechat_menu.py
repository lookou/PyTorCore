#!/usr/bin/env python3
#-*- coding: utf-8 -*-

import tornado.ioloop
from tornado.httpclient import AsyncHTTPClient, HTTPRequest
import json
from insts.llog import llogger
#from .. import conf
import conf
import cachetools


# 创建一个LRU缓存，最大容量为3
cache = cachetools.Cache(maxsize=3)
logger = llogger()

async def get(url):
    http_client = AsyncHTTPClient()
    try:
        response = await http_client.fetch(url)
        data = json.loads(response.body) 
        return data
    except tornado.httpclient.HTTPError as e:
        print('Error:', e)
    except Exception as e:
        print('Error:', e)
    finally:
        http_client.close()

async def post(url, headers, data):
    http_client = AsyncHTTPClient()
    #利用 Python 的 json 内置模块，在进行 dumps 操作时，使用 ensure_ascii=False 参数是中文不会被转码
    #body=json.dumps(data, ensure_ascii=False).encode('utf-8')
    #print(body)
    try:
        request = HTTPRequest(
            url,
            method="POST",
            headers=headers,
            body=json.dumps(data,ensure_ascii=False).encode('utf-8')
        )
        response = await http_client.fetch(request)
        data = json.loads(response.body) 
        return data
    except tornado.httpclient.HTTPError as e:
        print('Error:', e)
    except Exception as e:
        print('Error:', e)
    finally:
        http_client.close()



async def fetch_key():
    url = 'https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid=' + conf.wechat_appid + '&secret=' + conf.wechat_appsecret # 替换为你的API URL
    data = await get(url)
    print(data)
    if 'errcode' in data:
        logger.error(data)

    if 'access_token' in data:
        logger.info("token", data['access_token'], "expires_in", str(data['expires_in']))
        cache['access_token'] = data['access_token']
        print(cache.get("access_token"))
    else:
        logger.info('No key found in the response')



async def fetch_menu():
    value = cache.get('access_token')
    print(value)
    url = 'https://api.weixin.qq.com/cgi-bin/menu/get?access_token=' + cache.get('access_token')
    data = await get(url)
    if 'errcode' in data:
        logger.error(data)
    else:
        print(data)


async def refresh_menu(data):
    url = 'https://api.weixin.qq.com/cgi-bin/menu/create?access_token=' + cache.get('access_token')  # 替换为你的API URL
    headers = {'Content-Type': 'application/json'}
    data = await post(url, headers, data)
    if 'errcode' in data:
        if data['errcode'] == 0:
            logger.info("Refresh Success!")
        else:
            logger.error(data)

    else:
        logger.warning('No key found in the response')

async def process():
    await fetch_key()
    await fetch_menu()
    data = {"button":[{"type":"view", "name":"AI助手", "url":"https://cloud.ifootoo.com/resource/html/h5/#/pages/componentsAI/chat/chat?appcode=b1d7571e4299a1de&chat=1"}]}
    #data = {"button":[{"type":"view", "name":"AI助手", "url":"https://cloud.ifootoo.com/resource/html/h5/?appcode=0c42ffc718c85ac2"}], },"https://cloud.ifootoo.com/resource/html/h5/#/pages/componentsAI/chat/chat?appcode=b1d7571e4299a1de"}]}
    await refresh_menu(data)


if __name__ == '__main__':
    tornado.ioloop.IOLoop.current().run_sync(lambda: process())
