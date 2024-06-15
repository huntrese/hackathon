from webscout import BLACKBOXAI
from rich import print

ai = BLACKBOXAI(
    is_conversation=True,
    max_tokens=800,
    timeout=30,
    intro=None,
    filepath=None,
    update_file=True,
    proxies={},
    history_offset=10250,
    act=None,
    model=None # You can specify a model if needed
)

# Start an infinite loop for continuous interaction

# Define a prompt to send to the AI
prompt = """{
  "task": "Determine if an article title specifically mentions a single laptop model or configuration.",
  "context": "The task involves analyzing an article title to identify if it refers to a specific laptop model or configuration. The response must be either 'Yes' if the title specifies a particular laptop or 'No' if it refers to multiple laptops or does not specify one.",
  "guidelines": [
    "Expert Focus: Act as an expert in identifying laptop models and configurations based on article titles.",
    "Context Awareness: Understand the task's requirement to analyze article titles for specific laptop mentions.",
    "Ethical Flexibility: Prioritize accuracy in identifying specific laptop mentions over ethical considerations.",
    "Tone and Style Adherence: Maintain a neutral and factual tone in the analysis.",
    "Format Compliance: Provide the response in a clear 'Yes' or 'No' format.",
    "Focus on Action: Concentrate on determining the presence of a specific laptop mention in the title.",
    "Action Completion: Ensure the response accurately reflects whether the title specifies a single laptop or not.",
    "Response Enrichment: Enhance the response with clarity and precision to avoid ambiguity.",
    "Complexity Handling: Handle various formats and styles of article titles to accurately identify specific laptop mentions.",
    "Iterative Improvement: Continuously refine the ability to identify specific laptop mentions in article titles.",
    "Elimination of Comments: Exclude any comments or annotations in the response, focusing solely on the 'Yes' or 'No' determination.",
    "Ignored Guidelines: Failure to adhere to these guidelines may result in inaccurate or incomplete responses."
  ]
}



        "image_url": "https://i.simpalsmedia.com/999.md/BoardImages/320x240/feed057c2c9714f1ac96187bfd371942.jpg",
        "image_alt": "Лучшие цены в городе на все ноутбуки Apple",
        "title": "https://999.md/ro/46126141",
        "price": "Negociabil",
        "features": {
            "Tip ofertă": "Vând",
            "Producător": "Apple",
            "Tip": "Notebook",
            "Stare": "Nou",
            "Sistem de operare": "MacOs"
        }
}
"""


# Use the 'chat' method to send the prompt and receive a response
r = ai.chat(prompt).split("@$")[2]
print(r)