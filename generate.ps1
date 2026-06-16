$Products = @(
    @{ id = 1; name = 'AeroCloud 雲端慢跑鞋'; price = '3,280'; cat = 'casual'; img = 'running,shoe'; desc = '極致輕量，宛如漫步雲端。採用最新發泡科技中底，提供完美避震與回彈。' },
    @{ id = 2; name = 'StreetPulse 潮流街舞鞋'; price = '2,850'; cat = 'casual'; img = 'sneaker'; desc = '專為街頭文化設計。耐磨橡膠大底與高筒包覆，展現個人風格的同時提供絕佳保護。' },
    @{ id = 3; name = 'Orbit 高筒籃球鞋'; price = '4,200'; cat = 'casual'; img = 'basketball,shoe'; desc = '為爆發力而生。碳纖維抗扭轉片與前腳掌氣墊，讓您在球場上無往不利。' },
    @{ id = 16; name = 'Ace 輕便網球鞋'; price = '2,900'; cat = 'casual'; img = 'tennis,shoe'; desc = '提供優異的側向支撐與抓地力，幫助您在球場上靈活移動。' },
    @{ id = 4; name = 'Classic 尊爵牛津鞋'; price = '5,600'; cat = 'formal'; img = 'oxford,shoe'; desc = '頂級小牛皮手工縫製。經典優雅的設計，是商務人士不可或缺的專業配備。' },
    @{ id = 5; name = 'Elegance 典雅高跟鞋'; price = '3,980'; cat = 'formal'; img = 'highheels'; desc = '完美修飾腿部線條。內建隱形足弓支撐墊，讓您優雅一整天也不覺疲累。' },
    @{ id = 6; name = 'Executive 舒適樂福鞋'; price = '4,500'; cat = 'formal'; img = 'loafer'; desc = '免綁帶設計，穿脫方便。適合半正式場合與日常辦公，展現從容自信。' },
    @{ id = 7; name = 'Titan 鈦金屬重裝登山鞋'; price = '4,850'; cat = 'outdoor'; img = 'hiking,boot'; desc = '全天候防水透氣。配備黃金大底與防撞鞋頭，征服各種崎嶇地形。' },
    @{ id = 8; name = 'Summit 輕量越野鞋'; price = '3,600'; cat = 'outdoor'; img = 'trail,shoe'; desc = '專為越野跑者設計。超強抓地力刻痕與防泥沙網布，讓您盡情奔跑。' },
    @{ id = 9; name = 'AquaShield 極致防水靴'; price = '2,500'; cat = 'outdoor'; img = 'rain,boot'; desc = '100% 絕對防水。時尚的外型設計，讓您在雨天依然保持優雅乾爽。' },
    @{ id = 10; name = 'Breeze 舒適氣墊涼鞋'; price = '1,280'; cat = 'home'; img = 'sandal'; desc = '獨家氣墊設計，減輕足部壓力。抗菌防臭材質，給您最舒適的夏日體驗。' },
    @{ id = 11; name = 'Cozy 記憶棉居家拖鞋'; price = '850'; cat = 'home'; img = 'slipper'; desc = '高密度記憶棉內墊，完美貼合腳型。讓疲憊一天的雙腳獲得真正的放鬆。' },
    @{ id = 12; name = 'Flex 強韌彈力鞋帶'; price = '250'; cat = 'accessories'; img = 'shoelace'; desc = '高強度編織工藝，不易鬆脫斷裂。多種顏色選擇，隨心搭配您的愛鞋。' },
    @{ id = 13; name = 'CloudSupport 減壓足弓鞋墊'; price = '680'; cat = 'accessories'; img = 'insole'; desc = '人體工學設計，有效分散足底壓力。適合長時間站立或行走的人士。' },
    @{ id = 14; name = 'GripPro 隱形防滑貼'; price = '150'; cat = 'accessories'; img = 'grip,sole'; desc = '超強黏性，防止鞋底打滑。延長愛鞋壽命，保護您的行走安全。' },
    @{ id = 15; name = 'Active 抗菌運動襪'; price = '350'; cat = 'accessories'; img = 'socks'; desc = '吸濕排汗，長效抗菌。加厚毛巾底設計，提供額外的緩衝保護。' }
)

