import json
from datetime import datetime

import requests

from endpoint import WEBHOOK, URL_NETLIFY


def notif_slack():
    json_content = open("report_all.json", "r").read()
    data_json = json.loads(json_content)
    time = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

    try:
        test_passed = data_json.get("summary")["passed"]
    except:
        test_passed = "0"
    try:
        test_failed = data_json.get("summary")["failed"]
    except:
        test_failed = "0"
    try:
        test_total = data_json.get("summary")["total"] = data_json.get("summary")["passed"]
    except:
        test_total = "0"

    if float(test_failed) > 0:
        color = "#FF0000"
    else:
        color = "#008000"

    test_success_rate = (test_passed / test_total) * 100

    payload = {
        "attachments": [
            {
                "color": color,
                "blocks": [
                    {
                        "type": "header",
                        "text": {
                            "type": "plain_text",
                            "text": "API AUTOMATION",
                            "emoji": True
                        }
                    },
                    {
                        "type": "divider"
                    },
                    {
                        "type": "section",
                        "fields": [
                            {
                                "type": "mrkdwn",
                                "text": f"*Success Test:*\n {test_passed}"
                            },
                            {
                                "type": "mrkdwn",
                                "text": f"*Failed Test:*\n {test_failed}"
                            }
                        ]
                    },
                    {
                        "type": "section",
                        "fields": [
                            {
                                "type": "mrkdwn",
                                "text": "*Skipped Test:*\n0"
                            },
                            {
                                "type": "mrkdwn",
                                "text": f"*Total Test:*\n {test_total}"
                            }
                        ]
                    },
                    {
                        "type": "section",
                        "fields": [
                            {
                                "type": "mrkdwn",
                                "text": f"*Success Rate:*\n {test_success_rate}%"
                            }
                        ]
                    },
                    {
                        "type": "section",
                        "text": {
                            "type": "mrkdwn",
                            "text": f"<{URL_NETLIFY}|Link Report Test>"
                        }
                    },
                    {
                        "type": "divider"
                    },
                    {
                        "type": "rich_text",
                        "elements": [
                            {
                                "type": "rich_text_section",
                                "elements": [
                                    {
                                        "type": "text",
                                        "text": "tested by : HANS SEPTIANTO",
                                        "style": {
                                            "italic": True
                                        }
                                    }
                                ]
                            }
                        ]
                    },
                    {
                        "type": "rich_text",
                        "elements": [
                            {
                                "type": "rich_text_section",
                                "elements": [
                                    {
                                        "type": "text",
                                        "text": f"created at : {time}",
                                        "style": {
                                            "italic": True
                                        }
                                    }
                                ]
                            }
                        ]
                    }
                ]
            }
        ]
    }

    req = requests.post(WEBHOOK, json=payload)


notif_slack()
