import os
os.environ["ZHIPUAI_API_KEY"] = "53ca6a88a682be774f7c07ad856b5d42.5Hczmqc5Cz3d4WBM"
from langchain_community.chat_models import ChatZhipuAI
zhipuai_model = ChatZhipuAI(
    model="glm-4",
    # temperature=0.9,
)
MyModel = zhipuai_model

import streamlit as st
text = st.text_area(label='输入问题，最大200字，ctrl+enter发送。'
                          '(此问答以智谱api为基础,通过LangChain构建对话,streamlit搭建web界面)',
                    value='你好......',
                    height=5,
                    max_chars=200,
                    help='最大长度限制为200')

st.write("正在思考：", text)

response = MyModel.invoke(text)

st.write('回答：', response.content)
