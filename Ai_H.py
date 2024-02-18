from websocket import WebSocketApp
import json
import re
import gzip
from urllib.parse import unquote_plus
import requests
from douyin_pb2 import PushFrame, Response, ChatMessage, GiftMessage
import time
import pyautogui
import threading





# 定义一个函数，用于从直播房间的URL中提取信息
def fetch_live_room_info(url):
    # 发送GET请求获取直播房间信息
    res = requests.get(
        url=url,
        headers={
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36",
        },
        cookies={
            "__ac_nonce": "063abcffa00ed8507d599"  # 可以是任意值
        }
    )
    # print(res.text)
    # 从响应文本中提取包含直播房间信息的数据字符串
    # data_string = re.findall(r'<script id="RENDER_DATA" type="application/json">(.*?)</script>', res.text)[0]

    # print(data_string)
    # data_dict = json.loads(unquote_plus(data_string))

    # 提取房间ID、房间标题和在线用户数等信息
    # room_id = data_dict['app']['initialState']['roomStore']['roomInfo']['roomId']
    # room_title = data_dict['app']['initialState']['roomStore']['roomInfo']["room"]['title']
    # room_user_count = data_dict['app']['initialState']['roomStore']['roomInfo']["room"]['user_count_str']
    room_id = '7288850849772686136'
    room_title = '1'
    room_user_count = '1'

    # 构建WebSocket URL，包含房间ID等信息
    # wss_url = f"wss://webcast5-ws-web-hl.douyin.com/webcast/im/push/v2/?app_name=douyin_web&version_code=180800&webcast_sdk_version=1.0.10&update_version_code=1.0.10&compress=gzip&device_platform=web&cookie_enabled=true&screen_width=1536&screen_height=864&browser_language=zh-CN&browser_platform=Win32&browser_name=Mozilla&browser_version=5.0%20(Windows%20NT%2010.0;%20Win64;%20x64)%20AppleWebKit/537.36%20(KHTML,%20like%20Gecko)%20Chrome/118.0.0.0%20Safari/537.36%20Edg/118.0.2088.76&browser_online=true&tz_name=Asia/Shanghai&cursor=t-1698911609366_r-1_d-1_u-1_h-1&internal_ext=internal_src:dim|wss_push_room_id:7296272456657029939|wss_push_did:7218100493292946956|dim_log_id:202311021553292BDA87F7438D9D0C4E3C|first_req_ms:1698911609290|fetch_time:1698911609366|seq:1|wss_info:0-1698911609366-0-0|wrds_kvs:WebcastInRoomBannerMessage-GrowthCommonBannerSubSyncKey-1698849768336386911_InputPanelComponentSyncData-1698854359832533744_WebcastRoomRankMessage-1698853902414179955_WebcastRoomStatsMessage-1698854358335445615_WebcastRoomStreamAdaptationMessage-1698854358785053535&host=https://live.douyin.com&aid=6383&live_id=1&did_rule=3&endpoint=live_pc&support_wrds=1&user_unique_id=7218100493292946956&im_path=/webcast/im/fetch/&identity=audience&need_persist_msg_count=15&room_id=7296272456657029939&heartbeatDuration=0&signature=WsZQqOiiEPA/Gp1T"
    # wss_url = f"wss://webcast5-ws-web-lf.douyin.com/webcast/im/push/v2/?app_name=douyin_web&version_code=180800&webcast_sdk_version=1.0.12&update_version_code=1.0.12&compress=gzip&device_platform=web&cookie_enabled=true&screen_width=1536&screen_height=864&browser_language=zh-CN&browser_platform=Win32&browser_name=Mozilla&browser_version=5.0%20(Windows%20NT%2010.0;%20Win64;%20x64)%20AppleWebKit/537.36%20(KHTML,%20like%20Gecko)%20Chrome/120.0.0.0%20Safari/537.36%20Edg/120.0.0.0&browser_online=true&tz_name=Asia/Shanghai&cursor=r-1_d-1_u-1_fh-7314945514418770994_t-1703143490338&internal_ext=internal_src:dim|wss_push_room_id:7314706291295849231|wss_push_did:7218100493292946956|dim_log_id:20231221152450D9B02400D5DB372A953E|first_req_ms:1703143490271|fetch_time:1703143490338|seq:1|wss_info:0-1703143490338-0-0|wrds_kvs:HighlightContainerSyncData-1_WebcastRoomStatsMessage-1703143485827569923_WebcastRoomStreamAdaptationMessage-1703143482338920581_InputPanelComponentSyncData-1703115917084945878_WebcastRoomRankMessage-1703143401907702314&host=https://live.douyin.com&aid=6383&live_id=1&did_rule=3&endpoint=live_pc&support_wrds=1&user_unique_id=7218100493292946956&im_path=/webcast/im/fetch/&identity=audience&need_persist_msg_count=15&room_id=7314706291295849231&heartbeatDuration=0&signature=Rh3pWc/1mqhZq3ZY"
    wss_url = f"wss://webcast5-ws-web-hl.douyin.com/webcast/im/push/v2/?app_name=douyin_web&version_code=180800&webcast_sdk_version=1.0.12&update_version_code=1.0.12&compress=gzip&device_platform=web&cookie_enabled=true&screen_width=1536&screen_height=864&browser_language=zh-CN&browser_platform=Win32&browser_name=Mozilla&browser_version=5.0%20(Windows%20NT%2010.0;%20Win64;%20x64)%20AppleWebKit/537.36%20(KHTML,%20like%20Gecko)%20Chrome/120.0.0.0%20Safari/537.36%20Edg/120.0.0.0&browser_online=true&tz_name=Asia/Shanghai&cursor=t-1705886360022_r-1_d-1_u-1_h-1&internal_ext=internal_src:dim|wss_push_room_id:7326725277080423206|wss_push_did:7218100493292946956|first_req_ms:1705886359925|fetch_time:1705886360022|seq:1|wss_info:0-1705886360022-0-0|wrds_v:7326726118302550906|wrds_kvs:WebcastRoomStatsMessage-1705886351231079046_WebcastRoomStreamAdaptationMessage-1705886358455976925_InteractEffectSyncData-1705886213690481570_WebcastRoomRankMessage-1705886349763562427&host=https://live.douyin.com&aid=6383&live_id=1&did_rule=3&endpoint=live_pc&support_wrds=1&user_unique_id=7218100493292946956&im_path=/webcast/im/fetch/&identity=audience&need_persist_msg_count=15&room_id=7326725277080423206&heartbeatDuration=0&signature=RdrdyXj1IMlfI05u"
    wss_url = f"wss://webcast5-ws-web-lf.douyin.com/webcast/im/push/v2/?app_name=douyin_web&version_code=180800&webcast_sdk_version=1.0.12&update_version_code=1.0.12&compress=gzip&device_platform=web&cookie_enabled=true&screen_width=1536&screen_height=864&browser_language=zh-CN&browser_platform=Win32&browser_name=Mozilla&browser_version=5.0%20(Windows%20NT%2010.0;%20Win64;%20x64)%20AppleWebKit/537.36%20(KHTML,%20like%20Gecko)%20Chrome/121.0.0.0%20Safari/537.36%20Edg/121.0.0.0&browser_online=true&tz_name=Asia/Shanghai&cursor=t-1707235918131_r-1_d-1_u-1_h-1&internal_ext=internal_src:dim|wss_push_room_id:7332426088553335606|wss_push_did:7218100493292946956|first_req_ms:1707235918069|fetch_time:1707235918131|seq:1|wss_info:0-1707235918131-0-0|wrds_v:7332522430071573411&host=https://live.douyin.com&aid=6383&live_id=1&did_rule=3&endpoint=live_pc&support_wrds=1&user_unique_id=7218100493292946956&im_path=/webcast/im/fetch/&identity=audience&need_persist_msg_count=15&insert_task_id=&live_reason=&room_id=7332426088553335606&heartbeatDuration=0&signature=R4qshfEtMjCnaafH"
    # 获取ttwid
    ttwid = res.cookies.get_dict()['ttwid']

    # 返回提取的信息
    return room_id, room_title, room_user_count, wss_url, ttwid


