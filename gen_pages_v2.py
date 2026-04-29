#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
批量生成 50 个筑邦资质代办子页面 - 简化版
"""

import os

# 页面配置列表
PAGES = [
    {"file": "zizhi-zhuanyechengbao.html", "title": "专业承包资质办理", "h1": "专业承包资质办理", "desc": "提供36项专业承包资质代办服务"},
    {"file": "zizhi-laowufenbao.html", "title": "劳务分包资质办理", "h1": "劳务分包资质办理", "desc": "施工劳务资质新办、延期、变更"},
    {"file": "zizhi-jiaoyi.html", "title": "资质交易服务", "h1": "资质交易服务", "desc": "整体收购、重组分立、吸收合并、地址迁移"},
    {"file": "zizhi-anxuzheng.html", "title": "安全生产许可证办理", "h1": "安全生产许可证办理", "desc": "安许证新办、延期、变更"},
    {"file": "zizhi-shengji.html", "title": "资质升级服务", "h1": "资质升级服务", "desc": "二级升一级、一级升特级"},
    {"file": "zizhi-zengxiang.html", "title": "资质增项服务", "h1": "资质增项服务", "desc": "拓展企业经营范围"},
    {"file": "zizhi-yanqi.html", "title": "资质延期服务", "h1": "资质延期服务", "desc": "资质证书有效期延续"},
    {"file": "zizhi-biange.html", "title": "资质变更服务", "h1": "资质变更服务", "desc": "法人、地址、注册资本变更"},
    {"file": "jianzhu-zongbao.html", "title": "建筑工程总承包资质", "h1": "建筑工程总承包资质", "desc": "建筑总包二级新办40-50万"},
    {"file": "shizheng-zongbao.html", "title": "市政工程总承包资质", "h1": "市政工程总承包资质", "desc": "市政总包二级新办50-60万"},
    {"file": "gonglu-zongbao.html", "title": "公路工程总承包资质", "h1": "公路工程总承包资质", "desc": "公路工程总承包资质办理"},
    {"file": "shuili-zongbao.html", "title": "水利水电工程总承包资质", "h1": "水利水电工程总承包资质", "desc": "水利水电工程总承包资质办理"},
    {"file": "dianli-zongbao.html", "title": "电力工程总承包资质", "h1": "电力工程总承包资质", "desc": "电力工程总承包资质办理"},
    {"file": "jidian-zhuanye.html", "title": "机电工程专业承包资质", "h1": "机电工程专业承包资质", "desc": "建筑机电安装工程专业承包"},
    {"file": "fangshui-zhuanye.html", "title": "防水防腐保温工程专业承包资质", "h1": "防水防腐保温工程专业承包", "desc": "防水防腐保温工程专业承包资质"},
    {"file": "gangjiegou-zhuanye.html", "title": "钢结构工程专业承包资质", "h1": "钢结构工程专业承包资质", "desc": "钢结构工程专业承包资质办理"},
    {"file": "mujia-jumiao.html", "title": "模板脚手架专业承包资质", "h1": "模板脚手架专业承包资质", "desc": "模板脚手架专业承包不分等级"},
    {"file": "jianzhu-muqiang.html", "title": "建筑幕墙工程专业承包资质", "h1": "建筑幕墙工程专业承包资质", "desc": "建筑幕墙工程专业承包资质"},
    {"file": "dianzi-zhineng.html", "title": "电子与智能化工程专业承包资质", "h1": "电子与智能化工程专业承包", "desc": "电子与智能化工程专业承包资质"},
    {"file": "jiaoyi-zhengtishougou.html", "title": "整体收购资质转让", "h1": "整体收购资质转让", "desc": "整体收购具备中大型资质的企业"},
    {"file": "jiaoyi-chongzufenli.html", "title": "重组分立资质转让", "h1": "重组分立资质转让", "desc": "重组分立实现零风险资质转让"},
    {"file": "jiaoyi-xishouhebing.html", "title": "吸收合并资质转让", "h1": "吸收合并资质转让", "desc": "吸收合并直接将资质吸收进母公司"},
    {"file": "jiaoyi-dizhiqianyi.html", "title": "地址迁移资质转让", "h1": "地址迁移资质转让", "desc": "资质地址迁移服务"},
    {"file": "cs-zizhi.html", "title": "长沙资质代办", "h1": "长沙资质代办", "desc": "湖南筑邦总部位于长沙"},
    {"file": "yz-zizhi.html", "title": "永州资质代办", "h1": "永州资质代办", "desc": "永州分公司位于冷水滩区"},
    {"file": "hy-zizhi.html", "title": "衡阳资质代办", "h1": "衡阳资质代办", "desc": "衡阳分公司位于蒸湘区"},
    {"file": "yy-zizhi.html", "title": "岳阳资质代办", "h1": "岳阳资质代办", "desc": "岳阳分公司位于岳阳楼区"},
    {"file": "ld-zizhi.html", "title": "娄底资质代办", "h1": "娄底资质代办", "desc": "娄底分公司位于娄星区"},
    {"file": "sy-zizhi.html", "title": "邵阳资质代办", "h1": "邵阳资质代办", "desc": "邵阳分公司位于大祥区"},
    {"file": "hh-zizhi.html", "title": "怀化资质代办", "h1": "怀化资质代办", "desc": "怀化分公司位于鹤城区"},
    {"file": "know-shenmeshizizhi.html", "title": "什么是建筑资质", "h1": "什么是建筑资质", "desc": "建筑资质是建筑企业的行业身份证"},
    {"file": "know-zizhifenlei.html", "title": "建筑资质分类详解", "h1": "建筑资质分类详解", "desc": "总承包、专业承包、劳务三大类"},
    {"file": "know-banliliucheng.html", "title": "资质办理流程详解", "h1": "资质办理流程详解", "desc": "咨询评估到拿证的全流程"},
    {"file": "know-shengjizhinan.html", "title": "资质升级指南", "h1": "资质升级指南", "desc": "提高资质等级承接更大工程"},
    {"file": "know-zengxiangzhinan.html", "title": "资质增项指南", "h1": "资质增项指南", "desc": "拓展企业经营范围"},
    {"file": "know-yanqizhinan.html", "title": "资质延期指南", "h1": "资质延期指南", "desc": "资质证书5年有效期延续"},
    {"file": "know-biangezhinan.html", "title": "资质变更指南", "h1": "资质变更指南", "desc": "法人、地址、注册资本变更"},
    {"file": "know-anxuzheng.html", "title": "安许证办理指南", "h1": "安许证办理指南", "desc": "安全生产许可证办理指南"},
    {"file": "know-jianzaoshi.html", "title": "建造师要求详解", "h1": "建造师要求详解", "desc": "不同资质对建造师数量要求"},
    {"file": "know-changjianwenti.html", "title": "资质办理常见问题", "h1": "资质办理常见问题", "desc": "关于资质办理的常见疑问解答"},
    {"file": "case-zongbao.html", "title": "总承包资质成功案例", "h1": "总承包资质成功案例", "desc": "1000+企业总承包资质代办案例"},
    {"file": "case-zhuanye.html", "title": "专业承包资质成功案例", "h1": "专业承包资质成功案例", "desc": "36项专业承包资质办理案例"},
    {"file": "case-laowu.html", "title": "劳务资质成功案例", "h1": "劳务资质成功案例", "desc": "施工劳务资质办理成功案例"},
    {"file": "case-jiaoyi.html", "title": "资质交易成功案例", "h1": "资质交易成功案例", "desc": "整体收购、重组分立成功案例"},
    {"file": "case-anxu.html", "title": "安许证办理成功案例", "h1": "安许证办理成功案例", "desc": "安全生产许可证办理案例"},
    {"file": "about-intro.html", "title": "公司简介", "h1": "公司简介", "desc": "湖南筑邦企业管理咨询有限公司简介"},
    {"file": "about-process.html", "title": "服务流程", "h1": "服务流程", "desc": "四步轻松拿证服务流程"},
    {"file": "about-team.html", "title": "团队介绍", "h1": "团队介绍", "desc": "湖南筑邦专业顾问团队"},
    {"file": "about-contact.html", "title": "联系我们", "h1": "联系我们", "desc": "7家分公司联系信息"},
]

CSS = """
        * { margin:0; padding:0; box-sizing:border-box; }
        body { font-family:"Microsoft YaHei",sans-serif; line-height:1.6; color:#2d3748; background:#f7fafc; }
        .header { background:rgba(26,35,50,0.95); padding:15px 0; position:fixed; top:0; left:0; right:0; z-index:1000; }
        .header-inner { max-width:1200px; margin:0 auto; padding:0 20px; display:flex; justify-content:space-between; align-items:center; }
        .logo { display:flex; align-items:center; gap:15px; text-decoration:none; color:white; }
        .logo-icon { width:50px; height:50px; background:linear-gradient(135deg,#d4a843,#ecc94b); border-radius:12px; display:flex; align-items:center; justify-content:center; font-size:24px; font-weight:bold; color:#1a2332; }
        .logo-text h1 { font-size:20px; color:white; margin-bottom:2px; }
        .logo-text p { font-size:11px; color:#d4a843; letter-spacing:2px; }
        .nav { display:flex; gap:30px; list-style:none; }
        .nav a { color:rgba(255,255,255,0.8); text-decoration:none; font-size:14px; }
        .nav a:hover { color:#d4a843; }
        .page-hero { background:linear-gradient(135deg,#1a2332,#2c5282); padding:180px 20px 100px; text-align:center; color:white; }
        .page-hero h2 { font-size:48px; margin-bottom:20px; }
        .page-hero p { font-size:18px; opacity:0.9; max-width:800px; margin:0 auto; }
        .page-content { max-width:1200px; margin:0 auto; padding:100px 20px; }
        .page-content h3 { font-size:28px; color:#1a2332; margin-bottom:20px; }
        .page-content p { font-size:15px; color:#718096; line-height:1.8; margin-bottom:20px; }
        .features { display:grid; grid-template-columns:repeat(3,1fr); gap:30px; margin:40px 0; }
        .feature-card { background:white; padding:30px; border-radius:16px; box-shadow:0 5px 20px rgba(0,0,0,0.1); }
        .feature-card h4 { font-size:18px; color:#1a2332; margin-bottom:10px; }
        .feature-card p { font-size:14px; color:#718096; }
        .cta-section { background:linear-gradient(135deg,#1a2332,#2c5282); padding:80px 20px; text-align:center; color:white; }
        .cta-section h2 { font-size:36px; margin-bottom:20px; }
        .cta-section p { font-size:16px; opacity:0.9; margin-bottom:30px; }
        .cta-btn { display:inline-block; background:#d4a843; color:#1a2332; padding:15px 40px; border-radius:30px; text-decoration:none; font-weight:bold; font-size:16px; }
        .footer { background:#0d1117; color:rgba(255,255,255,0.8); padding:60px 20px 30px; }
        .footer-inner { max-width:1200px; margin:0 auto; }
        .footer-grid { display:grid; grid-template-columns:2fr 1fr 1fr 1fr; gap:40px; margin-bottom:40px; }
        .footer h3 { font-size:20px; color:white; margin-bottom:15px; }
        .footer p { font-size:14px; line-height:1.8; opacity:0.7; }
        .footer-links { list-style:none; }
        .footer-links li { margin-bottom:10px; }
        .footer-links a { color:rgba(255,255,255,0.7); text-decoration:none; font-size:14px; }
        .footer-bottom { border-top:1px solid rgba(255,255,255,0.1); padding-top:20px; text-align:center; font-size:13px; opacity:0.5; }
        @media (max-width:768px) { .nav { display:none; } .features { grid-template-columns:1fr; } .footer-grid { grid-template-columns:1fr; } }
"""

TEMPLATE = """<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} | 湖南筑邦</title>
    <meta name="description" content="{desc}">
    <style>{css}</style>
</head>
<body>
    <header class="header">
        <div class="header-inner">
            <a href="index.html" class="logo">
                <div class="logo-icon">筑</div>
                <div class="logo-text"><h1>湖南筑邦</h1><p>建筑资质代办专家</p></div>
            </a>
            <ul class="nav">
                <li><a href="index.html#about">关于我们</a></li>
                <li><a href="index.html#services">服务项目</a></li>
                <li><a href="index.html#branches">分公司</a></li>
                <li><a href="index.html#contact">联系我们</a></li>
            </ul>
        </div>
    </header>
    <section class="page-hero">
        <h2>{h1}</h2>
        <p>{desc}</p>
    </section>
    <div class="page-content">
        <h3>服务介绍</h3>
        <p>湖南筑邦企业管理咨询有限公司，品牌创立于2018年，是一家专注于建筑资质代办服务的专业机构。</p>
        <p>公司秉承"专业的事交给专业的人"的服务理念，致力于为建筑企业提供高效、合规、零风险的资质解决方案。</p>
        <div class="features">
            <div class="feature-card"><h4>⚡ 效率高</h4><p>1对1专人全程跟进，让资质办理省时省心</p></div>
            <div class="feature-card"><h4>🎓 专业强</h4><p>建筑行业服务领域深耕十余年，精准把握政策法规</p></div>
            <div class="feature-card"><h4>💰 价格优</h4><p>报价内容公开透明，提供严谨、灵活、全面的解决方案</p></div>
        </div>
    </div>
    <section class="cta-section">
        <h2>免费获取资质办理方案</h2>
        <p>专业顾问一对一服务，为您量身定制资质办理方案</p>
        <a href="tel:15774116703" class="cta-btn">📞 立即咨询 157-7411-6703</a>
    </section>
    <footer class="footer">
        <div class="footer-inner">
            <div class="footer-grid">
                <div>
                    <h3>湖南筑邦</h3>
                    <p>专为建筑业企业提供资质服务的一站式服务公司。</p>
                </div>
                <div>
                    <h3>快速链接</h3>
                    <ul class="footer-links">
                        <li><a href="index.html">首页</a></li>
                        <li><a href="about-intro.html">公司简介</a></li>
                        <li><a href="know-changjianwenti.html">常见问题</a></li>
                    </ul>
                </div>
                <div>
                    <h3>服务项目</h3>
                    <ul class="footer-links">
                        <li><a href="zizhi-zongchengbao.html">总承包资质</a></li>
                        <li><a href="zizhi-zhuanyechengbao.html">专业承包资质</a></li>
                        <li><a href="zizhi-laowufenbao.html">劳务分包资质</a></li>
                    </ul>
                </div>
                <div>
                    <h3>联系我们</h3>
                    <ul class="footer-links">
                        <li>📞 157-7411-6703</li>
                        <li>📍 长沙市开福区福元西路96号</li>
                    </ul>
                </div>
            </div>
            <div class="footer-bottom"><p>© 2026 湖南筑邦企业管理咨询有限公司 版权所有</p></div>
        </div>
    </footer>
</body>
</html>"""

def main():
    output_dir = os.path.dirname(os.path.abspath(__file__))
    print(f"开始生成 {len(PAGES)} 个子页面...")
    
    for i, page in enumerate(PAGES, 1):
        try:
            html = TEMPLATE.format(
                title=page["title"],
                desc=page["desc"],
                h1=page["h1"],
                css=CSS
            )
            filepath = os.path.join(output_dir, page["file"])
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(html)
            print(f"[{i}/{len(PAGES)}] [OK] {page['file']}")
        except Exception as e:
            print(f"[{i}/{len(PAGES)}] [ERR] {page['file']} - {e}")

    print(f"\n[OK] 生成完成！共 {len(PAGES)} 个页面")

if __name__ == "__main__":
    main()
