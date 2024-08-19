# config.py
import os
from dotenv import load_dotenv

# 加载 .env 文件中的环境变量
load_dotenv()

# 从环境变量中获取 Notion API 令牌
NOTION_TOKEN = os.getenv("NOTION_TOKEN")  # 如果需要，可以加载 DATABASE_ID

# 构建请求头
HEADERS = {
    "Authorization": f"Bearer {NOTION_TOKEN}",
    "Content-Type": "application/json",
    "Notion-Version": "2022-06-28",
}
