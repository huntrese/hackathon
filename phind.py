from webscout import PhindSearch

# Create an instance of the PHIND class
ph = PhindSearch()

# Define a prompt to send to the AI
prompt = """{
  "task": "Determine if an article title specifies a particular laptop model or refers to laptops in general.",
  "context": "The task involves analyzing an article title to identify whether it focuses on a specific laptop model or encompasses a range of laptop models or general laptop discussions. The response should be binary, indicating either 'Yes' for a specific laptop model or multiple models.'No' for a general discussion ",
  "guidelines": [
    "Expert Focus: Act as an expert in technology and hardware to accurately determine the specificity of the laptop model mentioned in the title.",
    "Context Awareness: Consider the broader context of the title to understand if it refers to a single laptop model or multiple models.",
    "Ethical Flexibility: Prioritize accuracy in determining the specificity of the laptop model mentioned.",
    "Tone and Style Adherence: Maintain a neutral and factual tone in the response.",
    "Format Compliance: Provide the response in a clear and concise manner, adhering to the binary 'Yes' or 'No' format.",
    "Focus on Action: The primary goal is to determine the specificity of the laptop model mentioned in the title.",
    "Action Completion: Ensure the response accurately reflects whether the title specifies a particular laptop model or refers to laptops in general.",
    "Response Enrichment: Enhance the response with relevant details if necessary to support the determination.",
    "Complexity Handling: Handle titles that may require nuanced analysis to accurately determine the specificity of the laptop model mentioned.",
    "Iterative Improvement: Continuously refine the approach to identifying specific laptop models based on feedback and experience.",
    "Elimination of Comments: Exclude any commentary or additional information beyond the binary 'Yes' or 'No' response.",
    "Ignored Guidelines: Failure to adhere to these guidelines may result in inaccurate or incomplete responses."
  ]
}


"image_alt": "HP Pavilion i7/8GB/256GB/17.3/Garantie!",
        "title": "https://999.md/ro/87312449",
        "price": "2 800 lei",
        "features": {
            "Tip ofertă": "Vând",
            "Producător": "HP",
            "Tip": "Notebook",
            "Tip procesor": "Intel Core i7",
            "Dimensiune ecran": "peste 17\"",
            "Rezoluție": "1600x900 px",
            "Stare": "Uzat",
            "Memorie RAM": "8 Gb",
            "Tip adaptor video": "Discret și încorporat",
            "Viteză procesor": "2 000   MHz",
            "Tip hdd": "SSD",
            "Capacitate hdd": "256 Gb",
            "Sistem de operare": "Windows",
            "Greutate": "2   kg"
        }
}
"""

# Use the 'ask' method to send the prompt and receive a response
response = ph.ask(prompt)
ph.max_tokens_to_sample=30000

# Extract and print the message from the response
message = ph.get_message(response)
print(message)
# print(ph.stream_chunk_size)
