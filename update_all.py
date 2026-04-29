#!/usr/bin/env python3
"""
批量更新所有 HTML 子页面：
1. 更新公司地址（以最新正确版为准）
2. 更新电话号码为 157-7491-8981
3. 添加右下角悬浮组件（电话 + 微信二维码）
4. SEO 优化（重点关键词：湖南筑邦、湖南筑邦企业管理咨询有限公司）
"""

import os
import re

WORK_DIR = r"c:\Users\yqyzj_skzq6hr\WorkBuddy\20260425142831"

# 地址替换映射（旧地址 → 新地址）
ADDRESS_REPLACEMENTS = [
    ("润和商业广场7栋15001<", "润和商业广场7栋15001-15002<"),
    ("愿景国际广场B座815<", "愿景国际广场B座815室<"),
    ("融冠亲城6栋1504<", "沐林美郡28号公馆13楼1311-1314室<"),
    ("昌水大楼A栋707<", "欣邦写字楼10楼1019-1020室<"),
    ("国藩举集团办公楼<", "万豪城市广场7栋904室<"),
    ("盛世嘉园1栋1单元<", "步步高新天地1栋3107室<"),
    ("怡馨园小区2栋<", "柒星广场二期4楼411室<"),
    # 不带尖括号的版本
    ("润和商业广场7栋15001", "润和商业广场7栋15001-15002"),
    ("愿景国际广场B座815", "愿景国际广场B座815室"),
    ("融冠亲城6栋1504", "沐林美郡28号公馆13楼1311-1314室"),
    ("昌水大楼A栋707", "欣邦写字楼10楼1019-1020室"),
    ("国藩举集团办公楼", "万豪城市广场7栋904室"),
    ("盛世嘉园1栋1单元", "步步高新天地1栋3107室"),
    ("怡馨园小区2栋", "柒星广场二期4楼411室"),
]

# 电话替换
PHONE_REPLACEMENTS = [
    ("157-7411-6703", "157-7491-8981"),
    ("15774116703", "15774918981"),
]

# 右下角悬浮组件 HTML
FLOAT_WIDGET = """
    <!-- 右下角悬浮组件 -->
    <div class="float-widget" id="floatWidget">
        <div class="float-phone" onclick="window.location.href='tel:15774918981'">
            <svg width="24" height="24" viewBox="0 0 24 24" fill="white">
                <path d="M6.62 10.79c1.44 2.83 3.76 5.14 6.59 6.59l2.2-2.2c.27-.27.67-.36 1.02-.24 1.12.37 2.33.57 3.57.57.55 0 1 .45 1 1V20c0 .55-.45 1-1 1-9.39 0-17-7.61-17-17 0-.55.45-1 1-1h3.5c.55 0 1 .45 1 1 0 1.25.2 2.45.57 3.57.11.35.03.74-.25 1.02l-2.2 2.2z"/>
            </svg>
            <span class="float-tooltip">拨打 157-7491-8981</span>
        </div>
        <div class="float-wechat" onclick="toggleWechatQR()">
            <svg width="24" height="24" viewBox="0 0 24 24" fill="white">
                <path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm-2 15l-5-5 1.41-1.41L10 14.17l7.59-7.59L19 8l-9 9z"/>
            </svg>
            <span class="float-tooltip">微信咨询</span>
        </div>
        <div class="wechat-qr" id="wechatQR">
            <div style="width:180px;height:180px;background:#f0f0f0;border-radius:8px;display:flex;align-items:center;justify-content:center;margin:0 auto 10px;font-size:14px;color:#666;">
                请添加微信号：15774918981
            </div>
            <p style="font-size:13px;color:#666;margin:5px 0;">扫码添加微信</p>
            <p style="font-size:14px;color:#07c160;font-weight:600;">微信号：15774918981</p>
        </div>
    </div>
    <style>
        .float-widget{position:fixed;right:30px;bottom:30px;z-index:9999;display:flex;flex-direction:column;gap:15px;align-items:flex-end;}
        .float-phone,.float-wechat{width:60px;height:60px;border-radius:50%;display:flex;align-items:center;justify-content:center;cursor:pointer;transition:all 0.3s;position:relative;box-shadow:0 5px 20px rgba(0,0,0,0.3);}
        .float-phone{background:linear-gradient(135deg,#d4a843,#c49b3a);}
        .float-wechat{background:linear-gradient(135deg,#07c160,#06ad56);}
        .float-phone:hover,.float-wechat:hover{transform:scale(1.1);}
        .float-tooltip{position:absolute;right:70px;background:rgba(0,0,0,0.8);color:white;padding:8px 15px;border-radius:8px;font-size:14px;white-space:nowrap;opacity:0;transition:opacity 0.3s;pointer-events:none;}
        .float-phone:hover .float-tooltip,.float-wechat:hover .float-tooltip{opacity:1;}
        .wechat-qr{position:absolute;bottom:80px;right:0;width:250px;background:white;border-radius:16px;box-shadow:0 10px 40px rgba(0,0,0,0.2);display:none;overflow:hidden;padding:20px;text-align:center;}
        .wechat-qr.active{display:block;animation:fadeInUp 0.3s ease;}
        @keyframes fadeInUp{from{opacity:0;transform:translateY(10px);}to{opacity:1;transform:translateY(0);}}
        @media(max-width:768px){.float-widget{right:15px;bottom:15px;}.float-phone,.float-wechat{width:50px;height:50px;}.wechat-qr{width:200px;}}
    </style>
    <script>
        function toggleWechatQR(){document.getElementById("wechatQR").classList.toggle("active");}
        document.addEventListener("click",function(e){var qr=document.getElementById("wechatQR");var btn=document.querySelector(".float-wechat");if(!qr.contains(e.target)&&!btn.contains(e.target))qr.classList.remove("active");});
    </script>
"""

