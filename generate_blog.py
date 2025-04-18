import google.generativeai as genai

API_KEY = "enter-gemini-api-key" 
genai.configure(api_key=API_KEY)

def generate_blog_post(product_title, keywords):
    prompt = f"""
    Write a 150-200 word blog post about the product "{product_title}". 
    Include the following SEO keywords naturally: {', '.join(keywords)}. 
    Focus on the product's features and benefits, and ensure the content is SEO-friendly. 
    The tone should be professional but engaging, with a call to action at the end.
    """
    
    model = genai.GenerativeModel("gemini-2.0-flash")  # Using Google Gemini's model
    response = model.generate_content(prompt)

    return response.text

# Example usage
if __name__ == "__main__":
    # Example product title and SEO keywords
    product_title = "Wireless Bluetooth Headphones"
    keywords = ["wireless headphones", "Bluetooth headphones", "best headphones for music", "headphones for workout"]

    blog_post = generate_blog_post(product_title, keywords)
    
    print("\nGenerated Blog Post:\n")
    print(blog_post)
