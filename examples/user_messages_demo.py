import sys

sys.path.append('..')
from actionflow import Assistant, OpenAILLM

Assistant(
    llm=OpenAILLM(model="gpt-3.5-turbo", stop="</answer>"),
    debug_mode=True,
).run(
    messages=[
        {"role": "user", "content": "What is the color of a banana? Provide your answer in the xml tag <answer>."},
        {"role": "assistant", "content": "<answer>"},
    ],
)
