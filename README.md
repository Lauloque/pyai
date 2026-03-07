# pyai

Simple AI agent based on Gemini as a Python learning project from [Build an AI Agent in Python \[Full Course\] | Boot.dev](https://www.boot.dev/courses/build-ai-agent-python)

![Certification of Completion soon...]()

## Setup

Requires:
- The [uv](https://github.com/astral-sh/uv) project/package manager ([installation docs](https://docs.astral.sh/uv/getting-started/installation/))
- Access to a Unix-like shell (e.g. `zsh` or `bash`)
- Python 3.12

Initialize your virtual environment with uv:

```bash
uv venv --python 3.12
source .venv/bin/activate
uv add google-genai==1.12.1
uv add python-dotenv==1.1.0
```

Then you can run python files using `uv run <filename>`.

## Usage 
*Optional arguments in brackets []*

- main.py [-h] [-v] user_prompt

  Simple chatbot to... chat with... Original!
  
  positional arguments:
    user_prompt    User prompt
  
  options:
    -h, --help     show this help message and exit
    -v, --verbose  enable verbose output
