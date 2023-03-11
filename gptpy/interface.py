from .system import response
from .presets import education, standard, creative


def config(
    model,
    prompt,
    temperature,
    top_p,
    max_tokens,
    frequency_penality,
    presence_penality
):
    return [
        model,
        prompt,
        temperature,
        top_p,
        max_tokens,
        frequency_penality,
        presence_penality
    ]


def raw_controller(args):
    answer = response(*args).choices[0].text.strip()
    tokens_in_prompt = round(len(answer)/4)
    if answer != "" and answer != "?":
        print(f"~{tokens_in_prompt} tokens in prompt")
        print(f"\n\n{answer}\n\n")
    else:
        print("Sorry, I couldn't generate a response for that prompt.")


def preset_controller():
    while True:
        user_type = input(
            "Enter your type - [e] education, "
            "[s] standard, "
            "[c] creative, "
            "[q] quit: "
        )
        if user_type == "q":
            break
        user_prompt = input("Enter your prompt: ")
        if user_type == "e":
            answer = response(*education(user_prompt)).choices[0].text.strip()
            tokens_in_prompt = round(len(answer)/4)
            answer_type = "Education response..."
        elif user_type == "s":
            answer = response(*standard(user_prompt)).choices[0].text.strip()
            tokens_in_prompt = round(len(answer)/4)
            answer_type = "Standard response..."
        elif user_type == "c":
            answer = response(*creative(user_prompt)).choices[0].text.strip()
            tokens_in_prompt = round(len(answer)/4)
            answer_type = "Creative response..."
        if answer != "" and answer != "?":
            print(f"~{tokens_in_prompt} tokens in prompt")
            print(answer_type)
            print(f"\n\n{answer}\n\n")
        else:
            print("Sorry, I couldn't generate a response for that prompt.")
