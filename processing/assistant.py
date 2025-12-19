from utils.rag_knowledge import KNOWLEDGE_BASE, SYSTEM_PROMPT
from openai import OpenAI
from utils.state_manager import get_messages

BASE_URL = 'http://localhost:11434/v1'
MODEL = 'qwen2.5:3b'

assistant = OpenAI(
    base_url=BASE_URL,
    api_key="ollama",
)

def extract_relevant_sections(user_message: str) -> str:
    """
    Extract relevant sections from knowledge base based on user's query.
    Uses keyword matching to find related information.
    """
    user_lower = user_message.lower()
    relevant_sections = set()
    
    for keyword, section in KNOWLEDGE_BASE.items():
        if keyword in user_lower:
            relevant_sections.add(section)
    
    page_patterns = {
        "home": KNOWLEDGE_BASE.get("home", ""),
        "page 1": KNOWLEDGE_BASE.get("basic", ""),
        "page 2": KNOWLEDGE_BASE.get("filter", ""),
        "page 3": KNOWLEDGE_BASE.get("edge", ""),
        "page 4": KNOWLEDGE_BASE.get("threshold", ""),
        "page 5": KNOWLEDGE_BASE.get("morphology", ""),
        "page 6": KNOWLEDGE_BASE.get("enhancement", ""),
        "page 7": KNOWLEDGE_BASE.get("batch", ""),
        "page 8": KNOWLEDGE_BASE.get("face", ""),
    }
    
    for pattern, section in page_patterns.items():
        if pattern in user_lower and section:
            relevant_sections.add(section)
    
    if relevant_sections:
        return "\n\n" + "## RELEVANT DETAILED INFORMATION\n\n" + "\n\n".join(relevant_sections)
    return ""


def generate_bot_response(user_message):
    """
    Generates a streaming response from the LLM.
    """
    base_prompt = SYSTEM_PROMPT
    
    relevant_info = extract_relevant_sections(user_message)
    
    enhanced_prompt = base_prompt + relevant_info
    
    messages = [{"role": "system", "content": enhanced_prompt}]
    
    conversation_history = get_messages()
    for msg in conversation_history:
        role = "assistant" if msg["role"] == "bot" else msg["role"]
        messages.append({"role": role, "content": msg["content"]})
    
    messages.append({"role": "user", "content": user_message})
    
    response = assistant.chat.completions.create(
        model=MODEL,
        messages=messages,
        temperature=0.5,
        stream=True,
    )
    
    for chunk in response:
        content = chunk.choices[0].delta.content
        if content is not None:
            yield content
