'''Demonstration of Tweet Generator'''
import gradio as gr
from tweet_generator import generate_tweet
def create_tweet(topics,hastags,tone,style):
    '''Return the generated tweet'''
    tweet=generate_tweet(topics=topics,hastags=hastags,tone=tone,style=style)
    return tweet

demo = gr.Interface(
  fn=create_tweet, 
  inputs=[
    gr.Textbox(
    placeholder="Please enters the topics separated by commas",
      label="Topics",
      info="Generate a Tweet based on the following Topics"
  ),
  gr.Textbox(
    label="#hastags",
    placeholder="Please enter the hastags you want in this Tweet",
    info="These hastags will be part of the Tweet"
  ),
  gr.Textbox(
    label="Tone",
    placeholder="What should be the tone of the Tweet??",
    info="Setting the tone helps tweet convey right meaning"
  ),
  gr.Textbox(
    label="Style",
    placeholder="What Style do you want the Tweet to be in ?? - Informal, humurous, etc"
  )], 
  outputs=gr.Textbox(
    show_copy_button=True
  )
)
demo.launch(share=True)
