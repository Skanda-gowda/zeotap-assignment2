# zeotap-assignment2
# 📝 CDP Support Agent Chatbot

This project is a **CDP Support Agent Chatbot** designed to assist users in retrieving relevant documentation and answers to questions related to Zeotap's CDP (Customer Data Platform). The chatbot intelligently parses the content and provides solutions based on user queries.

# 📸 Screenshot
![image](https://github.com/user-attachments/assets/67ce8cb1-f47e-4870-aeaa-9df6a9cfad06)


## 📌 **Features**

1. **Content Parsing:**
   - Extracts and retrieves content from web pages based on HTML structure.
   - Focuses on fetching answers within specific tags (e.g., `<strong>`, `<p>`) for accuracy.

2. **Question-Answering:**
   - Allows users to input queries about Zeotap CDP features and functionalities.
   - Provides concise and relevant answers.

3. **Scalable Design:**
   - Built with modular code, making it adaptable to different content sources.

4. **Error Handling:**
   - Manages cases where relevant content cannot be found and informs users appropriately.

---

## 🚀 **Getting Started**

### **Prerequisites**
- Python 3.x
- Required Libraries:
  - `beautifulsoup4`
  - `requests`

Install the required libraries using:
```bash
pip install beautifulsoup4 requests
```
How to Run
Clone the repository:

```
git clone https://github.com/your-username/cdp-chatbot.git
cd cdp-chatbot
```
Run the chatbot script:

```
python app.py
```
Input your question about Zeotap CDP to get answers.

📚 Usage Example
User Input:
"How can I integrate my data with Zeotap?"

Chatbot Response:
Step 1 - Source Creation  

Step 2 - Source Implementation  

 Step 3 - Previewing Data  


 Step 4 - Catalogue Mapping  


 Step 5 - Create Calculated Attributes  


 Step 6 - Create Your Audience  


 Step 7 - Activation  


🤖 Technologies Used
Python: Backend development and HTML parsing.
Beautiful Soup: For extracting data from HTML documents.
Requests: For handling HTTP requests.
🛡️ Error Handling
The chatbot provides meaningful feedback if:

The queried content is unavailable.
Incorrect tags or invalid HTML structures are encountered.
🗂️ Future Enhancements
Integrate machine learning to improve query understanding.
Expand support for multiple documentation formats (e.g., PDFs).
Add a web interface for enhanced user interaction.
