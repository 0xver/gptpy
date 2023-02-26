# GPTpy

[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)

### GPT-powered text generator with OpenAI Python library

GPTpy is a Python boilerplate that utilizes OpenAI's GPT technology to generate human-like text in real-time. It includes presets for different output ranges, with formats tailored for education, standard usage, and creative prompts. Designed for self-driven work in a terminal environment, GPTpy is a versatile tool for personal projects and experimentation.

## Linux Installation

Make sure you use `python3` instead of `python` to run Python 3 or create shell aliases for `python` and `pip` that always default to `python3` and `pip3`

Create a Python virtual environment in the GPTpy directory before installing:

```
python -m venv env
```

Activate the virtual environment:

```
source env/bin/activate
```

Install the required Python packages:

```
pip install .
```

Add your API key from [OpenAI](https://platform.openai.com/account/api-keys)

Create the .env file from your terminal in the project directory:

```
touch .env
```

Add the API key in the .env file:

```
OPENAI_API_KEY=...
```

Your project directory should now look like this:

```
gptpy
├─ env
├─ modules
│  ├─ api.py
│  ├─ interface.py
│  ├─ presets.py
│  ├─ system.py
├─ __main__.py
├─ .env
├─ LICENSE.md
├─ README.md
├─ setup.py
```

## Usage

Make sure you are inside the project directory then start GPTpy in your terminal:

```
python .
```

Configure the GPT model hyperparameters manually in `__main__.py`:

(Note that `user_prompt` is added in the terminal input when the application is running)

```py
#__main__.py

config(
    model="text-davinci-003",
    prompt=user_input,
    temperature=0.5,
    top_p=0.9,
    max_tokens=500,
    frequency_penality=0.5,
    presence_penality=0
)
```

Alternate from manual control to preset control by setting `preset_control` to True:

```py
# __main__.py

preset_control = True
```

## Resources

It is recommended to create shell aliases in your ~/.bashrc or ~/.zshrc file located in your home directory to always run Python 3:

```
alias python="python3"
alias pip="pip3"
```

If you always name your virtual environments as `env` you can create a shell alias to quickly activate the environment using the `activate` command:

```
alias activate="source env/bin/activate"
```

Here are some resourceful links for this project:

- [Playground](https://platform.openai.com/playground)
- [Python Library](https://platform.openai.com/docs/libraries/python-bindings)
- [OpenAI GitHub](https://github.com/openai/openai-python)
