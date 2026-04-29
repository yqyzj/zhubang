#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
批量生成 50 个筑邦资质代办子页面
使用方法：python generate_pages.py
"""

import os

# 页面配置：50 个子页面
PAGES = [
    # Group 1: 资质服务详情页 (20 pages)
    {
        "file": "zizhi-zongchengbao.html",
        "title": "施工总承包资质办理 | 湖南筑邦",
        "desc": "湖南筑邦提供建筑工程、市政公用、公路工程等12项总承包资质新办、升级、增项服务",
        "h1": "施工总承包资质办理",
        "content": "施工总承包资质是建筑企业的核心资质，分为12个类别。湖南筑邦专注总承包资质代办服务，助力企业快速取得资质证书，合法承接工程项目。"
    },
    {
        "file": "zizhi-zhuanyechengbao.html",
        "title": "专业承包资质办理 | 湖南筑邦",
        "desc": "提供地基基础、起重设备、预拌混凝土等36项专业承包资质代办服务",
        "h1": "专业承包资质办理",
        "content": "专业承包资质共36项，涵盖地基基础、起重设备安装、预拌混凝土、消防设施、防水防腐保温等多个专业领域。"
    },
    {
        "file": "zizhi-laowufenbao.html",
        "title": "劳务分包资质办理 | 湖南筑邦",
        "desc": "施工劳务资质新办、延期、变更，快速对接住建部门",
        "h1": "劳务分包资质办理",
        "content": "施工劳务资质是从事建筑劳务作业的企业必须取得的资质。湖南筑邦提供劳务资质新办、延期、变更一站式服务。"
    },
    {
        "file": "zizhi-jiaoyi.html",
        "title": "资质交易服务 | 湖南筑邦",
        "desc": "整体收购、重组分立、吸收合并、地址迁移等资质交易服务",
        "h1": "资质交易服务",
        "content": "资质交易是企业快速获取高等级资质的捷径。湖南筑邦提供整体收购、重组分立、吸收合并、地址迁移等多种交易方式，60天快速办结。"
    },
    {
        "file": "zizhi-anxuzheng.html",
        "title": "安全生产许可证办理 | 湖南筑邦",
        "desc": "安全生产许可证新办、延期、变更，确保企业合法施工",
        "h1": "安全生产许可证办理",
        "content": "根据《建筑施工企业安全生产许可证管理规定》，建筑施工企业未取得安全生产许可证的，不得从事建筑施工活动。"
    },
    {
        "file": "zizhi-shengji.html",
        "title": "资质升级服务 | 湖南筑邦",
        "desc": "建筑资质升级，提高资质等级，承接更大工程项目",
        "h1": "资质升级服务",
        "content": "资质升级是提高企业实力的重要途径。湖南筑邦协助企业完成二级升一级、一级升特级等资质升级服务，提供业绩整理、人员配备等全方位支持。"
    },
    {
        "file": "zizhi-zengxiang.html",
        "title": "资质增项服务 | 湖南筑邦",
        "desc": "建筑企业资质增项办理，拓展企业经营范围",
        "h1": "资质增项服务",
        "content": "资质增项是指在原有资质基础上，增加其他类别的资质。湖南筑邦协助企业办理资质增项，拓展业务范围，提升市场竞争力。"
    },
    {
        "file": "zizhi-yanqi.html",
        "title": "资质延期服务 | 湖南筑邦",
        "desc": "建筑资质延期办理，提前3个月准备，确保资质有效延续",
        "h1": "资质延期服务",
        "content": "建筑资质证书有效期为5年，需在到期前3个月申请延期。湖南筑邦提供资质延期一站式服务，确保企业资质有效延续。"
    },
    {
        "file": "zizhi-biange.html",
        "title": "资质变更服务 | 湖南筑邦",
        "desc": "建筑资质变更办理，企业法人、地址、注册资本等变更",
        "h1": "资质变更服务",
        "content": "企业在经营过程中发生法人、地址、注册资本等变更时，需要及时办理资质变更手续。湖南筑邦协助企业快速完成资质变更。"
    },
    {
        "file": "jianzhu-zongbao.html",
        "title": "建筑工程总承包资质 | 湖南筑邦",
        "desc": "建筑工程总承包二级新办40-50万，不含社保，时间6-8个月",
        "h1": "建筑工程总承包资质",
        "content": "建筑工程总承包资质是承接房屋建筑工程的必备资质。湖南筑邦专业代办建筑总包二级新办、升级服务，价格透明，办理高效。"
    },
    {
        "file": "shizheng-zongbao.html",
        "title": "市政工程总承包资质 | 湖南筑邦",
        "desc": "市政公用工程总承包二级新办50-60万，不含社保，时间6-8个月",
        "h1": "市政工程总承包资质",
        "content": "市政公用工程总承包资质是承接城市道路、桥梁、隧道等市政工程的必备资质。湖南筑邦专业代办市政总包资质。"
    },
    {
        "file": "gonglu-zongbao.html",
        "title": "公路工程总承包资质 | 湖南筑邦",
        "desc": "公路工程总承包资质办理，专业团队全程跟进",
        "h1": "公路工程总承包资质",
        "content": "公路工程总承包资质是承接公路工程的必备资质。湖南筑邦拥有丰富的公路资质办理经验，助力企业快速取得资质。"
    },
    {
        "file": "shuili-zongbao.html",
        "title": "水利水电工程总承包资质 | 湖南筑邦",
        "desc": "水利水电工程总承包资质办理，专业可靠",
        "h1": "水利水电工程总承包资质",
        "content": "水利水电工程总承包资质是承接水利水电工程的必备资质。湖南筑邦提供水利水电资质新办、升级、增项等全方位服务。"
    },
    {
        "file": "dianli-zongbao.html",
        "title": "电力工程总承包资质 | 湖南筑邦",
        "desc": "电力工程总承包资质办理，高效专业",
        "h1": "电力工程总承包资质",
        "content": "电力工程总承包资质是承接电力工程的必备资质。湖南筑邦专业代办电力总包资质，熟悉办理流程，通过率高。"
    },
    {
        "file": "jidian-zhuanye.html",
        "title": "机电工程专业承包资质 | 湖南筑邦",
        "desc": "建筑机电安装工程专业承包资质办理",
        "h1": "机电工程专业承包资质",
        "content": "建筑机电安装工程专业承包资质是承接机电设备安装工程的必备资质。湖南筑邦提供机电资质新办、升级服务。"
    },
    {
        "file": "fangshui-zhuanye.html",
        "title": "防水防腐保温工程专业承包资质 | 湖南筑邦",
        "desc": "防水防腐保温工程专业承包资质办理",
        "h1": "防水防腐保温工程专业承包资质",
        "content": "防水防腐保温工程专业承包资质是承接建筑防水、防腐、保温工程的必备资质。"
    },
    {
        "file": "gangjiegou-zhuanye.html",
        "title": "钢结构工程专业承包资质 | 湖南筑邦",
        "desc": "钢结构工程专业承包资质办理",
        "h1": "钢结构工程专业承包资质",
        "content": "钢结构工程专业承包资质是承接钢结构工程的必备资质。湖南筑邦专业代办钢结构资质，经验丰富。"
    },
    {
        "file": "miaojia-jumiao.html",
        "title": "模板脚手架专业承包资质 | 湖南筑邦",
        "desc": "模板脚手架专业承包资质办理，不分类别",
        "h1": "模板脚手架专业承包资质",
        "content": "模板脚手架专业承包资质不分等级，是承接模板、脚手架工程的必备资质。"
    },
    {
        "file": "jianzhu-muqiang.html",
        "title": "建筑幕墙工程专业承包资质 | 湖南筑邦",
        "desc": "建筑幕墙工程专业承包资质办理",
        "h1": "建筑幕墙工程专业承包资质",
        "content": "建筑幕墙工程专业承包资质是承接建筑幕墙工程的必备资质。湖南筑邦提供幕墙资质新办、升级服务。"
    },
    {
        "file": "dianzi-zhineng.html",
        "title": "电子与智能化工程专业承包资质 | 湖南筑邦",
        "desc": "电子与智能化工程专业承包资质办理",
        "h1": "电子与智能化工程专业承包资质",
        "content": "电子与智能化工程专业承包资质是承接智能化工程的必备资质。湖南筑邦专业代办电子与智能化资质。"
    },
    # Group 2: 资质交易方式详情页 (4 pages)
    {
        "file": "jiaoyi-zhengtishougou.html",
        "title": "整体收购资质转让 | 湖南筑邦",
        "desc": "整体收购具备中大型资质的企业，60天快速办结",
        "h1": "整体收购资质转让",
        "content": "整体收购是指对拥有指定资质企业股权的整体收购，包括公司资质、资产、债权债务、劳动关系、税务、合同等。优势：办理时长最快，可将业绩、奖项、荣誉同时收购。"
    },
    {
        "file": "jiaoyi-chongzufenli.html",
        "title": "重组分立资质转让 | 湖南筑邦",
        "desc": "重组分立实现零风险资质转让，无债权债务纠纷",
        "h1": "重组分立资质转让",
        "content": "重组分立是指在企业与其全资子公司之间、或各全资子公司间进行主营业务资产、人员转移，在资质总量不增加的情况下，企业申请资质全部或部分转移。"
    },
    {
        "file": "jiaoyi-xishouhebing.html",
        "title": "吸收合并资质转让 | 湖南筑邦",
        "desc": "吸收合并直接将资质吸收进母公司，时间快",
        "h1": "吸收合并资质转让",
        "content": "吸收合并是指一个企业吸收另一个企业，被吸收企业已办理工商注销登记并提出资质证书注销申请，企业申请被吸收企业的资质。"
    },
    {
        "file": "jiaoyi-dizhiqianyi.html",
        "title": "地址迁移资质转让 | 湖南筑邦",
        "desc": "资质地址迁移服务，实现跨区域资质转移",
        "h1": "地址迁移资质转让",
        "content": "地址迁移是指将目标公司的工商注册地从原地址迁至新的注册地址，同时将税务、资质等的登记地址进行变更。"
    },
    # Group 3: 城市分站页面 (7 pages)
    {
        "file": "cs-zizhi.html",
        "title": "长沙资质代办 | 湖南筑邦总部",
        "desc": "长沙资质代办专业服务，湖南筑邦总部位于开福区福元西路96号润和商业广场",
        "h1": "长沙资质代办",
        "content": "湖南筑邦企业管理咨询有限公司总部位于长沙市开福区福元西路96号润和商业广场7栋15001-15002。作为湖南本土建筑资质代办领导品牌，为长沙建筑企业提供一站式资质代办服务。"
    },
    {
        "file": "yz-zizhi.html",
        "title": "永州资质代办 | 湖南筑邦",
        "desc": "永州资质代办专业服务，分公司位于冷水滩区愿景国际广场B座815",
        "h1": "永州资质代办",
        "content": "湖南筑邦永州分公司位于永州市冷水滩区愿景国际广场B座815。扎根永州，熟悉永州住建局办事流程和政策要求，为永州建筑企业提供本地化资质代办服务。"
    },
    {
        "file": "hy-zizhi.html",
        "title": "衡阳资质代办 | 湖南筑邦",
        "desc": "衡阳资质代办专业服务，分公司位于蒸湘区船山大道融冠亲城6栋1504",
        "h1": "衡阳资质代办",
        "content": "湖南筑邦衡阳分公司位于衡阳市蒸湘区船山大道融冠亲城6栋1504。为衡阳建筑企业提供专业资质代办服务，熟悉当地政策法规。"
    },
    {
        "file": "yy-zizhi.html",
        "title": "岳阳资质代办 | 湖南筑邦",
        "desc": "岳阳资质代办专业服务，分公司位于岳阳楼区五里牌路昌水大楼A栋707",
        "h1": "岳阳资质代办",
        "content": "湖南筑邦岳阳分公司位于岳阳市岳阳楼区五里牌路昌水大楼A栋707。为岳阳建筑企业提供高效、合规的资质代办服务。"
    },
    {
        "file": "ld-zizhi.html",
        "title": "娄底资质代办 | 湖南筑邦",
        "desc": "娄底资质代办专业服务，分公司位于娄星区湘中大道国藩举集团办公楼",
        "h1": "娄底资质代办",
        "content": "湖南筑邦娄底分公司位于娄底市娄星区湘中大道国藩举集团办公楼。为娄底建筑企业提供专业资质代办服务。"
    },
    {
        "file": "sy-zizhi.html",
        "title": "邵阳资质代办 | 湖南筑邦",
        "desc": "邵阳资质代办专业服务，分公司位于大祥区邵州路盛世嘉园1栋1单元",
        "h1": "邵阳资质代办",
        "content": "湖南筑邦邵阳分公司位于邵阳市大祥区邵州路盛世嘉园1栋1单元。为邵阳建筑企业提供本地化资质代办服务。"
    },
    {
        "file": "hh-zizhi.html",
        "title": "怀化资质代办 | 湖南筑邦",
        "desc": "怀化资质代办专业服务，分公司位于鹤城区锦园路怡馨园小区2栋",
        "h1": "怀化资质代办",
        "content": "湖南筑邦怀化分公司位于怀化市鹤城区锦园路怡馨园小区2栋。为怀化建筑企业提供专业资质代办服务。"
    },
    # Group 4: 资质知识/FAQ页面 (10 pages)
    {
        "file": "know-shenmeshizizhi.html",
        "title": "什么是建筑资质 | 湖南筑邦",
        "desc": "建筑资质是建筑企业的行业身份证和能力证明，没有它无法合法承接工程",
        "h1": "什么是建筑资质",
        "content": "建筑工程资质就是建筑公司的行业身份证和能力证明。没有它，公司就无法合法承接工程项目，就像无证驾驶一样，属于违法行为。建筑企业只有取得相应建筑资质，方可从事资质证书许可范围内的相应工程承包、工程项目管理等业务。"
    },
    {
        "file": "know-zizhifenlei.html",
        "title": "建筑资质分类详解 | 湖南筑邦",
        "desc": "建筑施工资质分为总承包、专业承包及劳务三大类",
        "h1": "建筑资质分类详解",
        "content": "建筑施工资质分为三大类：施工总承包资质（12项）、专业承包资质（36项）、施工劳务资质（1项）。不同资质对应不同的工程范围和承接能力。"
    },
    {
        "file": "know-banlilicheng.html",
        "title": "资质办理流程详解 | 湖南筑邦",
        "desc": "资质办理流程：咨询评估→签约付款→整理材料→递交申请→拿证",
        "h1": "资质办理流程详解",
        "content": "资质办理流程包括：1. 免费咨询评估；2. 签约付款启动；3. 整理递交材料；4. 拿证后续服务。湖南筑邦提供全程一对一服务，让资质办理省心无忧。"
    },
    {
        "file": "know-shengjizhinan.html",
        "title": "资质升级指南 | 湖南筑邦",
        "desc": "建筑资质升级提高资质等级，等级越高企业实力越强",
        "h1": "资质升级指南",
        "content": "建筑资质升级是提高资质等级的过程。等级越高，企业的实力越强，承接的项目也就越大，利润空间也就越大。升级需要企业提供符合升级标准的业绩、人员、厂房、设备等证明。"
    },
    {
        "file": "know-zengxiangzhinan.html",
        "title": "资质增项指南 | 湖南筑邦",
        "desc": "资质增项拓展企业经营范围，提升市场竞争力",
        "h1": "资质增项指南",
        "content": "资质增项是指在原有资质基础上，增加其他类别的资质。通过增项，企业可以拓展经营范围，承接更多类型的工程项目，提升市场竞争力。"
    },
    {
        "file": "know-yanqizhinan.html",
        "title": "资质延期指南 | 湖南筑邦",
        "desc": "资质证书有效期5年，需在到期前3个月申请延期",
        "h1": "资质延期指南",
        "content": "建筑资质证书有效期为5年。企业应在资质证书有效期届满3个月前，向原资质许可机关提出延续申请。湖南筑邦提供资质延期一站式服务。"
    },
    {
        "file": "know-biangezhinan.html",
        "title": "资质变更指南 | 湖南筑邦",
        "desc": "企业法人、地址、注册资本等变更需及时办理资质变更",
        "h1": "资质变更指南",
        "content": "企业在经营过程中发生法人、地址、注册资本等变更时，需要在规定时间内办理资质变更手续。湖南筑邦协助企业快速完成资质变更。"
    },
    {
        "file": "know-anxuzheng.html",
        "title": "安许证办理指南 | 湖南筑邦",
        "desc": "安全生产许可证是建筑施工企业合法施工的必要条件",
        "h1": "安许证办理指南",
        "content": "根据《建筑施工企业安全生产许可证管理规定》，建筑施工企业未取得安全生产许可证的，不得从事建筑施工活动。湖南筑邦提供安许证新办、延期、变更服务。"
    },
    {
        "file": "know-jianzaoshi.html",
        "title": "建造师要求详解 | 湖南筑邦",
        "desc": "不同资质对建造师数量和专业有不同要求",
        "h1": "建造师要求详解",
        "content": "建筑总包二级需要：注册建造师5人（建筑专业）、中级职称人员6人、施工现场管理人员15人、中级技术工人30人。不同资质对人员要求不同，湖南筑邦提供专业配备方案。"
    },
    {
        "file": "know-changjianwenti.html",
        "title": "资质办理常见问题 | 湖南筑邦",
        "desc": "关于建筑资质办理，您关心的问题都在这里",
        "h1": "资质办理常见问题",
        "content": "湖南筑邦整理资质办理常见问题：办理时间、办理费用、人员要求、不成功怎么办等。专业顾问一对一解答，让您省心放心。"
    },
    # Group 5: 成功案例页面 (5 pages)
    {
        "file": "case-zongbao.html",
        "title": "总承包资质成功案例 | 湖南筑邦",
        "desc": "已为1000+企业提供总承包资质代办服务，成功率高",
        "h1": "总承包资质成功案例",
        "content": "湖南筑邦已为1000+企业提供总承包资质代办服务。案例涵盖建筑工程、市政公用工程、公路工程等多个领域，办理周期短，通过率高。"
    },
    {
        "file": "case-zhuanye.html",
        "title": "专业承包资质成功案例 | 湖南筑邦",
        "desc": "36项专业承包资质办理案例，经验丰富",
        "h1": "专业承包资质成功案例",
        "content": "湖南筑邦已成功办理数百项专业承包资质，涵盖地基基础、消防设施、防水防腐保温、钢结构工程等多个专业领域。"
    },
    {
        "file": "case-laowu.html",
        "title": "劳务资质成功案例 | 湖南筑邦",
        "desc": "施工劳务资质办理成功案例，快速高效",
        "h1": "劳务资质成功案例",
        "content": "湖南筑邦已为数百家企业成功办理施工劳务资质。劳务资质办理周期短（1-2个月），通过率高，是初创建筑企业的首选。"
    },
    {
        "file": "case-jiaoyi.html",
        "title": "资质交易成功案例 | 湖南筑邦",
        "desc": "整体收购、重组分立等资质交易成功案例",
        "h1": "资质交易成功案例",
        "content": "湖南筑邦已成功完成数十项资质交易案例，包括整体收购、重组分立、吸收合并、地址迁移等多种方式，60天快速办结。"
    },
    {
        "file": "case-anxu.html",
        "title": "安许证办理成功案例 | 湖南筑邦",
        "desc": "安全生产许可证新办、延期成功案例",
        "h1": "安许证办理成功案例",
        "content": "湖南筑邦已为数百家企业成功办理安全生产许可证。安许证是建筑施工企业合法施工的必要条件，需与资质证书配套使用。"
    },
    # Group 6: 关于我们相关页面 (4 pages)
    {
        "file": "about-intro.html",
        "title": "公司简介 | 湖南筑邦",
        "desc": "湖南筑邦企业管理咨询有限公司，2018年创立，专注建筑资质代办",
        "h1": "公司简介",
        "content": "湖南筑邦企业管理咨询有限公司，品牌创立于2018年，是一家专注于建筑资质代办服务的专业机构。公司秉承专业的事交给专业的人的服务理念，致力于为建筑企业提供高效、合规、零风险的资质解决方案。"
    },
    {
        "file": "about-process.html",
        "title": "服务流程 | 湖南筑邦",
        "desc": "四步轻松拿证：咨询评估→签约付款→整理材料→拿证后续服务",
        "h1": "服务流程",
        "content": "湖南筑邦标准化服务流程：第一步：免费咨询评估；第二步：签约付款启动；第三步：整理递交材料；第四步：拿证后续服务。全程一对一服务，让资质办理省心无忧。"
    },
    {
        "file": "about-team.html",
        "title": "团队介绍 | 湖南筑邦",
        "desc": "湖南筑邦专业顾问团队，深耕建筑资质代办领域十余年",
        "h1": "团队介绍",
        "content": "湖南筑邦拥有一支专业的顾问团队，深耕建筑资质代办领域十余年，精准把握政策法规，熟悉办理流程，已为1000+企业提供专业服务。"
    },
    {
        "file": "about-contact.html",
        "title": "联系我们 | 湖南筑邦",
        "desc": "7家分公司，为湖南建筑企业提供本地化服务",
        "h1": "联系我们",
        "content": "湖南筑邦在长沙、永州、衡阳、岳阳、娄底、邵阳、怀化等地设立分公司。联系电话：157-7411-6703（刘女士，微信同号）。服务时间：周一至周日 8:00-22:00。"
    },
]

TEMPLATE = '''<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
    <meta name="description" content="{desc}">
    <meta name="keywords" content="建筑资质代办,资质办理,湖南筑邦,{extra_keywords}">
    <style>
        * {{ margin:0; padding:0; box-sizing:border-box; }}
        body {{ font-family:"Microsoft YaHei",sans-serif; line-height:1.6; color:#2d3748; background:#f7fafc; }}
        .header {{ background:rgba(26,35,50,0.95); padding:15px 0; position:fixed; top:0; left:0; right:0; z-index:1000; }}
        .header-inner {{ max-width:1200px; margin:0 auto; padding:0 20px; display:flex; justify-content:space-between; align-items:center; }}
        .logo {{ display:flex; align-items:center; gap:15px; text-decoration:none; color:white; }}
        .logo-icon {{ width:50px; height:50px; background:linear-gradient(135deg,#d4a843,#ecc94b); border-radius:12px; display:flex; align-items:center; justify-content:center; font-size:24px; font-weight:bold; color:#1a2332; }}
        .logo-text h1 {{ font-size:20px; color:white; margin-bottom:2px; }}
        .logo-text p {{ font-size:11px; color:#d4a843; letter-spacing:2px; }}
        .nav {{ display:flex; gap:30px; list-style:none; }}
        .nav a {{ color:rgba(255,255,255,0.8); text-decoration:none; font-size:14px; transition:color 0.3s; }}
        .nav a:hover {{ color:#d4a843; }}
        .page-hero {{ background:linear-gradient(135deg,#1a2332,#2c5282); padding:180px 20px 100px; text-align:center; color:white; }}
        .page-hero h2 {{ font-size:48px; margin-bottom:20px; }}
        .page-hero p {{ font-size:18px; opacity:0.9; max-width:800px; margin:0 auto; }}
        .page-content {{ max-width:1200px; margin:0 auto; padding:100px 20px; }}
        .page-content h3 {{ font-size:28px; color:#1a2332; margin-bottom:20px; }}
        .page-content p {{ font-size:15px; color:#718096; line-height:1.8; margin-bottom:20px; }}
        .page-content .features {{ display:grid; grid-template-columns:repeat(3,1fr); gap:30px; margin:40px 0; }}
        .feature-card {{ background:white; padding:30px; border-radius:16px; box-shadow:0 5px 20px rgba(0,0,0,0.1); }}
        .feature-card h4 {{ font-size:18px; color:#1a2332; margin-bottom:10px; }}
        .feature-card p {{ font-size:14px; color:#718096; }}
        .cta-section {{ background:linear-gradient(135deg,#1a2332,#2c5282); padding:80px 20px; text-align:center; color:white; }}
        .cta-section h2 {{ font-size:36px; margin-bottom:20px; }}
        .cta-section p {{ font-size:16px; opacity:0.9; margin-bottom:30px; }}
        .cta-btn {{ display:inline-block; background:#d4a843; color:#1a2332; padding:15px 40px; border-radius:30px; text-decoration:none; font-weight:bold; font-size:16px; transition:all 0.3s; }}
        .cta-btn:hover {{ transform:translateY(-3px); box-shadow:0 10px 40px rgba(212,168,67,0.6); }}
        .footer {{ background:#0d1117; color:rgba(255,255,255,0.8); padding:60px 20px 30px; }}
        .footer-inner {{ max-width:1200px; margin:0 auto; }}
        .footer-grid {{ display:grid; grid-template-columns:2fr 1fr 1fr 1fr; gap:40px; margin-bottom:40px; }}
        .footer h3 {{ font-size:20px; color:white; margin-bottom:15px; }}
        .footer p {{ font-size:14px; line-height:1.8; opacity:0.7; }}
        .footer-links {{ list-style:none; }}
        .footer-links li {{ margin-bottom:10px; }}
        .footer-links a {{ color:rgba(255,255,255,0.7); text-decoration:none; font-size:14px; }}
        .footer-links a:hover {{ color:#d4a843; }}
        .footer-bottom {{ border-top:1px solid rgba(255,255,255,0.1); padding-top:20px; text-align:center; font-size:13px; opacity:0.5; }}
        @media (max-width:768px) {{
            .nav {{ display:none; }}
            .page-hero h2 {{ font-size:32px; }}
            .page-content .features {{ grid-template-columns:1fr; }}
            .footer-grid {{ grid-template-columns:1fr; }}
        }}
    </style>
</head>
<body>
    <header class="header">
        <div class="header-inner">
            <a href="index.html" class="logo">
                <div class="logo-icon">筑</div>
                <div class="logo-text">
                    <h1>湖南筑邦</h1>
                    <p>建筑资质代办专家</p>
                </div>
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
        <p>{content}</p>
        <div class="features">
            <div class="feature-card">
                <h4>⚡ 效率高</h4>
                <p>1对1专人全程跟进，让资质办理省时省心</p>
            </div>
            <div class="feature-card">
                <h4>🎓 专业强</h4>
                <p>建筑行业服务领域深耕十余年，精准把握政策法规</p>
            </div>
            <div class="feature-card">
                <h4>💰 价格优</h4>
                <p>报价内容公开透明，提供严谨、灵活、全面的解决方案</p>
            </div>
        </div>
        <p>湖南筑邦企业管理咨询有限公司，品牌创立于2018年，是一家专注于建筑资质代办服务的专业机构。公司秉承"专业的事交给专业的人"的服务理念，致力于为建筑企业提供高效、合规、零风险的资质解决方案。</p>
        <p>作为湖南本土建筑资质代办领导品牌，公司服务范围覆盖全省，已在长沙（总部）、永州、衡阳、岳阳、娄底、邵阳、怀化等地设立分公司。</p>
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
                    <p>专为建筑业企业提供资质服务的一站式服务公司，秉承"客户主导服务、标准主导市场"的理念。</p>
                </div>
                <div>
                    <h3>快速链接</h3>
                    <ul class="footer-links">
                        <li><a href="index.html">首页</a></li>
                        <li><a href="about-intro.html">公司简介</a></li>
                        <li><a href="about-process.html">服务流程</a></li>
                        <li><a href="know-changjianwenti.html">常见问题</a></li>
                    </ul>
                </div>
                <div>
                    <h3>服务项目</h3>
                    <ul class="footer-links">
                        <li><a href="zizhi-zongchengbao.html">总承包资质</a></li>
                        <li><a href="zizhi-zhuanyechengbao.html">专业承包资质</a></li>
                        <li><a href="zizhi-laowufenbao.html">劳务分包资质</a></li>
                        <li><a href="zizhi-jiaoyi.html">资质交易服务</a></li>
                    </ul>
                </div>
                <div>
                    <h3>联系我们</h3>
                    <ul class="footer-links">
                        <li>📞 157-7411-6703</li>
                        <li>📍 长沙市开福区福元西路96号</li>
                        <li>🕐 周一至周日 8:00-22:00</li>
                    </ul>
                </div>
            </div>
            <div class="footer-bottom">
                <p>© 2026 湖南筑邦企业管理咨询有限公司 版权所有</p>
            </div>
        </div>
    </footer>
</body>
</html>'''

def generate_page(page_config, output_dir):
    """生成单个子页面"""
    extra_keywords = page_config.get("extra_keywords", "资质代办")
    html = TEMPLATE.format(
        title=page_config["title"],
        desc=page_config["desc"],
        h1=page_config["h1"],
        content=page_config["content"],
        extra_keywords=extra_keywords
    )
    
    filepath = os.path.join(output_dir, page_config["file"])
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(html)
    return filepath

def main():
    output_dir = os.path.dirname(os.path.abspath(__file__))
    
    print(f"开始生成 {len(PAGES)} 个子页面...")
    print(f"输出目录: {output_dir}")
    print("-" * 50)
    
    generated = []
    for i, page in enumerate(PAGES, 1):
        try:
            filepath = generate_page(page, output_dir)
            generated.append(page["file"])
            print(f"[{i}/{len(PAGES)}] ✅ {page['file']} - {page['h1']}")
        except Exception as e:
            print(f"[{i}/{len(PAGES)}] ❌ {page['file']} - 错误: {e}")
    
    print("-" * 50)
    print(f"生成完成！共 {len(generated)}/{len(PAGES)} 个页面")
    print("\n生成的文件：")
    for f in generated:
        print(f"  - {f}")

if __name__ == "__main__":
    main()
