from langchain_core.prompts import PromptTemplate, ChatPromptTemplate

system_chat_prompt = ChatPromptTemplate.from_messages( [
    ("system", "你是qWen开发的聊天机器人，请根据用户的提问进行回复,我叫{username}"),


])

human_chat_promt = ChatPromptTemplate.from_messages( [
    ("human", "{query}"),
])

chat_prompt = system_chat_prompt + human_chat_promt

print(chat_prompt.invoke({"username": "张三", "query": "你叫什么名字"}))