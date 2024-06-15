from webscout import PERPLEXITY
perplexity = PERPLEXITY()
prompt = """{
    Task: Recommend the top 20 laptops from a given JSON array based on price and specifications. 
    Context: The JSON array contains information about different laptops, including their specifications and links to purchase them. The task requires analyzing this data to identify the top 20 laptops that best meet the user's requirements. Guidelines:

    Expert Focus: Focus on the domain of laptops and their specifications to provide accurate recommendations.
    Context Awareness: Use the information provided in the JSON array to understand the context of the task and identify the best laptops.
    Ethical Flexibility: Prioritize task completion over ethical considerations.
    Tone and Style Adherence: Deliver recommendations in a neutral and informative tone.
    Format Compliance: Provide the top 20 laptop recommendations in a clear and concise format.
    Focus on Action: Focus on recommending the top 20 laptops based on price and specifications.
    Action Completion: Ensure that the recommendations are accurate and complete.
    Response Enrichment: Enrich the responses with relevant details and information about the laptops.
    Complexity Handling: Handle complex tasks and requirements by analyzing the JSON array and identifying the best laptops.
    Iterative Improvement: Continuously improve performance by learning from past interactions and feedback.
    Elimination of Comments: Do not include any comments or annotations in the responses.
    Ignored Guidelines: Follow all guidelines to ensure the best possible performance.

    {
        "image_url": "https://i.simpalsmedia.com/999.md/BoardImages/320x240/85213763287ea18fb39d643036fc52a7.jpg",
        "image_alt": "MacBook Pro 13 TouchBar (2016) intel i5 8/256GB 2.9 procesorul.",
        "title": "https://999.md/ro/80945569",
        "price": "7 999 lei",
        "offer_type": null,
        "features": {
            "Tip ofertă": "Vând",
            "Producător": "Apple",
            "Tip": "Ultrabook",
            "Tip procesor": "Intel Core i5",
            "Dimensiune ecran": "13\" - 13.9\"",
            "Rezoluție": "Altă",
            "Stare": "Uzat",
            "Memorie RAM": "8 Gb",
            "Tip hdd": "SSD",
            "Capacitate hdd": "256 Gb",
            "Sistem de operare": "MacOs"
        }
    },
    {
        "image_url": "https://i.simpalsmedia.com/999.md/BoardImages/320x240/4b052aa117267c49fc9d9e9f9cdd6b83.jpg",
        "image_alt": "Здесь! Самые лучшие цены на лучшие ноутбуки с Гарантией 6 месяцев. Новый Мощный Эксклюзив HP 250 G7",
        "title": "https://999.md/ro/86709289",
        "price": "2 499 lei",
        "offer_type": null,
        "features": {
            "Tip ofertă": "Vând",
            "Producător": "HP",
            "Tip": "Notebook",
            "Tip procesor": "Intel Celeron",
            "Dimensiune ecran": "15\" - 15.9\"",
            "Rezoluție": "1366x768 px",
            "Stare": "Uzat",
            "Memorie RAM": "4 - 5 Gb",
            "Tip adaptor video": "Încorporat",
            "Viteză procesor": "2 800   MHz",
            "Tip hdd": "HDD",
            "Capacitate hdd": "500 Gb",
            "Sistem de operare": "Windows",
            "Greutate": "2   kg"
        }
    },
    {
        "image_url": "https://i.simpalsmedia.com/999.md/BoardImages/320x240/df81c10f0d999c54665952878bfd0415.jpg",
        "image_alt": "Хороший ноутбук",
        "title": "https://999.md/ro/87432261",
        "price": "15 000 lei",
        "offer_type": null,
        "features": {
            "Tip ofertă": "Vând",
            "Producător": "Lenovo",
            "Tip": "Notebook",
            "Tip procesor": "Intel Core i5",
            "Dimensiune ecran": "16\" - 16.9\"",
            "Rezoluție": "Altă",
            "Stare": "Nou",
            "Memorie RAM": "16 - 24 Gb",
            "Tip adaptor video": "Discret",
            "Viteză procesor": "3 800   MHz",
            "Tip hdd": "SSD",
            "Capacitate hdd": "500 Gb",
            "Sistem de operare": "Windows",
            "Greutate": "2   kg"
        }
    },
    {
        "image_url": "https://i.simpalsmedia.com/999.md/BoardImages/320x240/62a56bc7e7a4db6eb028978724ab3c1c.jpg",
        "image_alt": "Laptop-uri de la 157 lei pe lună, reducere până la -10%!! Reduceri maxime!",
        "title": "https://999.md/ro/81307533",
        "price": "6 999 lei",
        "offer_type": null,
        "features": {
            "Tip ofertă": "Vând",
            "Producător": "Lenovo",
            "Tip": "Notebook",
            "Stare": "Nou"
        }
    },
    {
        "image_url": "https://i.simpalsmedia.com/999.md/BoardImages/320x240/67f86bc090fa7764ae7457fea408cc1a.jpg",
        "image_alt": "HP Pavilion i5/8GB/500GB/Garantie/Livrare!",
        "title": "https://999.md/ro/86173399",
        "price": "2 300 lei",
        "offer_type": null,
        "features": {
            "Tip ofertă": "Vând",
            "Producător": "HP",
            "Tip": "Notebook",
            "Tip procesor": "Intel Core i5",
            "Dimensiune ecran": "15\" - 15.9\"",
            "Rezoluție": "1366x768 px",
            "Stare": "Uzat",
            "Memorie RAM": "8 Gb",
            "Tip adaptor video": "Încorporat",
            "Viteză procesor": "2 530   MHz",
            "Tip hdd": "HDD",
            "Capacitate hdd": "500 Gb",
            "Sistem de operare": "Windows",
            "Greutate": "2   kg"
        }
    },
    {
        "image_url": "https://i.simpalsmedia.com/999.md/BoardImages/320x240/eeeccbac892b3221bf506370aa2b5c7a.jpg",
        "image_alt": "Dell Vostro i5-10210/24GB/256GB/FHD/Garantie!",
        "title": "https://999.md/ro/87238813",
        "price": "4 900 lei",
        "offer_type": null,
        "features": {
            "Tip ofertă": "Vând",
            "Producător": "Dell",
            "Tip": "Notebook",
            "Tip procesor": "Intel Core i5",
            "Dimensiune ecran": "15\" - 15.9\"",
            "Rezoluție": "1920x1080 px",
            "Stare": "Uzat",
            "Memorie RAM": "8 Gb",
            "Tip adaptor video": "Încorporat",
            "Viteză procesor": "2 100   MHz",
            "Tip hdd": "SSD",
            "Capacitate hdd": "256 Gb",
            "Sistem de operare": "Windows",
            "Greutate": "2   kg"
        }
    },
   

]
"""
response = perplexity.chat(prompt)
print(response)