import dotenv
from langchain_core.prompts import ChatPromptTemplate
from langchain_qwq import ChatQwen,ChatQwQ
from langchain_core.output_parsers import StrOutputParser

dotenv.load_dotenv()

#1.构建组件
prompt = ChatPromptTemplate.from_template("{query}")
llm = ChatQwen(
    model="qwen-plus",
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1"  # 国际站
)
parser = StrOutputParser()

#2.创建链
chain = prompt | llm | parser

#3.调用链得到结果
print(chain.invoke({"query": "请讲一个程序员的冷笑话"}))