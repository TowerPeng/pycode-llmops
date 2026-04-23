from itertools import chain

import dotenv
from langchain_core.prompts import ChatPromptTemplate
from langchain_qwq import ChatQwen,ChatQwQ
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough


dotenv.load_dotenv()

def retrieval(query:str)->str:
    """一个模拟的检索器函数"""
    print("正在检索：",query)
    return "我是towerpeng"
#1.编排prompt
prompt = ChatPromptTemplate.from_template("""请根据用户的问题回答，可以参考对应的上下文进行生成
<context>
{context}
</context>

用户提问是：{query}""")

#2.构建大语言模型
llm = ChatQwen(
    model="qwen-plus",
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1"  # 国际站
)

#3.输出解析器
parser = StrOutputParser()


#4.构建链
# chain  = {
#     "context":retrieval,
#     "query": RunnablePassthrough(),
# } | prompt | llm | parser

#加数据
chain = RunnablePassthrough.assign(context=lambda x:retrieval(x["query"])) | prompt | llm | parser


#5.调用链
content = chain.invoke({"query":"你好，我是谁?"})

print(content)
