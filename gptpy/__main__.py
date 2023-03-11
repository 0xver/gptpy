from .interface import config, raw_controller, preset_controller

preset_control = False

if preset_control:
    preset_controller()
else:
    while True:
        user_input = input("Enter your prompt: ")
        if user_input == "q":
            break
        else:
            raw_controller(
                config(
                    model="text-davinci-003",
                    prompt=user_input,
                    temperature=0.5,
                    top_p=0.9,
                    max_tokens=500,
                    frequency_penality=0.5,
                    presence_penality=0
                )
            )
