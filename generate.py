import json
import os

products = [
    { "id": 1, "name": "高機能空氣動能慢跑鞋", "cat": "casual", "price": "3,200", "img": "assets/images/sports_running_shoes_1781568343864.png", "desc": "針對專業跑者設計，提供極致緩震與透氣包覆。" },
    { "id": 2, "name": "復刻高筒實戰籃球鞋", "cat": "casual", "price": "4,500", "img": "assets/images/sports_basketball_sneakers_1781568361156.png", "desc": "強化腳踝支撐，抓地力十足的頂級籃球鞋。" },
    { "id": 3, "name": "經典極簡百搭白球鞋", "cat": "casual", "price": "2,100", "img": "assets/images/sports_white_sneakers_1781568373221.png", "desc": "日常穿搭必備，舒適好穿。" },
    { "id": 4, "name": "英倫紳士手工牛津皮鞋", "cat": "formal", "price": "5,800", "img": "assets/images/formal_oxford_shoes_1781568460367.png", "desc": "嚴選頂級牛皮，展現不凡商務品味。" },
    { "id": 5, "name": "優雅漆皮尖頭高跟鞋", "cat": "formal", "price": "3,600", "img": "assets/images/formal_high_heels_1781568471439.png", "desc": "完美修飾腿型，經典黑色展現極致優雅。" },
    { "id": 6, "name": "質感麂皮休閒樂福鞋", "cat": "formal", "price": "3,200", "img": "assets/images/formal_loafers_1781568484380.png", "desc": "正式與休閒的完美平衡，舒適百搭。" },
    { "id": 7, "name": "Gore-Tex 防水重裝登山鞋", "cat": "outdoor", "price": "6,500", "img": "assets/images/outdoor_hiking_boots_1781568575463.png", "desc": "無懼惡劣氣候，全地形適應。" },
    { "id": 8, "name": "經典亮黃防水雨鞋", "cat": "outdoor", "price": "1,800", "img": "assets/images/outdoor_rain_boots_1781568586321.png", "desc": "雨季必備，時尚與實用兼具。" },
    { "id": 9, "name": "全地形越野跑鞋", "cat": "outdoor", "price": "4,200", "img": "assets/images/outdoor_trail_running_shoes_1781568598324.png", "desc": "強悍抓地力，征服各種崎嶇路面。" },
    { "id": 10, "name": "極致輕量舒適涼鞋", "cat": "home", "price": "1,200", "img": "assets/images/casual_slide_sandals_1781568664905.png", "desc": "厚底緩震設計，居家外出皆宜。" },
    { "id": 11, "name": "保暖毛絨室內拖鞋", "cat": "home", "price": "850", "img": "assets/images/casual_home_slippers_1781568676935.png", "desc": "柔軟舒適，寒冬中的居家良伴。" },
    { "id": 12, "name": "夏日繽紛海灘夾腳拖", "cat": "home", "price": "600", "img": "assets/images/casual_flip_flops_1781568693650.png", "desc": "輕巧耐穿，海灘度假首選。" },
    { "id": 13, "name": "專業加厚緩震運動襪", "cat": "accessories", "price": "450", "img": "assets/images/accessories_socks_1781568712906.png", "desc": "保護雙腳，提升運動表現。" },
    { "id": 14, "name": "人體工學記憶海綿鞋墊", "cat": "accessories", "price": "650", "img": "assets/images/accessories_insoles_1781568724190.png", "desc": "舒緩足部壓力，適合長時間行走。" },
    { "id": 15, "name": "炫彩高韌性鞋帶組", "cat": "accessories", "price": "200", "img": "assets/images/accessories_shoelaces_1781568734651.png", "desc": "為愛鞋換上新裝，展現個人特色。" },
    { "id": 16, "name": "頂級鞋履保養清潔組", "cat": "accessories", "price": "1,500", "img": "assets/images/accessories_care_kit_1781568748448.png", "desc": "延長愛鞋壽命，隨時保持最佳狀態。" }
]

categories = {
    "casual": { "title": "休閒運動", "file": "casual.html" },
    "formal": { "title": "正式商務", "file": "formal.html" },
    "outdoor": { "title": "機能戶外", "file": "outdoor.html" },
    "home": { "title": "居家輕便", "file": "home.html" },
    "accessories": { "title": "配件類", "file": "accessories.html" }
}

