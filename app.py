from flask import Flask, request, jsonify, render_template
from langchain.llms import CTransformers
from langchain.prompts import PromptTemplate

app = Flask(__name__)

# Function to get response from the LLama model
def get_response(input_text, no_of_words, blog_style):
    llm = CTransformers(
        model="/home/kunalovish/Downloads/Blog Generator/llama-2-7b-chat.ggmlv3.q8_0.bin",
        model_type="llama",
        config={"max_new_tokens": 256, "temperature": 0.9}
    )

    # Prompt template for blog generation
    template = '''
        Write a blog about {blog_style} on {input_text} with {no_of_words} words.
    '''
    
    # Prompt template setup
    prompt_template = PromptTemplate(
        input_variables=["blog_style", "input_text", "no_of_words"],
        template=template
    )
    
    # Generate a response
    response = llm(prompt_template.format(
        blog_style=blog_style,
        input_text=input_text,
        no_of_words=no_of_words
    ))
    return response

# Homepage route to serve the HTML file
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/generate_blog', methods=['POST'])
def generate_blog():
    data = request.json
    input_text = data['input_text']
    no_of_words = data['no_of_words']
    blog_style = data['blog_style']
    
    response = get_response(input_text, no_of_words, blog_style)
    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(debug=True)
