# import os
# from dotenv import load_dotenv

# from agents import  OpenAIChatCompletionsModel, AsyncOpenAI, set_tracing_disabled

# # 🌿 Load environment variables from .env file
# load_dotenv()

# # 🚫 Disable tracing for clean output (optional for beginners)
# set_tracing_disabled(disabled=False)

# # 🔐 1) Environment & Client Setup
# GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")  # 🔑 Get your API key from environment
# BASE_URL = "https://generativelanguage.googleapis.com/v1beta/openai/"  # 🌐 Gemini-compatible base URL (set this in .env file)

# # 🌐 Initialize the AsyncOpenAI-compatible client with Gemini details
# external_client: AsyncOpenAI = AsyncOpenAI(api_key=GEMINI_API_KEY, base_url=BASE_URL)

# # 🧠 2) Model Initialization
# model_2: OpenAIChatCompletionsModel = OpenAIChatCompletionsModel(model="gemini-2.5-flash", openai_client=external_client)



import os
from dotenv import load_dotenv

from agents import OpenAIChatCompletionsModel, AsyncOpenAI, set_tracing_disabled

# 🌿 Load environment variables from .env file
load_dotenv()

# 🚫 Disable tracing
set_tracing_disabled(disabled=False)

# 🔐 API Key & Base URL
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
BASE_URL = "https://generativelanguage.googleapis.com/v1beta/openai/"

# 🔑 Patch OPENAI_API_KEY env so OpenAI client na complain kare
os.environ["OPENAI_API_KEY"] = GEMINI_API_KEY

# 🌐 Initialize Async client
external_client: AsyncOpenAI = AsyncOpenAI(
    api_key=GEMINI_API_KEY,
    base_url=BASE_URL
)

# 🧠 Model
model_2: OpenAIChatCompletionsModel = OpenAIChatCompletionsModel(
    model="gemini-2.5-flash",
    openai_client=external_client
)
