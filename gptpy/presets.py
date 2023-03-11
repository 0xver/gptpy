def education(user_prompt):
    model = "text-davinci-003"
    prompt = user_prompt
    temperature = 0
    top_p = 0.1
    max_tokens = 500
    frequency_penalty = 0
    presence_penalty = 0

    return [
        model,
        prompt,
        temperature,
        top_p,
        max_tokens,
        frequency_penalty,
        presence_penalty
    ]


def standard(user_prompt):
    model = "text-davinci-003"
    prompt = user_prompt
    temperature = 0.5
    top_p = 0.9
    max_tokens = 500
    frequency_penalty = 0.5
    presence_penalty = 0

    return [
        model,
        prompt,
        temperature,
        top_p,
        max_tokens,
        frequency_penalty,
        presence_penalty
    ]


def creative(user_prompt):
    model = "text-davinci-003"
    prompt = user_prompt
    temperature = 1.5
    top_p = 1
    max_tokens = 500
    frequency_penalty = 1
    presence_penalty = 0

    return [
        model,
        prompt,
        temperature,
        top_p,
        max_tokens,
        frequency_penalty,
        presence_penalty
    ]
