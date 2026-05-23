#!/usr/bin/env python3
"""
ESG招标信息抓取脚本
用法: python3 ./scripts/esg_scraper.py
输出: 保存到 ~/wiki/raw/articles/ 目录下
"""

import json
import os
import re
import sys
from datetime import datetime
from urllib.request import Request, urlopen
from urllib.parse import quote

WIKI_DIR = os.path.expanduser("~/wiki")
RAW_DIR = os.path.join(WIKI_DIR, "raw", "articles")
TODAY = datetime.now().strftime("%Y-%m-%d")

def fetch_bidcenter_esg():
    """从采招网抓取ESG招标信息"""
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
    }
    
    # 采招网搜索页（通过浏览器打开获取的URL模式）
    url = f"https://search.bidcenter.com.cn/search?keywords={quote('ESG')}&mod=0"
    
    req = Request(url, headers=headers)
    try:
        resp = urlopen(req, timeout=15)
        html = resp.read().decode('utf-8', errors='replace')
        return html
    except Exception as e:
        return f"ERROR: {e}"

def parse_results(html):
    """简单解析结果（主要用于错误检测，实际通过browser tool获取）"""
    if html.startswith("ERROR"):
        return []
    
    # 提取搜索结果数量
    count_match = re.search(r'为您查询到.*?(\d+).*?条', html)
    total = count_match.group(1) if count_match else "未知"
    
    return [{"total": total, "note": "详细数据需通过Hermes browser获取"}]

def save_to_wiki(items, source="bidcenter"):
    """保存抓取结果到wiki"""
    os.makedirs(RAW_DIR, exist_ok=True)
    
    filename = f"esg-bidding-{source}-{TODAY}.md"
    filepath = os.path.join(RAW_DIR, filename)
    
    # 计算sha256
    content_text = json.dumps(items, ensure_ascii=False, indent=2)
    
    md = f"""---
source_url: https://search.bidcenter.com.cn/search?keywords=ESG&mod=0
ingested: {TODAY}
source: {source}
---

# ESG招标信息日报 - {TODAY}

## 来源: 采招网 bidcenter.com.cn

### 结果摘要

"""
    if items:
        md += f"- 共查询到相关结果\n\n"
        for item in items:
            md += f"- {item}\n"
    else:
        md += "- 本次未获取到数据\n"
    
    md += f"\n---\n*由Hermes自动抓取于 {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}*\n"
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(md)
    
    return filepath

def main():
    print(f"=== ESG招标信息抓取 - {TODAY} ===")
    
    # 尝试直接抓取
    html = fetch_bidcenter_esg()
    results = parse_results(html)
    
    if results:
        print(f"直接抓取结果: {results}")
    else:
        print("直接抓取失败或数据不完整（采招网需要浏览器渲染）")
        print("请通过Hermes browser工具获取详细数据")
    
    # 保存占位文件
    filepath = save_to_wiki(results)
    print(f"文件已保存: {filepath}")

if __name__ == "__main__":
    main()
