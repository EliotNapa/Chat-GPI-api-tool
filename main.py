import logging
import random
import sys
import os
import re
import openai
from typing import List, Dict

def main():
    if len(sys.argv) != 2:
        print("質問が指定されていません。")
        return

    question = sys.argv[1]

    msg_array = (
        [
        {"role": "system", "content": "17歳のギャル風女子高校生です。"},
        {"role": "user", "content": "これからの質問にはギャル風に答えてください。"}, 
        {"role": "assistant", "content": "了解しました。"},
        {"role": "user", "content": question}],

        [
        {"role": "system", "content": "32歳女性高校教師です。"},
        {"role": "user", "content": "これからの質問には優しい女性教師として答えてください。"}, 
        {"role": "assistant", "content": "了解しました。"},
        {"role": "user", "content": question}],

        [
        {"role": "system", "content": "52歳の海兵隊軍曹で訓練教官です。"},
        {"role": "user", "content": "これからの質問には海兵隊の訓練教官軍曹として答えてください。"}, 
        {"role": "assistant", "content": "了解しました。"},
        {"role": "user", "content": question}],

        [
        {"role": "system", "content": "アメリカ大統領です。"},
        {"role": "user", "content": "これからの質問にはアメリカ大統領として答えてください。"}, 
        {"role": "assistant", "content": "了解しました。"},
        {"role": "user", "content": question}],

        [
        {"role": "system", "content": "5歳の幼女ちこちゃんです。"},
        {"role": "user", "content": "これからの質問には5歳のちこちゃんとして答えてください。"}, 
        {"role": "assistant", "content": "了解しました。"},
        {"role": "user", "content": question}],
        )

    key_index = random.randint(0,4)

    openai_api_key = os.environ["OPENAI_API_KEY"]
    response = call_openai(
        api_key=openai_api_key,
        messages=msg_array[key_index],
        user="main.py",
    )
    assistant_reply: Dict[str, str] = response["choices"][0]["message"]
    assistant_reply_text = format_assistant_reply(assistant_reply["content"])
    print(msg_array[key_index][0]['content'])
    print(assistant_reply_text)



def call_openai(api_key: str, messages: List[Dict[str, str]], user: str):
    return openai.ChatCompletion.create(
        api_key=api_key,
        model="gpt-3.5-turbo",
        messages=messages,
        top_p=1,
        n=1,
        max_tokens=1024,
        temperature=1,
        presence_penalty=0,
        frequency_penalty=0,
        logit_bias={},
        user=user,
    )


def format_assistant_reply(content: str) -> str:
    result = content
    for o, n in [
        ("^\n+", ""),
        ("```[Rr]ust\n", "```\n"),
        ("```[Rr]uby\n", "```\n"),
        ("```[Ss]cala\n", "```\n"),
        ("```[Kk]otlin\n", "```\n"),
        ("```[Jj]ava\n", "```\n"),
        ("```[Gg]o\n", "```\n"),
        ("```[Ss]wift\n", "```\n"),
        ("```[Oo]objective[Cc]\n", "```\n"),
        ("```[Cc]\n", "```\n"),
        ("```[Ss][Qq][Ll]\n", "```\n"),
        ("```[Pp][Hh][Pp]\n", "```\n"),
        ("```[Pp][Ee][Rr][Ll]\n", "```\n"),
        ("```[Jj]ava[Ss]cript", "```\n"),
        ("```[Ty]ype[Ss]cript", "```\n"),
        ("```[Pp]ython\n", "```\n"),
    ]:
        result = re.sub(o, n, result)
    return result


if __name__ == "__main__":
    #
    # Local development
    #


    logging.basicConfig(level=logging.ERROR)
    main()