import dotenv
from click import prompt
from langchain_core.output_parsers import StrOutputParser
from langchain_qwq import ChatQwen
from langchain_core.prompts import ChatPromptTemplate

dotenv.load_dotenv()
#1.编排提示模版

prompt = ChatPromptTemplate.from_template("{query}")

#2.创建大语言模型
llm = ChatQwen(
    model="qwen-plus",
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1"  # 国际站
)
#3.创建字符串输出解析器
parser = StrOutputParser()

#4.调用大语言模型生成结果并解析
content = parser.invoke(llm.invoke(prompt.invoke({"query": "你好，你是？"})))
print(content)