# -*- coding: utf-8 -*-
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
    { "id": 16, "name": "頂級鞋履保養清潔組", "cat": "accessories", "price": "1,500", "img": "assets/images/accessories_care_kit_1781568748448.png", "desc": "延長愛鞋壽命，隨時保持最佳狀態。" },
    { "id": 17, "name": "重裝防護鋼頭鞋", "cat": "work", "price": "4,200", "img": "assets/images/work_steel_toe.png", "desc": "高強度鋼頭防護，防刺穿大底，保障高風險環境下的足部安全。" },
    { "id": 18, "name": "防滑專業廚師鞋", "cat": "work", "price": "1,800", "img": "assets/images/work_chef_shoe.png", "desc": "防水橡膠一體成型，強效防滑底紋，無後跟帶設計方便快速穿脫。" },
    { "id": 19, "name": "醫療舒適護士鞋", "cat": "work", "price": "2,200", "img": "assets/images/work_nurse_shoe.png", "desc": "純白潔淨，極致輕量化，方便穿脫與清潔，醫療護理人員首選。" },
    { "id": 20, "name": "極致緩震久站鞋", "cat": "work", "price": "3,600", "img": "assets/images/work_standing_shoe.png", "desc": "空姐制服專屬款式，正式粗跟包鞋外觀，內置隱形氣墊與加厚紓壓結構，長時間站立不疲勞。" }
]

