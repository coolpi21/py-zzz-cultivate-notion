import random
import requests
from config import NOTION_TOKEN


def add_select_option(token, database_id, property_name, options):
    url = f"https://api.notion.com/v1/databases/{database_id}"
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json",
        "Notion-Version": "2022-06-28",  # 确保使用最新的 API 版本
    }
    data = {"properties": {property_name: {"select": {"options": options}}}}

    response = requests.patch(url, headers=headers, json=data)
    return response.json()


# 使用示例
database_id = "902697d4b8624e52948b757049e6048f"  # 移除 URL 参数
property_name = "副本等级"  # 确保这个属性已经是选择类型
# 预定义的颜色列表
colors = [
    "blue",
    "brown",
    "default",
    "gray",
    "green",
    "orange",
    "pink",
    "purple",
    "red",
    "yellow",
]

# 随机分配颜色
options = [{"name": str(i), "color": random.choice(colors)} for i in range(10, 51, 10)]

print(options)

result = add_select_option(NOTION_TOKEN, database_id, property_name, options)
print(result)
