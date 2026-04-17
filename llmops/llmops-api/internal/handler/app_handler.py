#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time    : 2024/3/29 14:59
@Author  : thezehui@gmail.com
@File    : app_handler.py
"""
import os
import uuid
from dataclasses import dataclass

from click import prompt
from injector import inject
from openai import OpenAI
from flask import request

from langchain_core.prompts import ChatPromptTemplate
from langchain_qwq import ChatQwen
from langchain_core.output_parsers import JsonOutputParser, StrOutputParser
from internal.exception import FailException
from internal.schema.app_schema import CompletionReq
from internal.service import AppService
from pkg.response import success_json, validate_error_json, success_message

@inject
@dataclass
class AppHandler:
    """应用控制器"""
    app_service: AppService

    def create_app(self):
        """调用服务创建新的APP记录"""
        app = self.app_service.create_app()
        return success_message(f"应用已经成功创建，id为{app.id}")

    def get_app(self, id: uuid.UUID):
        app = self.app_service.get_app(id)
        return success_message(f"应用已经成功获取，名字是{app.name}")

    def update_app(self, id: uuid.UUID):
        app = self.app_service.update_app(id)
        return success_message(f"应用已经成功修改，修改的名字是:{app.name}")

    def delete_app(self, id: uuid.UUID):
        app = self.app_service.delete_app(id)
        return success_message(f"应用已经成功删除，id为:{app.id}")

    def completion(self):
        """聊天接口"""
        # 1.提取从接口中获取的输入，POST
        req = CompletionReq()
        if not req.validate():
            return validate_error_json(req.errors)
        # query = request.json.get("query");

        prompt = ChatPromptTemplate.from_template("{query}")

        # 2.构建llm客户端，并发起请求
        llm = ChatQwen(
            model="qwen-plus",
            base_url="https://dashscope.aliyuncs.com/compatible-mode/v1"  # 国际站
        )


        parser = StrOutputParser ()

        #3.构建链
        chain = prompt | llm | parser

        #4.调用链得到结果
        content = chain.invoke({"query": req.query.data})

        # content = parser.invoke(ai_message)

        # ai_message = llm.invoke(prompt.invoke({"query": req.query.data}))

        # # 2.构建OpenAI客户端，并发起请求
        # client = OpenAI(base_url=os.getenv("ALIAI_API_BASE"),
        #                 api_key=os.getenv("ALIAI_API_KEY"))
        #
        # # 3.得到请求响应，然后将OpenAI的响应传递给前端
        # completion = client.chat.completions.create(
        #     # 模型列表：https://help.aliyun.com/zh/model-studio/getting-started/models
        #     model="qwen-plus",
        #     messages=[
        #         {"role": "system", "content": "You are a helpful assistant."},
        #         {"role": "user", "content": req.query.data},
        #     ]
        # )
        #
        # content = completion.choices[0].message.content

        return success_json({"content": content})

    def ping(self):
        raise FailException("数据未找到")
        # return {"ping": "pong"}