def update_seo(content, filename):
    """更新 SEO 部分（标题、描述、关键词）"""
    # 城市映射
    city_map = {
        "cs": "长沙", "yz": "永州", "hy": "衡阳", "yy": "岳阳",
        "ld": "娄底", "sy": "邵阳", "hh": "怀化"
    }
    
    # 判断页面类型并生成 SEO
    fname = filename.lower()
    
    if fname == "index.html":
        title = "湖南筑邦企业管理咨询有限公司 | 建筑资质代办专家 | 湖南筑邦"
        desc = "湖南筑邦企业管理咨询有限公司（简称湖南筑邦），2018年创立，专注建筑资质代办一站式服务。覆盖总承包、专业承包、劳务分包、资质交易、安许办理等，已服务1000+企业。"
        keywords = "湖南筑邦,湖南筑邦企业管理咨询有限公司,建筑资质代办,施工资质办理,资质新办,资质升级,资质转让,安许证办理"
    elif any(fname.startswith(c) for c in city_map.keys()) and "zizhi" in fname:
        city = [city_map[c] for c in city_map.keys() if fname.startswith(c)][0]
        title = f"{city}资质代办 | {city}建筑资质办理 | 湖南筑邦"
        desc = f"湖南筑邦{city}分公司，专业提供{city}建筑资质代办服务，本地化团队，面对面沟通更放心。"
        keywords = f"湖南筑邦,{city}资质代办,{city}建筑资质,{city}施工资质"
    else:
        # 其他页面
        title = f"湖南筑邦 - {filename.replace('.html','')}"
        desc = "湖南筑邦企业管理咨询有限公司，专注建筑资质代办服务。"
        keywords = "湖南筑邦,建筑资质代办"
    
    # 替换 title
    content = re.sub(r'<title>.*?</title>', f'<title>{title}</title>', content)
    
    # 替换或添加 description
    if re.search(r'<meta\s+name="description"', content):
        content = re.sub(r'<meta\s+name="description"[^>]*>', f'<meta name="description" content="{desc}">', content)
    else:
        content = content.replace('</head>', f'    <meta name="description" content="{desc}">\n</head>')
    
    # 替换或添加 keywords
    if re.search(r'<meta\s+name="keywords"', content):
        content = re.sub(r'<meta\s+name="keywords"[^>]*>', f'<meta name="keywords" content="{keywords}">', content)
    else:
        content = content.replace('</head>', f'    <meta name="keywords" content="{keywords}">\n</head>')
    
    return content

def process_file(filepath):
    """处理单个文件"""
    filename = os.path.basename(filepath)
    print(f"处理: {filename}")
    
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
    except UnicodeDecodeError:
        try:
            with open(filepath, 'r', encoding='gbk') as f:
                content = f.read()
        except Exception as e:
            print(f"  [跳过] 无法读取: {e}")
            return False
    
    original = content
    
    # 1. 更新地址
    for old, new in ADDRESS_REPLACEMENTS:
        content = content.replace(old.split('<')[0], new.split('<')[0])
    
    # 2. 更新电话
    for old, new in PHONE_REPLACEMENTS:
        content = content.replace(old, new)
    
    # 3. 添加悬浮组件
    if 'float-widget' not in content:
        content = content.replace('</body>', FLOAT_WIDGET + '\n</body>')
    
    # 4. SEO 优化
    content = update_seo(content, filename)
    
    # 保存
    if content != original:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"  [OK] 已更新")
        return True
    else:
        print(f"  [跳过] 无需更新")
        return False

def main():
    """主函数"""
    html_files = [f for f in os.listdir(WORK_DIR) if f.endswith('.html') and f != 'index.html']
    html_files.sort()
    
    print(f"找到 {len(html_files)} 个子页面")
    print("=" * 50)
    
    success = 0
    for filename in html_files:
        filepath = os.path.join(WORK_DIR, filename)
        if process_file(filepath):
            success += 1
    
    print("=" * 50)
    print(f"[完成] 共处理 {len(html_files)} 个文件，成功更新 {success} 个")

if __name__ == "__main__":
    main()
