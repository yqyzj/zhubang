# 批量更新HTML文件 - PowerShell版本
# 完成6项修改

$WORK_DIR = "c:\Users\yqyzj_skzq6hr\WorkBuddy\20260425142831"

# 新的电话号码
$NEW_PHONE = "15774116703"
$NEW_PHONE_DISPLAY = "157-7411-6703"

# 新的版权信息
$NEW_COPYRIGHT = "© 2018-2026 湖南筑邦企业管理咨询有限公司 永州分公司  美逸广告"

# 获取所有HTML文件
$htmlFiles = Get-ChildItem -Path $WORK_DIR -Filter "*.html" -File

Write-Host "找到 $($htmlFiles.Count) 个HTML文件"
Write-Host "开始批量更新..."
Write-Host ""

$updatedCount = 0

foreach ($file in $htmlFiles) {
    $filePath = $file.FullName
    $content = Get-Content -Path $filePath -Raw -Encoding UTF8
    $originalContent = $content
    $modified = $false

    # 1. 去掉邮箱
    if ($content -match 'mailto:' -or $content -match 'hunanzhubang' -or $content -match '📧') {
        $content = $content -replace '<a[^>]*mailto:[^>]*>[^<]*</a>', ''
        $content = $content -replace '📧\s*[^\s<]+@[^\s<]+', ''
        $content = $content -replace 'hunanzhubang@163\.com', ''
        $modified = $true
    }

    # 2. 电话号码统一
    if ($content -match '157-7491-8981') {
        $content = $content -replace '157-7491-8981', $NEW_PHONE_DISPLAY
        $modified = $true
    }
    if ($content -match '15774918981') {
        $content = $content -replace '15774918981', $NEW_PHONE
        $modified = $true
    }
    if ($content -match 'tel:15774918981') {
        $content = $content -replace 'tel:15774918981', "tel:$NEW_PHONE"
        $modified = $true
    }

    # 4. 修改版权信息
    if ($content -match '版权所有') {
        $content = $content -replace '©\s*\d{4}\s*湖南筑邦企业管理咨询有限公司\s*版权所有', $NEW_COPYRIGHT
        $content = $content -replace '©\s*\d{4}-\d{4}\s*湖南筑邦企业管理咨询有限公司\s*版权所有', $NEW_COPYRIGHT
        $modified = $true
    }

    # 5. 统一导航栏（子页面）
    if ($file.Name -ne "index.html") {
        # 替换 nav 为 main-nav
        if ($content -match 'class="nav"') {
            $content = $content -replace 'class="nav"', 'class="main-nav"'
            $modified = $true
        }
    }

    # 保存修改
    if ($modified) {
        Set-Content -Path $filePath -Value $content -Encoding UTF8
        $updatedCount++
        Write-Host "✓ 已更新: $($file.Name)"
    }
}

Write-Host ""
Write-Host "完成！共更新 $updatedCount 个文件"
