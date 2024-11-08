import gradio as gr
import utils.main as my

def download_article(article_content):
    # Save the article to a file and return the file path for download
    file_path = "generated_article.txt"
    with open(file_path, "w") as file:
        file.write(article_content)
    return file_path

with gr.Blocks() as demo:
    gr.Markdown("# Auto-Article: Convert YouTube Transcripts into SEO-Friendly Content with Gradio")

    youtube_link = gr.Textbox(label="YouTube Video Link", placeholder="Enter the YouTube video link here")
    tone = gr.Dropdown(choices=["Casual", "Professional", "Academic", "Creative"], label="Select Tone")

    submit_btn = gr.Button("Submit")

    output = gr.Markdown(label="Generated Article")
    download_btn = gr.Button("Download Article")

    submit_btn.click(fn=my.get_output, inputs=[youtube_link,tone], outputs=output)
    download_btn.click(fn=download_article, inputs=output, outputs=gr.File(label="Download Article"))

# Run the Gradio app
demo.launch()