$Categories = @{
    'casual' = @{ title = '休閒運動'; file = 'casual.html' }
    'formal' = @{ title = '正式商務'; file = 'formal.html' }
    'outdoor' = @{ title = '機能戶外'; file = 'outdoor.html' }
    'home' = @{ title = '居家輕便'; file = 'home.html' }
    'accessories' = @{ title = '配件類'; file = 'accessories.html' }
}

$NavHtml = @"
    <header>
        <div class="nav-container">
            <a href="index.html" class="logo">Aero<span>Step</span></a>
            <nav class="nav-links">
                <a href="index.html">首頁</a>
                <a href="about.html">公司簡介</a>
                <a href="casual.html">休閒運動</a>
                <a href="formal.html">正式商務</a>
                <a href="outdoor.html">機能戶外</a>
                <a href="home.html">居家輕便</a>
                <a href="accessories.html">配件類</a>
                <a href="contact.html">聯絡我們</a>
            </nav>
        </div>
    </header>
"@

$FooterHtml = @"
    <footer>
        <div class="footer-content">
            <div class="footer-col">
                <a href="index.html" class="logo" style="margin-bottom: 1rem; display: block;">Aero<span>Step</span></a>
                <p>專業鞋款製造商，致力於提供最優質的足部體驗。結合創新科技與傳統工藝，為您的每一步帶來極致舒適。</p>
            </div>
            <div class="footer-col">
                <h3>快速連結</h3>
                <ul>
                    <li><a href="about.html">關於我們</a></li>
                    <li><a href="contact.html">聯絡客服</a></li>
                    <li><a href="#">退換貨政策</a></li>
                    <li><a href="#">隱私權聲明</a></li>
                </ul>
            </div>
            <div class="footer-col">
                <h3>聯絡資訊</h3>
                <p>📍 台北市信義區信義路五段7號</p>
                <p>📞 (02) 2345-6789</p>
                <p>✉️ support@aerostep.com.tw</p>
                <p>🕒 營業時間: 週一至週五 09:00-18:00</p>
            </div>
        </div>
        <div class="footer-bottom">
            &copy; 2026 AeroStep. All rights reserved.
        </div>
    </footer>
    <script src="js/main.js"></script>
</body>
</html>
"@

function Get-Header {
    param([string]$Title)
    return @"
<!DOCTYPE html>
<html lang="zh-TW">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>$Title | AeroStep</title>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;700;800&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="css/style.css">
</head>
<body>
$NavHtml
"@
}

# Generate Category Pages
foreach ($CatKey in $Categories.Keys) {
    $CatInfo = $Categories[$CatKey]
    $CatTitle = $CatInfo.title
    $Html = Get-Header -Title $CatTitle
    $Html += @"
    <main>
        <div class="container animate-fade-in">
            <h1 class="section-title">$CatTitle</h1>
            <div class="product-grid">
"@
    foreach ($P in $Products) {
        if ($P.cat -eq $CatKey) {
            $Img = $P.img
            $Pid = $P.id
            $Pname = $P.name
            $Pprice = $P.price
            $Html += @"
                <a href="product-${Pid}.html" class="product-card">
                    <img src="https://loremflickr.com/800/600/$Img" alt="$Pname" class="product-img">
                    <div class="product-info">
                        <span class="product-category">$CatTitle</span>
                        <h3 class="product-title">$Pname</h3>
                        <div class="product-price">
                            NT$ $Pprice <span class="view-details">查看詳情 →</span>
                        </div>
                    </div>
                </a>
"@
        }
    }
    $Html += @"
            </div>
        </div>
    </main>
$FooterHtml
"@
    Set-Content -Path $CatInfo.file -Value $Html -Encoding UTF8
}

