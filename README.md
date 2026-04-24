# Assignment -1 
Repository for Agentic Assignment 1

# Windows - UV Prompt
#   Commands                What it does
    uv sync                 Install or update all packages
    uv add package-name     Add a new package
    uv run app.py           Run the main program
    uv run pytest           Run tests
    uv run ruff format .    Format your code nicely



# 🚀 Quick Start
### Step 1: Download the Project

1. Go to this GitHub repository
2. Click on **Code** → **Download ZIP**  OR  copy the repository URL
3. Extract the ZIP file to a folder on your computer
4. Open **Cursor** (or VS Code)

### Step 2: Open the Project in Cursor

- In Cursor, go to **File → Open Folder**
- Select the folder where you extracted the project (`agentic-day1`)

### Step 3:Setting Up API Keys
After running the copy command:
cp .env.example .env

Open the .env file
Replace the placeholders with your actual keys:

env# ==================== LLM API KEYS ====================

OPENAI_API_KEY=sk-your-actual-openai-key-here
GOOGLE_API_KEY=your-actual-google-gemini-key-here

### Step 4: Search Tools 
tvly-your-actual-tavily-key-here

Where to get API keys:

OpenAI: https://platform.openai.com/api-keys
Google Gemini: https://aistudio.google.com/app/apikey
Tavily: https://app.tavily.com


### Step 4: Install uv (if you don't have it)

Open Terminal in Cursor (`Ctrl + ``) and run:

```
# Go into project folder
cd agentic-day1 


# Check if uv is installed
uv --version

# If not installed, install it:
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"

# Create virtual environment and install all packages
uv sync

# 3. Copy environment file
copy .env.example .env

# 4. Run the application
uv run main.py
```
