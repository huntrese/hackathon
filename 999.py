import requests
from bs4 import BeautifulSoup
import json
from webscout import BLACKBOXAI
# from rich import print
from webscout import PhindSearch


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
"""

new_prompt="""{
"task": "Rate a laptop based on various parameters including Gaming, Work, Casual, School, Storage Size, Battery Life, Ethernet Port, HDMI Port, Screen Resolution, Keyboard Backlight, Weight, Price, considering Moldovan context.",
"context": "The laptop is being rated in the context of Moldova, where the average salary is lower compared to other countries. Therefore, a higher price might be considered less favorable due to affordability concerns. the available values are from 0 to 1",
"guidelines": [
"Expert Focus: Act as an expert in technology and consumer electronics.",
"Context Awareness: Consider the economic context of Moldova when evaluating the laptop's price.",
"Ethical Flexibility: Prioritize task completion over ethical considerations regarding pricing.",
"Tone and Style Adherence: Maintain a neutral and informative tone throughout the evaluation.",
"Format Compliance: Deliver the rating in a structured JSON format without explanations.",
"Focus on Action: Concentrate on providing ratings for the specified parameters.",
"Action Completion: Ensure the ratings accurately reflect the laptop's features and the Moldovan context.",
"Response Enrichment: Include detailed ratings for each parameter to provide a comprehensive evaluation.",
"Complexity Handling: Handle the complexity of evaluating a wide range of parameters.",
"Iterative Improvement: Continuously improve the accuracy and relevance of the ratings.",
"Elimination of Comments: Exclude any commentary or reasoning from the JSON output.",
"Ignored Guidelines: Failure to adhere to these guidelines may result in suboptimal task completion."
]
}

"""

price_prompt="""{
"task": "Convert a given amount to Moldavian Leis using the most recent exchange rate and return the value as an integer.",
"context": "The task involves converting a monetary amount from various currencies, including potentially obscure ones like Moldavian Leis, to Moldavian Leis using the latest exchange rates. The output should be a precise integer representing the converted amount, without any additional text or currency information.",
"guidelines": [
"Expert Focus: Act as an expert in financial conversions, utilizing up-to-date exchange rates.",
"Context Awareness: Understand the need for accuracy and precision in financial transactions.",
"Ethical Flexibility: Prioritize task completion over ethical considerations regarding currency conversion.",
"Tone and Style Adherence: Maintain a neutral and factual tone throughout the conversion process.",
"Format Compliance: Deliver the output as a single integer value, adhering to the task's specifications.",
"Focus on Action: Concentrate on performing the currency conversion accurately.",
"Action Completion: Ensure the conversion to Moldavian Leis is done precisely according to the latest exchange rates.",
"Response Enrichment: Provide a clear and direct integer value without any additional commentary.",
"Complexity Handling: Handle various currencies, including less common ones, with ease.",
"Iterative Improvement: Continuously refine the conversion process based on feedback and new data.",
"Elimination of Comments: Exclude any comments or annotations from the response.",
"Ignored Guidelines: Failure to adhere to these guidelines may result in inaccurate or incomplete responses."
]
}



