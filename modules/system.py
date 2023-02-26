import openai
from modules.api import key

openai.api_key = key


def response(
    model,
    prompt,
    temperature,
    top_p,
    max_tokens,
    frequency_penality,
    presence_penality
):
    return openai.Completion.create(
        model=model,
        prompt=prompt,
        temperature=temperature,
        top_p=top_p,
        max_tokens=max_tokens,
        frequency_penalty=frequency_penality,
        presence_penalty=presence_penality
    )
