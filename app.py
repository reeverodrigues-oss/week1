import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage, SystemMessage, AIMessage

load_dotenv()

#initalize the model
llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash",seed=6)

# string based invocation
resp1 = llm.invoke("We are building an AI system for processing medical insurance claims.")
resp2 = llm.invoke("What are the main risks in this system?")


print(f"Original question:")
print(f"resp1: {resp1.content}")

print(f"----------------------------------------------")
print(f"Next question:")
print(f"resp2: {resp2.content}")
print(f"----------------------------------------------")


# Build conversation history using message construct
messages = [
    SystemMessage(content="You are a helpful veteran medical insurance claims representative with 30 years experience that can provide concise and summarized information"),
    HumanMessage(content="We are building an AI system for processing medical insurance claims."),
    AIMessage(content=resp1.content),  #  AIs actual response  passed back into context
    HumanMessage(content="What are the main risks in this system?")
]


# Build conversation history
"""
messages2 = [
    SystemMessage(content="You are a helpful vetran medical insurance claims represenative with 30 years experience that can provide concise and summarized information"),
    HumanMessage(content="We are building an AI system for processing medical insurance claims."),
    HumanMessage(content="What are the main risks in this system?")
]
"""


resp3= llm.invoke(messages)

#resp4= llm.invoke(messages2)

print(f"----------------------------------------------")
print(f"Quetions: chanined with messages")

print(f"resp3: {resp3.content}")
#print(f"resp4: {resp4.content}")



"""
Reflection:

1. Why did string-based invocation fail?
    -Data is out dated
    -LLMs are stateless by nature , once it sends a request it forget anything about it
    This is evident when the LLM was asking for further clarification on what *this* referring below. Attaching response
    **To help me narrow down the risks for *your* system, please tell me:**
    **What kind of system is it?** (e.g., a software application, a manufacturing process, a financial trading platform, a medical device, a supply chain, a public infrastructure system)
    **What is its primary purpose?**
    **Who are the main users or stakeholders?**
    **What are its critical functions?**
    **What kind of data does it handle?**
    **Is it new or established?**


2. Why does message-based invocation work?
    When you pass a list of messages, you're essentially reconstructing the conversation history inside the payload of that one request
    via 
       Human message -> We are building an AI system for processing medical insurance claims
       AI message <- you are feeding it the prior response
       Human message -> What are the main risk
    The model nw has context of all 3 messages and understand what  *this* refers to , which is the medical insurance claims  and the risks  

3. What would break in a production AI system if we ignore message history?
   	Why agent loops are hard in production
	    □ For each decision: 
			® Agent can choose right or wrong tool.
			® Can loop indefinitely.
			® Context blindness.
            ® Inconsistent responses.
            ® Can hallucinate intermediate results.
            ® Poor auditability
            ® Poor user experience.
            ® Errors can compound across steps.
		□ Complexity is less about each tool and more about managing the loop.

"""