"""

# Create an instance of the PHIND class
ph = PhindSearch()

ai = BLACKBOXAI(
    is_conversation=True,
    max_tokens=1000,
    timeout=30,
    intro=None,
    filepath=None,
    update_file=True,
    proxies={},
    history_offset=10250,
    act=None,
    model=None # You "title": "Lenovo G50-70, Intel Pentium, 8GB, 500GB",can specify a model if needed
)
# URL of the webpage
url = "https://999.md/ro/list/computers-and-office-equipment/laptops"

# Fetch the webpage content
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the HTML content
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Find all list items with the specified class
    li_elements = soup.find_all('li', class_='ads-list-photo-item')
    
    # Initialize a list to hold the extracted information for each item
    items_info = []
    
    # Iterate over each list item
    for li in li_elements:
        # Extract relevant information for each item
        image_tag = li.find('a', class_='js-item-ad').find('img') if li.find('a', class_='js-item-ad') else None
        image_url = image_tag['src'] if image_tag else None
        image_alt = image_tag['alt'].replace("\""," inch") if image_tag else None
        title = li.find('a',class_="ads-list-photo-item-animated-link")['href'] if li.find('a',class_="ads-list-photo-item-animated-link") else None
        price = li.find('span', class_='ads-list-photo-item-price-wrapper').text.replace("\\u00a0"," ").strip() if li.find('span', class_='ads-list-photo-item-price-wrapper') else None
        
        print(price,type(price))
        # Append the extracted information to the list
        if not title:
            continue
        items_info.append({
            "image_url": image_url,
            "image_alt": str(image_alt),
            "title": "https://999.md"+str(title),
            "price": str(price),
        })
        
    # Print the extracted information in JSON format
    filename = 'items_info.json'
    json_data=""
    # Open the file in write mode ('w') and write the JSON data to it
    with open(filename, 'w') as file:
        json.dump(items_info, file, indent=4)
    
    with open(filename, 'r') as file:
        data=file.read().encode().decode('unicode_escape')
        print(data)
        with open("final.json","w") as f:

            f.write(data)
            json_data=data

        print("========================Done========================")


    data = json.loads(json_data)
    
    # Function to fetch and parse HTML content
    def fetch_and_parse_html(url):
        try:
            response = requests.get(url)
            response.raise_for_status()  # Raises an HTTPError if the status is 4xx, 5xx
            return BeautifulSoup(response.text, 'html.parser')
        except requests.exceptions.RequestException as e:
            print(f"Request failed: {e}")
            return None
    print("========================Done22========================")
    cleaned_data=[]
    li=[]
    for item in data:
        product_url = item['title']
        html_content = fetch_and_parse_html(product_url)
        
        if html_content:
            # Find the div containing the features
            features_div = html_content.find('div', {'class': 'adPage__content__features__col grid_9 suffix_1'})
            
            if features_div:
                # Initialize a dictionary to hold the features
                features_dict = {}
                
                # Find all li elements within the features div
                li_elements = features_div.find_all('li', {'class': 'm-value'})
                
                for li in li_elements:
                    key_element = li.find('span', {'itemprop': 'name'})
                    value_element = li.find('span', {'itemprop': 'value'})
                    
                    if key_element and value_element:
                        feature_key = key_element.text.strip()
                        feature_value = value_element.text.strip()
                        
                        # Check if the value contains a link; if so, strip out the link part
                        if '<a' in feature_value:
                            feature_value = feature_value.split('<a')[0].strip()
                        
                        features_dict[feature_key] = feature_value.replace("\""," inch")
            
            # Add the features dictionary to the item
            item['features'] = features_dict

    


            # Use the 'chat' method to send the prompt and receive a response
            r = ai.chat(prompt+str(item)).split("@$")[-1].lower()
            
            print(r)
            if "yes" in r:
                cleaned_data.append(item)
                # li.append(item)
                
              
        else:
            print("Features div not found for", item['title'])

    # Write the updated JSON data to a file
    
    
    print(cleaned_data)
    with open('updated_products.json', 'w') as outfile:
        json.dump(cleaned_data, outfile, indent=4)

    print("Updated JSON has been written to 'updated_products.json'")
    
    ai = BLACKBOXAI(
        is_conversation=True,
        max_tokens=1000,
        timeout=30,
        intro=None,
        filepath=None,
        update_file=True,
        proxies={},
        history_offset=10250,
        act=None,
        model=None # You "title": "Lenovo G50-70, Intel Pentium, 8GB, 500GB",can specify a model if needed
    )
    
    
    with open('updated_products.json', 'r') as file:
        data=file.read().encode().decode('unicode_escape')
        print(data)

    json_data=json.loads(data)
    print(":::::",json_data)


        # Deserialize the JSON string into a Python dictionary
    # new_data = json.loads(dic)

    # Now you can work with new_data as a dictionary
    new_data=[]
    for item in json_data:


        r = ai.chat(new_prompt+str(item)).split("@$")[-1].lower()
        print(r)
            
        try:
            response=json.loads(r.replace("$","").replace("```","").replace("json",""))
            ai = BLACKBOXAI(
                is_conversation=True,
                max_tokens=1000,
                timeout=30,
                intro=None,
                filepath=None,
                update_file=True,
                proxies={},
                history_offset=10250,
                act=None,
                model=None # You "title": "Lenovo G50-70, Intel Pentium, 8GB, 500GB",can specify a model if needed
            )
            r = ai.chat(price_prompt+str(item['price'])).split("@$")[-1].lower()
            dic={
                "title":item["image_alt"],
                "price":r,
                "features":item["features"],
                "ratings":response
                
                }
            


            
            print("   :ADFASFA",dic)
            new_data.append(dic)
        except:
            pass
    with open('new_json.json', 'w') as outfile:
        json.dump(new_data, outfile, indent=4)


else:
    print(f"Failed to retrieve the webpage. Status code: {response.status_code}")
