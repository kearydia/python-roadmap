# Python Roadmap

我的 AI 应用开发学习记录。

目标：2028 秋招拿到 AI Agent 开发岗。

学习路线：
Python 基础
JSON / 异常处理
HTTP / API
FastAPI
数据库
LLM API
RAG
Agent

记录规则：每天学习结束，提交一次。

# FastAPI Day01

学习内容：

- FastAPI基础
- 创建POST接口
- Uvicorn启动服务
- Swagger测试接口

接口：

POST /chat

返回：

{
 "answer":"你的问题已经收到"
}
# FastAPI Chat Interface Demo

## 项目介绍

这是我的第一个AI应用后端接口练习项目。

使用FastAPI实现一个简单聊天接口，
学习HTTP请求、JSON数据传输、Pydantic数据验证。

## 技术栈

- Python
- FastAPI
- Pydantic
- Swagger UI

## 实现功能

目前实现：

1. 创建FastAPI服务
2. 创建POST接口
3. 接收JSON请求
4. 使用Pydantic验证数据
5. 使用Swagger测试接口

## 接口说明

POST /chat

请求：

{
    "question":"光合作用在哪里发生？"
}


返回：

{
    "question":"光合作用在哪里发生？"
}

## 学习收获

理解：

- Request Body（请求体）
- API接口通信流程
- JSON数据转换
- 后端接口测试流程
