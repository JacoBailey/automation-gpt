# Title

ChatGPT Prompt Automation

## Project Description
    
This tool automates repetitive ChatGPT workflows via user-provided templates, simple input handling, and web automation.

## Workflow

1. Create templates for each prompt (using a simple syntax for the input slots)
2. Select a prompt template
3. Submit your inputs for the template
4. Automatically submit the prompt to ChatGPT and copy the response to your clipboard

## Technologies Used

- Python *(Core application logic)*
- SeleniumBase *(Browser automation: simplifies Selenium usage and improves reliability via bot-detection handling)*

## Challenges Faced

- *ChatGPT adding additional security preventing reliable automation*
  I solved this problem by swapping Selenium for SeleniumBase (which uses bot-protection workarounds) and by using alternative DOM interaction strategies, including adjusting selector usage, using alternative automation methods, and separating and/or combining automation steps

- *ChatGPT's site changing selectors and DOM structure (making it difficult to locate specific elements with selectors/XPath)*
  I initially overcame this issue by creating a "multi-selector" mode (to check for multiple selectors) and later fixed it by using simpler, more precise selector choices.

## Features

### Current Features

- Custom user-provided templates
- Simple syntax for template inputs
- Automated prompt submission and response retrieval

### Planned Features

- Multi-message conversation support

## Program Setup

This setup assumes have Python installed on your machine. If not, please install Python prior to performing the setup steps below.

### Installation

1. Clone or download the repository
2. Navigate into the project directory
3. Install dependencies (TBD)

### Setup

1. Open the program file (should be named 'automation-gpt-main')
2. Open the "templates" folder (where your prompt templates will be stored)
3. Create a custom template:
    - *Use formatting shown in the example file (each input slot starts with "INSERT", followed by a space, then the slot name text in all capitals)*
    - *You may delete the example template files after creating your own (**NOTE:** you must always have at least one valid template in this directory)*

## Usage

Run the program:

```bash
python3 chatgpt_prompt_automation.py
```

You may also run the program via a Bash or shell script.

## How To Contribute

Contributions are not currently open, but bug reports and suggestions are welcome.