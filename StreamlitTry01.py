import os

os.environ["ZHIPUAI_API_KEY"] = "53ca6a88a682be774f7c07ad856b5d42.5Hczmqc5Cz3d4WBM"

os.environ["IFLYTEK_SPARK_APP_ID"] = "1a2c0e22"
os.environ["IFLYTEK_SPARK_API_KEY"] = "91ac602cffda5c10bbb78fc314f8525d"
os.environ["IFLYTEK_SPARK_API_SECRET"] = "ODYyMWEzMDViNGVjMWZjYWQyMmE5YWJi" # 这个key来自老师
# 此处参考：https://www.xfyun.cn/doc/spark/Web.html
os.environ["IFLYTEK_SPARK_API_URL"] = "wss://spark-api.xf-yun.com/v3.1/chat"
os.environ["IFLYTEK_SPARK_llm_DOMAIN"] = "generalv3"

from langchain_community.chat_models import ChatZhipuAI
zhipuai_model = ChatZhipuAI(
    model="glm-4",
    # temperature=0.9,
)
from langchain_community.chat_models import ChatSparkLLM
spark_chat_model = ChatSparkLLM()

MyModel = spark_chat_model

import streamlit as st
text = st.text_area(label='输入问题，最大200字，ctrl+enter发送。'
                          '(此问答以大语言模型api为基础,通过LangChain构建对话,streamlit搭建web界面)',
                    value='你好......',
                    height=5,
                    max_chars=200,
                    help='最大长度限制为200')

st.write("正在思考：", text)

response = MyModel.invoke(text)

st.write('回答：', response.content)