# Add Logo Image
nav_html = """
    <header>
        <div class="nav-container">
            <a href="index.html" class="logo">
                <img src="assets/images/logo_solemate_1781568329595.png" alt="Logo" style="height: 40px; margin-right: 10px;">
                Sole<span>Mate</span>
            </a>
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
"""

footer_html = """
    <footer>
        <div class="footer-content">
            <div class="footer-col">
                <a href="index.html" class="logo" style="margin-bottom: 1rem; display: flex; align-items: center;">
                    <img src="assets/images/logo_solemate_1781568329595.png" alt="Logo" style="height: 30px; margin-right: 10px;">
                    Sole<span>Mate</span>
                </a>
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
                <p>✉️ support@solemate.com.tw</p>
                <p>🕒 營業時間: 週一至週五 09:00-18:00</p>
            </div>
        </div>
        <div class="footer-bottom">
            &copy; 2026 SoleMate. All rights reserved.
        </div>
    </footer>
    <script src="js/main.js"></script>
</body>
</html>
"""

def get_header(title):
    return f"""<!DOCTYPE html>
<html lang="zh-TW">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} | SoleMate | 頂級鞋履</title>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;700;800&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="css/style.css">
</head>
<body>
{nav_html}"""

def write_file(filename, content):
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)

# Update index.html
index_html = get_header("SoleMate | 頂級鞋履") + f"""
    <main>
        <section class="hero animate-fade-in" style="background: linear-gradient(rgba(15, 17, 21, 0.7), rgba(15, 17, 21, 0.9)), url('{products[0]["img"]}') center/cover;">
            <div class="hero-content">
                <h1>踏出你的專業每一步</h1>
                <p>結合頂級工藝與現代設計，為您打造最完美的穿著體驗。無論是商務會議還是極限戶外，SoleMate 都是您最堅實的後盾。</p>
                <a href="casual.html" class="btn">探索系列</a>
            </div>
        </section>

        <div class="container">
            <h2 class="section-title">熱銷精選</h2>
            <div class="product-grid">
                <a href="product-1.html" class="product-card">
                    <img src="{products[0]["img"]}" alt="{products[0]["name"]}" class="product-img">
                    <div class="product-info">
                        <span class="product-category">休閒運動</span>
                        <h3 class="product-title">{products[0]["name"]}</h3>
                        <div class="product-price">
                            NT$ {products[0]["price"]} <span class="view-details">查看詳情 →</span>
                        </div>
                    </div>
                </a>
                <a href="product-4.html" class="product-card">
                    <img src="{products[3]["img"]}" alt="{products[3]["name"]}" class="product-img">
                    <div class="product-info">
                        <span class="product-category">正式商務</span>
                        <h3 class="product-title">{products[3]["name"]}</h3>
                        <div class="product-price">
                            NT$ {products[3]["price"]} <span class="view-details">查看詳情 →</span>
                        </div>
                    </div>
                </a>
                <a href="product-7.html" class="product-card">
                    <img src="{products[6]["img"]}" alt="{products[6]["name"]}" class="product-img">
                    <div class="product-info">
                        <span class="product-category">機能戶外</span>
                        <h3 class="product-title">{products[6]["name"]}</h3>
                        <div class="product-price">
                            NT$ {products[6]["price"]} <span class="view-details">查看詳情 →</span>
                        </div>
                    </div>
                </a>
                <a href="product-10.html" class="product-card">
                    <img src="{products[9]["img"]}" alt="{products[9]["name"]}" class="product-img">
                    <div class="product-info">
                        <span class="product-category">居家輕便</span>
                        <h3 class="product-title">{products[9]["name"]}</h3>
                        <div class="product-price">
                            NT$ {products[9]["price"]} <span class="view-details">查看詳情 →</span>
                        </div>
                    </div>
                </a>
            </div>
        </div>
    </main>
{footer_html}"""
write_file("index.html", index_html)

