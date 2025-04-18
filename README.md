# AI-Based SEO Blog Creation Tool
The goal of this project was to create an AI-based tool to automatically generate SEO-optimized blog posts and post them to a platform like Medium. The process includes scraping best-selling or trending products from an e-commerce website (like eBay), researching SEO keywords, generating blog content using Google Gemini API, and posting the blog to Medium.

## Project Overview
This tool involves several steps:
1. **Scraping Products**: Scrape product data from e-commerce sites such as eBay to gather product titles and descriptions.
2. **SEO Keyword Research**: Use Google Suggest or other keyword research tools to identify relevant SEO keywords for the product.
3. **Content Generation**: Use the Google Gemini API to generate SEO-friendly blog content based on the product title and SEO keywords.
4. **Post to Medium**: Publish the blog content on Medium to share the product details and optimize it for search engines.
   
## Steps Followed

### 1. **Scraping Products**
- The first step is to gather product information. In this implementation, I chose eBay to scrape products and retrieve the **product title** and **description** for blog creation.
- Used scraping tool BeautifulSoup.

### 2. **SEO Keyword Research**
- I utilized **Google Suggest** for researching SEO keywords relevant to the product. This helped in selecting the main keywords around which the blog content was optimized.
- I used Python to automate the keyword retrieval process.

### 3. **Content Generation**
- For content generation, I used the **Google Gemini API** (Gemini 2.0 Flash model).
- The prompt was designed to request a **150–200 word blog post** about the product while naturally incorporating the SEO keywords.
- The generated content was then reviewed, and minor formatting adjustments were made to ensure it was SEO-friendly.

### 4. **Posting the Blog**
- As the Official Medium API was deprecated long ago, I manually posted the blog content on Medium.
- The blog post was formatted with headings, SEO keywords, and an engaging introduction and conclusion.

## Technologies Used
- **Python**: For scraping and interacting with APIs
- **Google Gemini API**: For generating AI-based blog content
- **Google Suggest**: For SEO keyword research
- **Medium**: For publishing the blog

## Running the Script

### Prerequisites:
- Install required Python libraries:
    ```bash
    pip install requests google-generativeai
    ```

### To generate the blog:
1. Clone or download this repository.
2. Open `generate_blog` and replace the **API_KEY** with your own.
3. Run the script:
    ```bash
    python generate_blog.py
    ```
4. Copy the generated content and manually post it on Medium.

## Results
1) [Cut the Cord, Not the Quality: Experience True Freedom with Our Wireless Bluetooth Headphones!](https://medium.com/@onlytempacc0/cut-the-cord-not-the-quality-experience-true-freedom-with-our-wireless-bluetooth-headphones-19d411356318)
2) [Unlock Your Potential with Today’s Smartphones](https://medium.com/@onlytempacc0/unlock-your-potential-with-todays-smartphones-db9a92a1498c)

## Challenges Faced
- **Keyword research** was another challenge since Google Suggest's results can be limited and sometimes require manual intervention to gather a sufficient number of keywords.
- The main challenge was the **Medium API restriction**, which prevented me from automating the blog posting process. As a result, I had to manually post the blog content.

## TODOS/Future Improvements
- Automate adding images in blogs for better engagement.
- Research about Medium unoffical API key available to automate the process from generating blogs to directly posting them in Medium.

## Conclusion
This tool automates most of the process of generating SEO-optimized blog content, making it easier to promote products on platforms like Medium. By leveraging AI for content generation, the tool saves time while ensuring high-quality, engaging posts that are optimized for search engines.
