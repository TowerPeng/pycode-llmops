from datetime import datetime

import dotenv
from langchain_core.prompts import ChatPromptTemplate
from langchain_qwq import ChatQwen,ChatQwQ

dotenv.load_dotenv()

#1.编排prompt
prompt = ChatPromptTemplate.from_messages([
    ("system", "你是qWen开发的聊天机器人，请回答用户的问题，现在的时间是{now}"),
    ("human", "{query}"),
]).partial(now = datetime.now())

#2.创建大语言模型
llm = ChatQwen(
    model="qwen-plus",
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1"  # 国际站
)

response = llm.stream(prompt.invoke({"query": "你能简单介绍一下LLM和LLMOPS吗？"}))

for chunk in response:
    print(chunk.content,flush= True,end="")