import requests
from bs4 import BeautifulSoup
import streamlit as st
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

# Function to fetch and parse content from Segment docs
def fetch_segment_instructions():
    url = "https://segment.com/docs/connections/sources/#create-a-source/"
    headers = {
        "User-Agent": (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
            "(KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
        )
    }

    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        return f"Failed to retrieve documentation from {url}. Status code: {response.status_code}"

    soup = BeautifulSoup(response.text, "html.parser")
    section = soup.find(id="create-a-source")
    if not section:
        return "Could not find the 'Create a source' section on the page."

    steps = section.find_next("ol")
    if not steps:
        return "No detailed steps found under the 'Create a source' section."

    content = ["**Steps to Create a Source in Segment:**"]
    for step in steps.find_all("li"):
        content.append(f"- {step.get_text(strip=True)}")
    return "\n".join(content)

# Function to fetch and parse content from mParticle docs
def fetch_mparticle_instructions():
    url = "https://docs.mparticle.com/"
    headers = {
        "User-Agent": (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
            "(KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
        )
    }

    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        return f"Failed to retrieve documentation from {url}. Status code: {response.status_code}"

    soup = BeautifulSoup(response.text, "html.parser")

    # Find all `div` elements with the class `body`
    body_sections = soup.find_all("div", class_="body")
    if not body_sections:
        return "Could not find relevant content in the 'Manage User Profiles' section."

    content = ["**Steps to Create a User Profile in mParticle:**"]

    # Iterate over the sections to extract `h3` and `p` text
    for section in body_sections:
        h3_tag = section.find("h3")  # Find the h3 tag
        p_tag = section.find("p")  # Find the p tag

        if h3_tag:
            content.append(f"- {h3_tag.get_text(strip=True)}")  # Add the header
        if p_tag:
            content.append(f"  {p_tag.get_text(strip=True)}")  # Add the description

    return "\n".join(content)


# Function to fetch and parse content from Lytics docs
def fetch_lytics_instructions():
    url = "https://docs.lytics.com/docs/audiences"
    headers = {
        "User-Agent": (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
            "(KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
        )
    }

    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        return f"Failed to retrieve documentation from {url}. Status code: {response.status_code}"

    soup = BeautifulSoup(response.text, "html.parser")

    # Locate the blockquote with the required class
    callout_section = soup.find("blockquote", class_="callout callout_info")
    if not callout_section:
        return "Could not find the required information inside the 'callout_info' section."

    # Extract all <p> tags within this blockquote
    paragraphs = callout_section.find_all("p")
    if not paragraphs:
        return "No paragraphs found within the 'callout_info' section."

    content = ["**Steps or Information from Lytics Documentation:**"]
    for paragraph in paragraphs:
        content.append(paragraph.get_text(strip=True))
    
    return "\n".join(content)


# Function to fetch and parse content from Zeotap docs
def fetch_zeotap_instructions():
    url = "https://docs.zeotap.com/articles/#!integrate-customer/integrate"
    headers = {
        "User-Agent": (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
            "(KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
        )
    }

    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        return f"Failed to retrieve documentation from {url}. Status code: {response.status_code}"

    soup = BeautifulSoup(response.text, "html.parser")

    # Extract all <strong> tags from the document
    strong_tags = soup.find_all("strong")
    if not strong_tags:
        return "Step 1 - Source Creation\n Step 2 - Source Implementation \n Step 3 - Previewing Data \n Step 4 - Catalogue Mapping \n Step 5 - Create Calculated Attributes \n Step 6 - Create your Audience \n Step 7 - Activation"

    # Collect the text from all <strong> tags
    steps = [f"- {tag.get_text(strip=True)}" for tag in strong_tags]

    if not steps:
        return "No relevant content found in <strong> tags."

    content = ["**Steps to Integrate Your Data with Zeotap:**"] + steps
    return "\n".join(content)




# Streamlit frontend
st.title("CDP Support Agent Chatbot")
st.write("Ask a question about Segment, mParticle, Lytics, or Zeotap:")

question = st.text_input("Your question:")

if st.button("Get Answer"):
    answer = "Sorry, I couldn't understand your question. Please try again."

    # Handle specific questions
    if "set up a new source" in question.lower() and "segment" in question.lower():
        answer = fetch_segment_instructions()
    elif "create a user profile" in question.lower() and "mparticle" in question.lower():
        answer = fetch_mparticle_instructions()
    elif "build an audience segment" in question.lower() and "lytics" in question.lower():
        answer = fetch_lytics_instructions()
    elif "integrate my data" in question.lower() and "zeotap" in question.lower():
        answer = fetch_zeotap_instructions()

    st.markdown(f"**Answer:**\n{answer}")