# Generate Product Detail Pages
foreach ($P in $Products) {
    $CatKey = $P.cat
    $CatTitle = $Categories[$CatKey].title
    $Img = $P.img
    $Pid = $P.id
    $Pname = $P.name
    $Pprice = $P.price
    $Pdesc = $P.desc
    
    $Html = Get-Header -Title $Pname
    $Html += @"
    <main>
        <div class="container animate-fade-in">
            <div class="product-detail-container">
                <div class="product-gallery">
                    <img src="https://loremflickr.com/800/600/$Img" alt="$Pname">
                </div>
                <div class="product-details">
                    <span class="product-category">$CatTitle</span>
                    <h1>$Pname</h1>
                    <div class="price">NT$ $Pprice</div>
                    <p>$Pdesc</p>
                    
                    <ul class="features-list">
                        <li>高品質透氣材質</li>
                        <li>人體工學舒適設計</li>
                        <li>耐磨防滑大底</li>
                        <li>原廠一年保固</li>
                    </ul>
"@
    
    if ($CatKey -ne 'accessories') {
        $Html += @"
                    <div class="size-selector">
                        <h3>選擇尺寸 (US)</h3>
                        <div class="sizes">
                            <button class="size-btn selected">8</button>
                            <button class="size-btn">8.5</button>
                            <button class="size-btn">9</button>
                            <button class="size-btn">9.5</button>
                            <button class="size-btn">10</button>
                            <button class="size-btn">10.5</button>
                            <button class="size-btn">11</button>
                        </div>
                    </div>
"@
    }

    $Html += @"
                    <button class="btn add-to-cart">加入購物車</button>
                </div>
            </div>
        </div>
    </main>
$FooterHtml
"@
    Set-Content -Path "product-${Pid}.html" -Value $Html -Encoding UTF8
}

# Generate Contact Page
$ContactHtml = Get-Header -Title '聯絡我們'
$ContactHtml += @"
    <main>
        <div class="container animate-fade-in">
            <h1 class="section-title">聯絡我們</h1>
            <div class="product-detail-container" style="gap: 4rem;">
                <div>
                    <h2>我們很樂意聽取您的意見！</h2>
                    <p style="color: var(--text-secondary); margin: 1.5rem 0; line-height: 1.8;">
                        無論您對我們的產品有任何疑問，或是需要售後服務，我們的客服團隊隨時為您準備好。請填寫右側表單，我們會在 24 小時內回覆您。
                    </p>
                    <div style="margin-top: 2rem;">
                        <p style="margin-bottom: 1rem;"><strong>📍 總部地址:</strong> 台北市信義區信義路五段7號</p>
                        <p style="margin-bottom: 1rem;"><strong>📞 客服專線:</strong> (02) 2345-6789</p>
                        <p style="margin-bottom: 1rem;"><strong>✉️ 電子郵件:</strong> support@aerostep.com.tw</p>
                        <p style="margin-bottom: 1rem;"><strong>🕒 營業時間:</strong> 週一至週五 09:00-18:00</p>
                    </div>
                </div>
                <div>
                    <form onsubmit="event.preventDefault(); alert('感謝您的來信！我們已收到您的訊息，會盡快與您聯絡。'); this.reset();">
                        <div class="form-group">
                            <label for="name">姓名</label>
                            <input type="text" id="name" required placeholder="請輸入您的姓名">
                        </div>
                        <div class="form-group">
                            <label for="email">電子郵件</label>
                            <input type="email" id="email" required placeholder="example@email.com">
                        </div>
                        <div class="form-group">
                            <label for="subject">主旨</label>
                            <input type="text" id="subject" required placeholder="請輸入主旨">
                        </div>
                        <div class="form-group">
                            <label for="message">訊息內容</label>
                            <textarea id="message" rows="6" required placeholder="請詳細描述您的問題或建議..."></textarea>
                        </div>
                        <button type="submit" class="btn" style="width: 100%;">送出訊息</button>
                    </form>
                </div>
            </div>
        </div>
    </main>
$FooterHtml
"@
Set-Content -Path "contact.html" -Value $ContactHtml -Encoding UTF8

Write-Host "All HTML files generated successfully."
