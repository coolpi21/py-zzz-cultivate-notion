from config import HEADERS
import requests
import json

with open("pages_data.json", "r", encoding="utf-8") as file:
    data = json.load(file)

# Notion API 令牌和数据库 ID
DATABASE_ID = "562f015efd3648df892fa92624436f4c"

# 要创建的页面数据列表，每个字典代表一个页面
pages_to_create = data["agent"]

# 遍历页面数据列表，依次创建页面
for page in pages_to_create:
    new_page_data = {
        "parent": {"database_id": DATABASE_ID},  # 指定父数据库
        "properties": {
            "代理人": {  # 假设数据库中有一个标题属性叫 "Name"
                "title": [{"text": {"content": page["title"]}}],  # 设置页面标题
            },
            "人物等级": {"number": page["level"]},
            "音擎等级": {"number": page["weapon_level"]},
            "影画": {"number": page["constellation"]},
            "属性": {"select": {"name": page["character_property"]}},
            "特性": {"select": {"name": page["character_positioning"]}},
            "阵营": {"select": {"name": page["camp"]}},
            "稀有度": {"select": {"name": page["rarity"]}},
        },
        "icon": page["icon"],
    }

    # 发送请求创建新页面
    response = requests.post(
        "https://api.notion.com/v1/pages",
        headers=HEADERS,
        data=json.dumps(new_page_data),
    )

    # 检查请求是否成功
    if response.status_code == 200:
        print(f"页面 '{page['title']}' 创建成功！")
    else:
        print(f"页面 '{page['title']}' 创建失败:", response.status_code)
        print("错误信息:", response.json())
