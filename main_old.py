from urllib.parse import DefragResult
import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import time

st.title('stramlit 超入門')

#st.write('DataFrame')
#st.write('Display Image')
st.write('プレグレスバーの表示')
'start!!'

latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f'Iteration{i+1}')
    bar.progress(i + 1)
    time.sleep(0.1)

'Done!!!!!'

left_column, right_column = st.beta_columns(2)
button = left_column.button('右カラムに文字を表示')
if button:
    right_column.write('ここは右カラム')

expander = st.beta_expander('問い合わせ1')
expander.write('問い合わせ1の回答内容')
expander = st.beta_expander('問い合わせ2')
expander.write('問い合わせ2の回答内容')
expander = st.beta_expander('問い合わせ3')
expander.write('問い合わせ3の回答内容')

#text = st.text_input('あなたの趣味を教えて下さい。')
#condition = st.slider('あなたの今の調子は？', 0, 100, 50)

#text = st.sidebar.text_input('あなたの趣味を教えて下さい。')
#st.sidebarでかんたんにサイドバーを作れる
#'あなたの趣味:', text 
#'コンディション:', condition

#option = st.selectbox(
#    'あなたが好きな数字を教えて下さい、',
#    list(range(1,11))
#)

#'あなたの好きな数字は、', option,'です。'

#if st.checkbox('Show Image'):
#    img = Image.open('image0.png')
#    st.image(img, caption='Haruka Ayase', use_column_width=True)

#df = pd.DataFrame(
#    np.random.rand(100,2)/[50,50] + [35.69, 139.70],
#    columns=['lat','lon']
#)
# write,dataframe,table streamlit reference gaids　API reference display dataに詳細
#st.table(df.style.highlight_max(axis=0))
# magic comand
#st.line_chart(df)#折れ線グラフ作成
#st.area_chart(df)#エリアチャート
#st.bar_chart(df)#棒グラフ
#API reference Display charts
#st.map(df)