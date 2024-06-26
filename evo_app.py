"""
All code contributed to Wordlit.net is © 2024 by Esteban Pérez. 
The content is licensed under the Creative Commons Attribution 4.0 International License. 
This allows for sharing and adaptation, provided appropriate credit is given, and any changes made are indicated.

When using the code from Wordlit.net, please credit as follows: "Code sourced from Wordlit.net, authored by Esteban Pérez, 2024."

For reporting bugs, requesting features, or further inquiries, please reach out to Esteban Pérez at estebanpbuday@outlook.com
"""

import streamlit as st
from openai import OpenAI
import pymupdf
import os

# App title
st.set_page_config(page_title="Hackathon - The Future of AI is Open",
                   menu_items={
                       'About': "This is a demo app for the Hackathon - **The Future of AI is Open**"
                   }
)

def main():
    st.title("Wordlit.net")
    st.markdown(
        """
        This tool uses NLP to generate a knowledge graph from the text you provide.\n
        Enter any text or upload a file and hit the '**Generate**' button to visualize the connections between entities.
        
        All code contributed by [Sahir Maharaj](%s) is licensed under Attribution 4.0 International
        """
    )

if __name__ == "__main__":
    main()