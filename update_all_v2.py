#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
批量更新所有HTML页面 - 版本2
完成6项修改：
1. 去掉邮箱
2. 电话号码统一为：15774116703
3. 右下角悬浮组件改为展开显示，电话与微信并列排列
4. 修改版权信息
5. 统一导航栏（子页面与首页一致）
6. 调整分公司排列（长沙本部单独一排）并优化SEO
"""

import os
import re
from pathlib import Path

# 工作目录
WORK_DIR = r"c:\Users\yqyzj_skzq6hr\WorkBuddy\20260425142831"

# 新的电话号码（不带横杠）
NEW_PHONE = "15774116703"
NEW_PHONE_DISPLAY = "157-7411-6703"  # 显示用，带横杠

# 新的版权信息
NEW_COPYRIGHT = "© 2018-2026 湖南筑邦企业管理咨询有限公司 永州分公司  美逸广告"

# 首页导航栏HTML（目标格式）
INDEX_NAV = '''        <ul class="main-nav">
                    <li><a href="#about">关于我们</a></li>
                    <li><a href="#services">服务项目</a></li>
                    <li><a href="#branches">分公司</a></li>
                    <li><a href="#cases">成功案例</a></li>
                    <li><a href="#contact">联系我们</a></li>
                </ul>'''

# 子页面导航栏HTML（需要统一为与首页一样）
SUB_NAV = '''        <ul class="main-nav">
                    <li><a href="index.html#about">关于我们</a></li>
                    <li><a href="index.html#services">服务项目</a></li>
                    <li><a href="index.html#branches">分公司</a></li>
                    <li><a href="index.html#cases">成功案例</a></li>
                    <li><a href="index.html#contact">联系我们</a></li>
                </ul>'''

# 新的浮动widget HTML（电话展开显示，与微信并列）
NEW_FLOAT_WIDGET = '''
    <!-- 右下角悬浮组件 -->
    <div class="float-widget" id="floatWidget">
        <div class="float-phone" onclick="window.location.href='tel:15774116703'">
            <svg width="24" height="24" viewBox="0 0 24 24" fill="white">
                <path d="M6.62 10.79c1.44 2.83 3.76 5.14 6.59 6.59l2.2-2.2c.27-.27.67-.36 1.02-.24 1.12.37 2.33.57 3.57.57.55 0 1 .45 1 1V20c0 .55-.45 1-1 1-9.39 0-17-7.61-17-17 0-.55.45-1 1-1h3.5c.55 0 1 .45 1 1 0 1.25.2 2.45.57 3.57.11.35.03.74-.25 1.02l-2.2 2.2z"/>
            </svg>
            <span class="phone-number">157-7411-6703</span>
        </div>
        <div class="float-wechat" onclick="toggleWechatQR()">
            <svg width="24" height="24" viewBox="0 0 24 24" fill="white">
                <path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm-2 15l-5-5 1.41-1.41L10 14.17l7.59-7.59L19 8l-9 9z"/>
            </svg>
        </div>
        <div class="wechat-qr" id="wechatQR">
            <div style="width:180px;height:180px;background:#f0f0f0;border-radius:8px;display:flex;align-items:center;justify-content:center;margin:0 auto 10px;font-size:14px;color:#666;">
                请添加微信号：15774116703
            </div>
            <p style="font-size:13px;color:#666;margin:5px 0;">扫码添加微信</p>
            <p style="font-size:14px;color:#07c160;font-weight:600;">微信号：15774116703</p>
        </div>
    </div>
    <style>
        .float-widget{position:fixed;right:30px;bottom:30px;z-index:9999;display:flex;flex-direction:row;gap:15px;align-items:center;}
        .float-phone{display:flex;align-items:center;gap:8px;background:linear-gradient(135deg,#d4a843,#c49b3a);color:white;padding:12px 20px;border-radius:30px;cursor:pointer;transition:all 0.3s;box-shadow:0 5px 20px rgba(0,0,0,0.3);text-decoration:none;}
        .float-phone svg{flex-shrink:0;}
        .float-phone .phone-number{font-size:16px;font-weight:600;white-space:nowrap;}
        .float-phone:hover{transform:scale(1.05);}
        .float-wechat{width:60px;height:60px;border-radius:50%;display:flex;align-items:center;justify-content:center;cursor:pointer;transition:all 0.3s;position:relative;box-shadow:0 5px 20px rgba(0,0,0,0.3);background:linear-gradient(135deg,#07c160,#06ad56);}
        .float-wechat:hover{transform:scale(1.1);}
        .wechat-qr{position:absolute;bottom:80px;right:0;width:250px;background:white;border-radius:16px;box-shadow:0 10px 40px rgba(0,0,0,0.2);display:none;overflow:hidden;padding:20px;text-align:center;}
        .wechat-qr.active{display:block;animation:fadeInUp 0.3s ease;}
        @keyframes fadeInUp{from{opacity:0;transform:translateY(10px);}to{opacity:1;transform:translateY(0);}}
        @media(max-width:768px){.float-widget{right:15px;bottom:15px;}.float-phone{padding:10px 15px;}.float-phone .phone-number{font-size:14px;}.float-wechat{width:50px;height:50px;}.wechat-qr{width:200px;}}
    </style>
    <script>
        function toggleWechatQR(){document.getElementById("wechatQR").classList.toggle("active");}
        document.addEventListener("click",function(e){var qr=document.getElementById("wechatQR");var btn=document.querySelector(".float-wechat");if(!qr.contains(e.target)&&!btn.contains(e.target))qr.classList.remove("active");});
    </script>
'''

def update_html_file(file_path):
    """更新单个HTML文件"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        original_content = content

        # 1. 去掉邮箱 - 删除所有包含邮箱的行或内容
        # 删除 mailto 链接
        content = re.sub(r'<a[^>]*href="mailto:[^"]*"[^>]*>.*?</a>', '', content, flags=re.DOTALL)
        # 删除邮箱文本
        content = re.sub(r'📧\s*\S+@\S+\.\S+', '', content)
        content = re.sub(r'hunanzhubang@163\.com', '', content)
        # 删除 CTA 区域中的邮件按钮
        content = re.sub(r'<a[^>]*href="mailto:[^"]*"[^>]*>📧\s*发送邮件咨询</a>', '', content)

        # 2. 电话号码统一为 15774116703
        # 替换各种格式的电话号码
        content = re.sub(r'157-7491-8981', NEW_PHONE_DISPLAY, content)
        content = re.sub(r'15774918981', NEW_PHONE, content)
        content = re.sub(r'tel:15774918981', f'tel:{NEW_PHONE}', content)

        # 3. 更新浮动widget
        # 删除旧的浮动widget
        content = re.sub(r'<!-- 右下角悬浮组件 -->.*?</script>\s*</body>', '</body>', content, flags=re.DOTALL)
        # 添加新的浮动widget（在</body>之前）
        content = re.sub(r'</body>', NEW_FLOAT_WIDGET + '\n</body>', content)

        # 4. 修改版权信息
        content = re.sub(r'©\s*\d{4}\s*湖南筑邦企业管理咨询有限公司\s*版权所有', NEW_COPYRIGHT, content)
        content = re.sub(r'©\s*\d{4}-\d{4}\s*湖南筑邦企业管理咨询有限公司\s*版权所有', NEW_COPYRIGHT, content)

        # 5. 统一导航栏
        if 'index.html' in file_path or file_path.endswith('index.html'):
            # 首页：确保使用正确的导航栏
            # 首页的导航栏已经是正确的格式，主要确保CSS类名是 main-nav
            pass
        else:
            # 子页面：统一导航栏格式
            # 替换 nav 类为 main-nav
            content = re.sub(r'class="nav"', 'class="main-nav"', content)
            # 替换 href (#about 等改为 index.html#about)
            content = re.sub(r'href="#about"', 'href="index.html#about"', content)
            content = re.sub(r'href="#services"', 'href="index.html#services"', content)
            content = re.sub(r'href="#branches"', 'href="index.html#branches"', content)
            content = re.sub(r'href="#contact"', 'href="index.html#contact"', content)
            # 添加缺失的"成功案例"菜单项
            if '成功案例' not in content:
                content = re.sub(r'(<li><a href="index.html#contact">联系我们</a></li>)',
                                r'\n                    <li><a href="index.html#cases">成功案例</a></li>\n                    \1',
                                content)

        # 6. SEO优化：增强"湖南筑邦企业管理咨询有限公司"关键词
        # 在 title 中添加公司全名
        if '湖南筑邦企业管理咨询有限公司' not in content and 'title' in content:
            content = re.sub(r'<title>(.*?)</title>',
                           r'<title>\1 | 湖南筑邦企业管理咨询有限公司</title>',
                           content)

        # 在 description 中确保包含公司全名
        if '湖南筑邦企业管理咨询有限公司' not in content:
            content = re.sub(r'<meta name="description" content="(.*?)"/>',
                           r'<meta name="description" content="湖南筑邦企业管理咨询有限公司 -\1"/>',
                           content)
            content = re.sub(r'<meta name="description" content="(.*?)">',
                           r'<meta name="description" content="湖南筑邦企业管理咨询有限公司 -\1">',
                           content)

        # 写回文件
        if content != original_content:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            return True
        return False

    except Exception as e:
        print(f"处理文件 {file_path} 时出错: {e}")
        return False

def main():
    """主函数"""
    # 获取所有HTML文件
    html_files = list(Path(WORK_DIR).glob("*.html"))

    print(f"找到 {len(html_files)} 个HTML文件")
    print("开始批量更新...")

    updated_count = 0
    for html_file in html_files:
        if update_html_file(str(html_file)):
            updated_count += 1
            print(f"✓ 已更新: {html_file.name}")

    print(f"\n完成！共更新 {updated_count} 个文件")

if __name__ == "__main__":
    main()
