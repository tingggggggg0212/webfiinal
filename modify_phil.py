# -*- coding: utf-8 -*-
with open('generate.py', 'r', encoding='utf-8') as f:
    text = f.read()

import re

old_code_regex = r'# Generate Philosophy Page.*?write_file\("philosophy\.html", philosophy_html\)'

new_code = '''# Generate Philosophy Page
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
philosophy_html = get_header("品牌理念") + f"\\n    <main class=\\"animate-fade-in\\">{philosophy_content}\\n    </main>\\n" + footer_html
write_file("philosophy.html", philosophy_html)'''

text = re.sub(old_code_regex, new_code, text, flags=re.DOTALL)

with open('generate.py', 'w', encoding='utf-8') as f:
    f.write(text)
