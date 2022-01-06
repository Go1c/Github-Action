# -*- coding: utf-8 -*-
import requests


def push_report(web_hook):
    header = {
        "Content-Type": "application/json;charset=UTF-8"
    }
    message_body = {
        "msg_type": "post",
        "content": {
            "post": {
                "zh_cn": {
                    "title": "订餐啦",
                    "content": [
                        [
                            {
                                "tag": "at",
                                "user_id": "all",
                                "user_name": "所有人"
                            },
                            {
                                "tag": "text",
                                "text": "<color=\"red\">今天有周会，对着自己的okr来一发?</color>"
                            },
                            {
                                "tag": "a",
                                "text": "点我订餐",
                                "href": "https://applink.feishu.cn/T89MJUmq"
                            },
                        ]
                    ]
                }
            }
        }
    }
    message_body_card = {
        "msg_type": "interactive",
        "card": {
            "config": {
                # "wide_screen_mode": true,
                # "enable_forward": true
            },
            "elements": [{
                "tag": "div",
                "text": {
                    "content": "**可以辜负世界  但是不可以辜负自己的肚子**",
                    "tag": "lark_md"
                }
            }, {
                "actions": [{
                    "tag": "button",
                    "text": {
                        "content": "点我订餐 :玫瑰:",
                        "tag": "lark_md"
                    },
                    "url": "https://applink.feishu.cn/T89MJUmq",
                    "type": "default",
                    "value": {}
                }],
                "tag": "action"
            }],
            "header": {
                "title": {
                    "content": "订餐啦！！ 订餐啦！！！",
                    "tag": "plain_text"
                }
            }
        }
    }
    ChatRob = requests.post(url=web_hook, json=message_body_card, headers=header)
    opener = ChatRob.json()

    if opener["StatusMessage"] == "success":
        print(u"%s 通知消息发送成功！" % opener)
    else:
        print(u"通知消息发送失败，原因：{}".format(opener))


if __name__ == '__main__':
    # webhook 来自于 获取机器人webhook：复制webhook 中的那个值
    webhook = "https://open.feishu.cn/open-apis/bot/v2/hook/db077847-cefa-4035-b152-0dbe62b22b92"
    push_report(webhook)
