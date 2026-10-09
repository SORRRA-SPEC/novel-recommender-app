import streamlit as st
from google import genai #Geminiの呼び出し。


# .\.venv\Scripts\activate 仮想環境の起動
# streamlitの起動　　python -m streamlit run app.py
st.caption("小説探しのパートナー")
st.title("📚AI小説ソムリエ")
 
st.write("今の気分や読書スタイルに合わせて、あなたにぴったりの一冊を提案します。")

mood = st.text_input("今の気分を教えてください！「泣きたい…」、「ハラハラしたい！」、「静かな雨の日に読みたい」など")

setting = st.radio("読みたいページ数", ["短編(~100p）", "中編（100~300p）", "長編（300p~）"])

genre = st.multiselect("好きなジャンルを選んでください（複数可）", ["ミステリー", "SF", "恋愛", "ホラー" , "ファンタジー", "その他"])
if "その他" in genre:
  user_genre = st.text_input("「その他」の読みたいジャンルを教えてください！")
  if user_genre:
    genre.append(user_genre)
    genre.remove("その他")


  

  
  


#streamlit　では、ボタンの設置と条件分岐は一行のコードで実現可能　
if st.button("おすすめを探す"):
  if not mood or not setting or not genre:
    st.write("先に今の気分、読みたい長さ、ジャンルを教えてね！")
  else:
     st.write("🔍 以下の条件でぴったりな小説を探します！")
     st.write(f"気分//{mood}")
     st.write(f"読みたいページ数//{setting}")
     st.write(f"ジャンル//{genre}")
     #こっからAI 呼ぶ処理
     client = genai.Client(api_key= st.secrets["GEMINI_API_KEY"])

     with st.spinner("AIソムリエがあなたにぴったりの本を選んでいます..."):
       prompt = f"""
あなたはプロの小説ソムリエです。
以下の条件にぴったりの小説を3冊提案してください。

・気分: {mood}
・読みたい長さ: {setting}
・希望ジャンル: {genre}

【出力形式】
作品名、著者名、おすすめ理由を分かりやすく紹介してください。
"""
    
       response = client.models.generate_content(
         model= "gemini-3.8-flash",
         contents= prompt
       )

       st.write(response.text)

  
