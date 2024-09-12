from langchain.llms import CTransformers
import streamlit as st
# from langchain_community import CTransformers
from langchain_community.llms import CTransformers
from langchain.prompts import PromptTemplate

# creating a function to get a response from LLama 2 model
def get_response(input_text, no_of_words, blog_style):

    # llm = CTransformers(model="model\llama-2-7b-chat.ggmlv3.q8_0.bin", model_type="llama")

    # calling LLama model which we downloaded from Hugging Face using CTransformers
    llm = CTransformers(model="/home/kunalovish/Downloads/Blog Generator/llama-2-7b-chat.ggmlv3.q8_0.bin",
                        model_type="llama",
                        config={"max_new_tokens": 256,"temperature": 0.9})

    # creating a prompt template
    template = '''
            Write a blog about {blog_style} on {input_text} with {no_of_words} words.
            '''
    
    # creating a prompt template
    prompt_template = PromptTemplate(input_variables=["blog_style", "input_text", "no_of_words"],
                                     template=template)
    
    # generate a response from LLama model
    response=llm(prompt_template.format(blog_style=blog_style,input_text=input_text,no_of_words=no_of_words))
    print(response)
    return response