# 定义WebSocket连接打开时的回调函数
def on_open(ws):
    print('on_open')


# 定义WebSocket接收到消息时的回调函数
def on_message(ws, content):
    frame = PushFrame()
    frame.ParseFromString(content)

    # 对PushFrame的 payload 内容进行gzip解压
    origin_bytes = gzip.decompress(frame.payload)

    # 根据Response+gzip解压数据，生成数据对象
    response = Response()
    response.ParseFromString(origin_bytes)

    if response.needAck:
        s = PushFrame()
        s.payloadType = "ack"
        s.payload = response.internalExt.encode('utf-8')
        s.logId = frame.logId

        ws.send(s.SerializeToString())

    # 获取数据内容（需根据不同method，使用不同的结构对象对 数据 进行解析）
    #   注意：此处只处理 WebcastChatMessage ，其他处理方式都是类似的。
    # for item in response.messagesList:
    #     if item.method != "WebcastChatMessage":
    #         continue
    #
    #     message = ChatMessage()
    #     message.ParseFromString(item.payload)
    #     info = f"【{message.user.nickName}】{message.content} "
    #     print(info)

    for item in response.messagesList:
        if item.method == "WebcastChatMessage":
            message = ChatMessage()
            message.ParseFromString(item.payload)
            info = f"【{message.user.nickName}】{message.content} "
            print(info)
        elif item.method == "WebcastGiftMessage":
            # print("礼物")
            gift = GiftMessage()
            gift.ParseFromString(item.payload)
            gift_info = f"【{gift.user.nickName}】--------------------礼物ID：{gift.giftId},个数：{gift.totalCount},{gift.groupCount}"
            print(gift_info)

            # 判断礼物并执行指令
            print(int(gift.giftId),int(gift.totalCount))
            if int(gift.giftId) == 685:
                for i in range(0, int(gift.totalCount)):
                    print("粉丝团")
                    # print("睡衣")
                    # pyautogui.press('9')

            elif gift.giftId == 463:
                for i in range(0, int(gift.totalCount)):
                    print("小心心")
                    # print("绿色制服")
                    # pyautogui.press('6')

            elif gift.giftId == 3992:
                for i in range(0, int(gift.totalCount)):
                    print("人气票")
                    # print("黄色制服")
                    # pyautogui.press('3')

            elif gift.giftId == 2001:
                for i in range(0, int(gift.totalCount)):
                    print("玫瑰")
                    # print("女仆装")
                    # pyautogui.press('8')

            elif gift.giftId == 2002:
                for i in range(0, int(gift.totalCount)):
                    print("啤酒")
                    # print("摇摆裙")
                    # pyautogui.press('4')

            elif gift.giftId == 2006:
                for i in range(0, int(gift.totalCount)):
                    print("鲜花")
                    # print("旗袍")
                    # pyautogui.press('0')

            elif gift.giftId == 165:
                for i in range(0, int(gift.totalCount)):
                    print("棒棒糖")
                    # print("紫色校服")
                    # pyautogui.press('7')

            elif gift.giftId == 436:
                for i in range(0, int(gift.totalCount)):
                    print("墨镜")
                    # print("紧身裤")
                    # pyautogui.press('5')
            else:
                print("未匹配任何条件")






# 定义WebSocket发生错误时的回调函数
def on_error(ws, content):
    print(content)
    print("on_error")
    run()

# 定义WebSocket连接关闭时的回调函数
def on_close(*args, **kwargs):
    print(args, kwargs)
    print("on_close")

# 主函数
def run():
    # thread = threading.Thread(target=gitf_random)
    # thread.start()

    web_url = "https://live.douyin.com/80017709309"

    # 获取直播房间信息
    room_id, room_title, room_user_count, wss_url, ttwid = fetch_live_room_info(web_url)
    print(room_id, room_title, room_user_count, wss_url, ttwid)

    # 创建WebSocket连接，并设置回调函数
    ws = WebSocketApp(
        url=wss_url,
        header={
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"
        },
        cookie=f"ttwid={ttwid}",
        on_open=on_open,
        on_message=on_message,
        on_error=on_error,
        on_close=on_close,
    )
    ws.run_forever()


if __name__ == '__main__':
    run()

