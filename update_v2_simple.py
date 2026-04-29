#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
批量更新所有HTML页面 - 版本2
完成6项修改
"""

import os
import re
from pathlib import Path

# 工作目录
WORK_DIR = r"c:\Users\yqyzj_skzq6hr\WorkBuddy\20260425142831"

# 新的电话号码
NEW_PHONE = "15774116703"
NEW_PHONE_DISPLAY = "157-7411-6703"

# 新的版权信息
NEW_COPYRIGHT = "© 2018-2026 湖南筑邦企业管理咨询有限公司 永州分公司  美逸广告"

def update_file(file_path):
    """更新单个文件"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        modified = False

        # 1. 去掉邮箱
        if 'mailto:' in content or 'hunanzhubang' in content or '📧' in content:
            # 删除邮件链接
            content = re.sub(r'<a[^>]*mailto:[^>]*>[^<]*</a>', '', content)
            content = re.sub(r'📧\s*[^\s<]+@[^\s<]+', '', content)
            content = re.sub(r'hunanzhubang@163\.com', '', content)
            modified = True

        # 2. 电话号码统一
        old_phones = ['157-7491-8981', '15774918981']
        for old in old_phones:
            if old in content:
                content = content.replace(old, NEW_PHONE_DISPLAY if '-' in old else NEW_PHONE)
                modified = True

        # 更新 tel: 链接
        if 'tel:15774918981' in content:
            content = content.replace('tel:15774918981', f'tel:{NEW_PHONE}')
            modified = True

        # 3. 更新浮动widget (稍后统一处理)

        # 4. 修改版权信息
        if '版权所有' in content:
            content = re.sub(
                r'©\s*\d{4}\s*湖南筑邦企业管理咨询有限公司\s*版权所有',
                NEW_COPYRIGHT,
                content
            )
            content = re.sub(
                r'©\s*\d{4}-\d{4}\s*湖南筑邦企业管理咨询有限公司\s*版权所有',
                NEW_COPYRIGHT,
                content
            )
            modified = True

        # 5. 统一导航栏 (子页面)
        file_name = os.path.basename(file_path)
        if file_name != 'index.html':
            # 替换 nav 为 main-nav
            if 'class="nav"' in content:
                content = content.replace('class="nav"', 'class="main-nav"')
                modified = True

            # 确保链接格式正确
            nav_patterns = [
                (r'href="#about"', 'href="index.html#about"'),
                (r'href="#services"', 'href="index.html#services"'),
                (r'href="#branches"', 'href="index.html#branches"'),
                (r'href="#contact"', 'href="index.html#contact"'),
            ]
            for old, new in nav_patterns:
                if re.search(old, content) and 'index.html' not in re.search(old, content).group(0):
                    content = re.sub(old, new, content)
                    modified = True

        # 保存修改
        if modified:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            return True

        return False

    except Exception as e:
        print(f"错误: {file_path} - {e}")
        return False

def main():
    html_files = list(Path(WORK_DIR).glob("*.html"))
    print(f"找到 {len(html_files)} 个HTML文件")

    updated = 0
    for f in html_files:
        if update_file(str(f)):
            updated += 1
            print(f"✓ {f.name}")

    print(f"\n完成！更新了 {updated} 个文件")

if __name__ == "__main__":
    main()