categories = {
    "casual": { "title": "休閒運動", "file": "casual.html" },
    "formal": { "title": "正式商務", "file": "formal.html" },
    "outdoor": { "title": "機能戶外", "file": "outdoor.html" },
    "work": { "title": "工作用鞋", "file": "work.html" },
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
                <a href="philosophy.html">品牌理念</a>
                <a href="about.html">公司簡介</a>
                <a href="casual.html">休閒運動</a>
                <a href="formal.html">正式商務</a>
                <a href="outdoor.html">機能戶外</a>
                <a href="work.html">工作用鞋</a>
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


# Generate Philosophy Page
philosophy_content = """
        <!-- ================= 新增的品牌介紹區塊開始 ================= -->
        
        <!-- 品牌簡介 / 關於我們 (白底) -->
        <section style="padding: 80px 20px; background-color: #ffffff;">
            <div style="max-width: 1000px; margin: 0 auto; text-align: center;">
                <h2 style="font-size: 2rem; color: #1a1a1a; margin-top: 0; margin-bottom: 20px; letter-spacing: 1px;">遇見 SoleMate，遇見你的命定之鞋</h2>
                <div style="width: 50px; height: 3px; background-color: #1a1a1a; margin: 0 auto 40px;"></div>
                
                <p style="font-size: 1.1rem; color: #555; line-height: 1.8; text-align: justify; margin-bottom: 20px;">
                    我們始終相信，一雙好鞋不只是日常的穿搭配件，更是支撐你探索世界的「靈魂伴侶（Soulmate）」。在 SoleMate，我們致力於打破「美麗與舒適無法兼具」的迷思。我們深知現代人常受足部問題困擾，因此作為專業的【拇指外翻 鞋子 專賣店】，我們的團隊走訪各地，尋找最頂級的皮革與創新材質，並結合符合亞洲人腳型的【寬楦 運動 鞋】精準設計，為您打造出無可挑惕的頂級鞋履。我們更貼心研發了【足底筋膜炎 專用鞋款】，讓正在尋找舒緩【腳底筋膜炎 鞋子】的您，能重新找回步行的純粹愉悅。
                </p>
                <p style="font-size: 1.1rem; color: #555; line-height: 1.8; text-align: justify; margin-bottom: 0;">
                    無論是穿梭於職場的自信步伐、週末漫步的愜意時光，或是尋覓高質感【大尺碼 男鞋】的品味人士，SoleMate 都將以最高規格的包覆與支撐，溫柔承接您的每一次起步與駐足。若您熱愛戶外探索與日常漫步，我們的【溯溪 鞋 推薦】系列與【走路 鞋 推薦】指南，定能滿足您的全方位需求。
                </p>
            </div>
        </section>

        <!-- 品牌核心價值 卡片設計 (淺灰底，延續您商品的卡片風格) -->
        <section style="padding: 80px 20px; background-color: #f8f9fa;">
            <div style="max-width: 1200px; margin: 0 auto;">
                <h2 style="font-size: 2rem; color: #1a1a1a; text-align: center; margin-top: 0; margin-bottom: 15px;">品牌核心價值</h2>
                <p style="text-align: center; color: #7f8c8d; margin-bottom: 50px; font-size: 1.1rem;">為了呈現真正的「頂級」，我們在三個層面做到極致：</p>
                
                <div style="display: flex; flex-wrap: wrap; gap: 30px; justify-content: center;">
                    <!-- 卡片 1 -->
                    <div style="flex: 1 1 300px; background: #ffffff; padding: 40px 30px; border-radius: 12px; box-shadow: 0 4px 20px rgba(0,0,0,0.04);">
                        <h3 style="font-size: 1.3rem; color: #2c3e50; margin-top: 0; margin-bottom: 20px; border-bottom: 1px solid #eee; padding-bottom: 15px;">◆ 頂級匠心工藝</h3>
                        <p style="color: #666; line-height: 1.7; text-align: justify; margin: 0; font-size: 1.05rem;">拒絕大量製造的粗糙，我們堅持採用高規格的製鞋工法。從皮料的篩選、裁切到縫製，每一道工序都傾注了職人對品質的無聲承諾。不只是時尚鞋款，就連需要高度防護的【鋼頭 鞋 推薦】首選與重工業適用的【鋼頭 安全 鞋】，都能經得起時間與極端環境的嚴苛考驗。</p>
                    </div>
                    <!-- 卡片 2 -->
                    <div style="flex: 1 1 300px; background: #ffffff; padding: 40px 30px; border-radius: 12px; box-shadow: 0 4px 20px rgba(0,0,0,0.04);">
                        <h3 style="font-size: 1.3rem; color: #2c3e50; margin-top: 0; margin-bottom: 20px; border-bottom: 1px solid #eee; padding-bottom: 15px;">◆ 為雙足而生的極致舒適</h3>
                        <p style="color: #666; line-height: 1.7; text-align: justify; margin: 0; font-size: 1.05rem;">完美契合，是我們的定義。我們深知許多職業的需求，特別打造了【適合 久站 鞋子】的機能系列；無論是需要【防滑 工作 鞋】的廚師、尋覓【餐飲業 久站 鞋子】的服務人員、需要【護士 鞋 推薦】的醫護人員，還是各行各業尋求【工作 鞋 推薦】的職人，讓您即使久站，依然能感受如履雲端般的輕盈。熱愛運動的您，也能找到高包覆性的【無鞋帶 運動 鞋】及【慢跑 鞋 推薦 男】與【慢跑 鞋 推薦 女】專業跑鞋。</p>
                    </div>
                    <!-- 卡片 3 -->
                    <div style="flex: 1 1 300px; background: #ffffff; padding: 40px 30px; border-radius: 12px; box-shadow: 0 4px 20px rgba(0,0,0,0.04);">
                        <h3 style="font-size: 1.3rem; color: #2c3e50; margin-top: 0; margin-bottom: 20px; border-bottom: 1px solid #eee; padding-bottom: 15px;">◆ 跨越時間的雋永設計</h3>
                        <p style="color: #666; line-height: 1.7; text-align: justify; margin: 0; font-size: 1.05rem;">真正的經典不會隨著季節褪色。我們捨棄盲目追逐短暫的流行，專注於俐落的剪裁與內斂的細節。無論是討論度極高的【樂福鞋 推薦 dcard】熱門款式、復古優雅的【瑪莉珍 鞋 穿搭】提案、修飾身形的【粗跟 高跟鞋】，或是引領街頭潮流的【老爹 鞋 推薦】精選，都能無縫融入您的衣櫥。除了成人款式，更推出了保護發育中雙腳的【兒童 籃球 鞋】，全面照顧全家人的足下時尚。</p>
                    </div>
                </div>
            </div>
        </section>

        <!-- 行動呼籲 Call to Action (深色底，呼應您的 Hero Section) -->
        <section style="padding: 100px 20px; background-color: #0f1115; color: #ffffff; text-align: center;">
            <div style="max-width: 800px; margin: 0 auto;">
                <h2 style="font-size: 2.2rem; margin-top: 0; margin-bottom: 20px; color: #ffffff;">準備好迎接您的專屬舒適了嗎？</h2>
                <p style="font-size: 1.1rem; line-height: 1.8; opacity: 0.9; margin-bottom: 40px;">不再為磨腳而妥協，不再為挑選而苦惱。<br>現在就開始探索 SoleMate 的精選系列，找到那雙懂你、挺你、完美契合你的專屬鞋履。<br>結帳前，也別忘了帶上我們獨家研發的【鞋子 防水 噴霧】，為您的愛鞋提供最完善的全天候防護。</p>
                <!-- 這裡的按鈕我有加上您原本 css 裡的 .btn class -->
                <a href="casual.html" class="btn" style="display: inline-block; background-color: #ffffff; color: #0f1115; padding: 15px 40px; border-radius: 30px; text-decoration: none; font-weight: bold; font-size: 1.1rem;">探索全系列鞋款</a>
            </div>
        </section>
        
        <!-- ================= 新增的品牌介紹區塊結束 ================= -->
"""
philosophy_html = get_header("品牌理念") + f"""
    <main class="animate-fade-in">{philosophy_content}
    </main>
""" + footer_html
write_file("philosophy.html", philosophy_html)

print("All HTML files regenerated successfully")

