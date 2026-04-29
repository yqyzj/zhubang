#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os

WORK_DIR = r"c:\Users\yqyzj_skzq6hr\WorkBuddy\20260425142831"
NEW_COPYRIGHT = "© 2018-2026 湖南筑邦企业管理咨询有限公司 永州分公司  美逸广告"

count = 0
for filename in os.listdir(WORK_DIR):
    if filename.endswith('.html') and filename != 'index.html':
        filepath = os.path.join(WORK_DIR, filename)
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
            
            modified = False
            
            # 1. 替换 nav 为 main-nav (CSS)
            if 'class="nav"' in content:
                content = content.replace('class="nav"', 'class="main-nav"')
                modified = True
            
            # 2. 替换 nav 为 main-nav (HTML)
            if '<ul class="nav">' in content:
                content = content.replace('<ul class="nav">', '<ul class="main-nav">')
                modified = True
            
            # 3. 更新版权信息
            if '版权所有' in content and '2018-2026' not in content:
                import re
                content = re.sub(r'©\s*\d{4}\s*湖南筑邦[^<]*', NEW_COPYRIGHT, content)
                modified = True
            
            if modified:
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(content)
                count += 1
                print(f"Updated: {filename}")
        
        except Exception as e:
            print(f"Error {filename}: {e}")

print(f"\nTotal updated: {count} files")
print("Done!")
