# -*- coding: utf-8 -*-
with open('generate.py', 'r', encoding='utf-8') as f:
    text = f.read()

# 1. Add products
old_products = '{ "id": 16, "name": "頂級鞋履保養清潔組", "cat": "accessories", "price": "1,500", "img": "assets/images/accessories_care_kit_1781568748448.png", "desc": "延長愛鞋壽命，隨時保持最佳狀態。" }'
new_products = old_products + ',\n    { "id": 17, "name": "重裝防護鋼頭鞋", "cat": "work", "price": "4,200", "img": "assets/images/work_steel_toe.png", "desc": "高強度鋼頭防護，防刺穿大底，保障高風險環境下的足部安全。" },\n    { "id": 18, "name": "防滑專業廚師鞋", "cat": "work", "price": "1,800", "img": "assets/images/work_chef_shoe.png", "desc": "防水橡膠一體成型，強效防滑底紋，無後跟帶設計方便快速穿脫。" },\n    { "id": 19, "name": "醫療舒適護士鞋", "cat": "work", "price": "2,200", "img": "assets/images/work_nurse_shoe.png", "desc": "純白潔淨，極致輕量化，方便穿脫與清潔，醫療護理人員首選。" },\n    { "id": 20, "name": "極致緩震久站鞋", "cat": "work", "price": "3,600", "img": "assets/images/work_standing_shoe.png", "desc": "空姐制服專屬款式，正式粗跟包鞋外觀，內置隱形氣墊與加厚紓壓結構，長時間站立不疲勞。" }'
text = text.replace(old_products, new_products)

# 2. Add category
old_cat = '"outdoor": { "title": "機能戶外", "file": "outdoor.html" },'
new_cat = old_cat + '\n    "work": { "title": "工作用鞋", "file": "work.html" },'
text = text.replace(old_cat, new_cat)

# 3. Add to nav
old_nav = '<a href="index.html">首頁</a>\n                <a href="about.html">公司簡介</a>'
new_nav = '<a href="index.html">首頁</a>\n                <a href="philosophy.html">品牌理念</a>\n                <a href="about.html">公司簡介</a>'
text = text.replace(old_nav, new_nav)

old_nav2 = '<a href="outdoor.html">機能戶外</a>'
new_nav2 = '<a href="outdoor.html">機能戶外</a>\n                <a href="work.html">工作用鞋</a>'
text = text.replace(old_nav2, new_nav2)

# 4. Add philosophy page generation at the end
philosophy_code = '''
# Generate Philosophy Page
philosophy_html = get_header("品牌理念") + f"""
    <main>
        <div class="container animate-fade-in" style="min-height: 50vh; display: flex; flex-direction: column; justify-content: center; align-items: center; text-align: center;">
            <h1 class="section-title">品牌理念</h1>
            <p style="color: var(--text-secondary); font-size: 1.2rem;">（內容建置中，敬請期待）</p>
        </div>
    </main>
{footer_html}"""
write_file("philosophy.html", philosophy_html)

print("All HTML files regenerated successfully")
'''
text = text.replace('print("All HTML files regenerated successfully with EXACT product data and images.")', philosophy_code)

with open('generate.py', 'w', encoding='utf-8') as f:
    f.write(text)
