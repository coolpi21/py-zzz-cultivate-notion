import requests
import json
from config import HEADERS


# 之前创建的页面的 page_id 列表
pages_to_update = [
    {
        "page_id": "52ee1e7896e342e0906d898899821d62",  # 第一个页面的 ID
        "level": 50,
        "weapon_level": 50,
        "life": 2,
        "character_property": "冰",
        "character_positioning": "击破",
        "camp": "维多利亚家政",
    },
    # 可以继续添加更多页面的更新信息
]

# 遍历页面更新列表，依次更新页面
for page in pages_to_update:
    update_page_data = {
        "properties": {
            # "人物等级": {"number": page["level"]},
            # "音擎等级": {"number": page["weapon_level"]},
            # "影画": {"number": page["life"]},
            "属性": {"select": {"name": page["character_property"]}},
            "特性": {"select": {"name": page["character_positioning"]}},
            "阵营": {"select": {"name": page["camp"]}},
        },
    }

    # 发送请求更新页面
    response = requests.patch(
        f"https://api.notion.com/v1/pages/{page['page_id']}",
        headers=HEADERS,
        data=json.dumps(update_page_data),
    )

    # 检查请求是否成功
    if response.status_code == 200:
        print(f"页面 '{page['page_id']}' 更新成功！")
    else:
        print(f"页面 '{page['page_id']}' 更新失败:", response.status_code)
        print("错误信息:", response.json())
