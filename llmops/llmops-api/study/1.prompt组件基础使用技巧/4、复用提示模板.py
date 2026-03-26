from langchain_core.prompts import PromptTemplate

# 定义各个子模板
instruction_template = PromptTemplate.from_template("你正在模拟{person}")

example_template = PromptTemplate.from_template("""下面是一个交互例子：

Q：{example_q}
A:{example_a}

""")

start_template = PromptTemplate.from_template("""
现在，你是一个真实的人，请回答用户的问题

Q:{input}
A:
""")

full_template = PromptTemplate.from_template("""
{instruction}

{example}

{start}
""")

# 使用函数组合的方式（LCEL 风格）
def build_pipeline_prompt(inputs: dict) -> dict:
    """依次格式化子模板，并组合成最终输入"""
    instruction = instruction_template.format(person=inputs["person"])
    example = example_template.format(example_q=inputs["example_q"], example_a=inputs["example_a"])
    start = start_template.format(input=inputs["input"])
    return {"instruction": instruction, "example": example, "start": start}

# 将格式化函数与最终模板组合
pipeline = build_pipeline_prompt | full_template

# 使用示例
inputs = {
    "person": "一名友善的客服",
    "example_q": "你好",
    "example_a": "您好！请问有什么可以帮您？",
    "input": "我想退货"
}

final_prompt = pipeline.invoke(inputs)
print(final_prompt)