# Update about.html
about_html = get_header("公司簡介") + f"""
    <style>
        .about-section {{ display: grid; grid-template-columns: 1fr 1fr; gap: 4rem; align-items: center; margin-bottom: 5rem; }}
        .about-section:nth-child(even) {{ direction: rtl; }}
        .about-section:nth-child(even) > * {{ direction: ltr; }}
        .about-text h2 {{ font-size: 2.5rem; margin-bottom: 1.5rem; color: var(--accent-color); }}
        .about-text p {{ font-size: 1.1rem; color: var(--text-secondary); margin-bottom: 1.5rem; }}
        .about-img img {{ width: 100%; border-radius: 20px; box-shadow: 0 20px 40px rgba(0,0,0,0.3); }}
        @media (max-width: 768px) {{ .about-section {{ grid-template-columns: 1fr; gap: 2rem; }} .about-section:nth-child(even) {{ direction: ltr; }} }}
    </style>
    <main>
        <div class="container animate-fade-in">
            <h1 class="section-title">品牌故事</h1>
            
            <div class="about-section">
                <div class="about-text">
                    <h2>我們的起源</h2>
                    <p>SoleMate 創立於 2010 年，源自於對完美足部體驗的執著。我們的創辦人相信，一雙好鞋不僅能改變你的步伐，更能改變你面對世界的心態。</p>
                    <p>從最初的一間小工作室，到現在成為國際知名的專業鞋履品牌，我們始終堅持「舒適、耐用、美學」三大核心理念。</p>
                </div>
                <div class="about-img">
                    <img src="assets/images/about_origin.jpg" alt="Shoemaking process">
                </div>
            </div>

            <div class="about-section">
                <div class="about-text">
                    <h2>極致工藝與科技結合</h2>
                    <p>我們深知傳統製鞋工藝的價值，同時也不斷尋求科技創新的可能。SoleMate 的每一雙鞋，都經過超過 100 道工序的嚴格把關。</p>
                    <p>我們獨家研發的 AeroCushion™ 氣墊技術，能有效吸收高達 85% 的衝擊力，為您的雙足提供全天候的舒適支撐。</p>
                </div>
                <div class="about-img">
                    <img src="assets/images/about_tech.jpg" alt="Shoe technology">
                </div>
            </div>
            
            <div class="about-section">
                <div class="about-text">
                    <h2>永續發展承諾</h2>
                    <p>SoleMate 致力於保護地球環境。我們在生產過程中使用 60% 的回收材料，並承諾在 2030 年達到零碳排放的目標。</p>
                    <p>選擇我們，不僅是選擇一雙好鞋，更是選擇一個可持續的未來。</p>
                </div>
                <div class="about-img">
                    <img src="assets/images/about_eco.jpg" alt="Sustainability">
                </div>
            </div>
        </div>
    </main>
{footer_html}"""
write_file("about.html", about_html)


# Generate Category Pages
for cat_id, cat_info in categories.items():
    cat_title = cat_info["title"]
    html = get_header(cat_title) + f"""
    <main>
        <div class="container animate-fade-in">
            <h1 class="section-title">{cat_title}</h1>
            <div class="product-grid">
"""
    cat_products = [p for p in products if p["cat"] == cat_id]
    for p in cat_products:
        html += f"""
                <a href="product-{p['id']}.html" class="product-card">
                    <img src="{p['img']}" alt="{p['name']}" class="product-img">
                    <div class="product-info">
                        <span class="product-category">{cat_title}</span>
                        <h3 class="product-title">{p['name']}</h3>
                        <div class="product-price">
                            NT$ {p['price']} <span class="view-details">查看詳情 →</span>
                        </div>
                    </div>
                </a>
"""
    html += f"""
            </div>
        </div>
    </main>
{footer_html}"""
    write_file(cat_info["file"], html)

# Generate Product Detail Pages
for p in products:
    cat_title = categories[p["cat"]]["title"]
    html = get_header(p["name"]) + f"""
    <main>
        <div class="container animate-fade-in">
            <div class="product-detail-container">
                <div class="product-gallery">
                    <img src="{p['img']}" alt="{p['name']}">
                </div>
                <div class="product-details">
                    <span class="product-category">{cat_title}</span>
                    <h1>{p['name']}</h1>
                    <div class="price">NT$ {p['price']}</div>
                    <p>{p['desc']}</p>
                    
                    <ul class="features-list">
                        <li>高品質透氣材質</li>
                        <li>人體工學舒適設計</li>
                        <li>耐磨防滑大底</li>
                        <li>原廠一年保固</li>
                    </ul>
"""
    if p["cat"] != "accessories":
        html += """
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
"""
    html += f"""
                    <button class="btn add-to-cart">加入購物車</button>
                </div>
            </div>
        </div>
    </main>
{footer_html}"""
    write_file(f"product-{p['id']}.html", html)

contact_html = get_header("聯絡我們") + f"""
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
                        <p style="margin-bottom: 1rem;"><strong>✉️ 電子郵件:</strong> support@solemate.com.tw</p>
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
{footer_html}"""
write_file("contact.html", contact_html)

print("All HTML files regenerated successfully with EXACT product data and images.")
