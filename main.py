import os

import openai
import whisper
import pandas as pd
from pytube import YouTube
import csv

with gr.Blocks() as demo:
    txt = gr.Textbox(label="Input", lines=5)
    txt_2 = gr.Textbox(label="Output")
    txt_3 = gr.Textbox(str, label="Output", interactive=False)
    btn = gr.Button("Submit")
    btn_clear = gr.Button("Clear")


    def clear_text():
        return txt.update(value='')


    btn.click(lambda a: a, inputs=[txt], outputs=[txt_2])
    btn_clear.click(clear_text, inputs=[], outputs=[txt])

demo.launch()















#openai.api_key = "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"
#COMPLETIONS_MODEL = "text-davinci-003"
#EMBEDDINGS_MODEL = "text-embedding-ada-002"

#model = whisper.load_model('base')
youtube_video_url = "https://www.youtube.com/watch?v=p7nueyk4EiE"
youtube_video = YouTube(youtube_video_url)

stream = youtube_video.streams.filter(only_audio=True).first()
stream.download(filename='xqc5.mp4')


#output = model.transcribe("C:/Users/gavin/PycharmProjects/PodcastAI/")

#df= pd.DataFrame(columns=['episode','URL','start_timestamp','start','end','question','context'])
#
# i=0
#
# with open('All_In.csv') as csv_file:
#     reader = csv.reader(csv_file)
#
#     # skip the header row in the csv file
#     next(reader)
#
#     for row in reader:
#         # assign each column in the row to a variable and split questions on carriage return
#         episode, url, questions = row
#         question_list = questions.split("\n")
#
#         # for each question in the list, extract the timestamp and convert it to seconds for youtube
#         for question in question_list:
#             pieces = question.split('-')
#             timestamp = pieces[0]
#             minutes, seconds = timestamp.split(':')
#             seconds = int(seconds) + (int(minutes.lstrip()) * 60)
#
#
#             # add a new row to the dataframe
#             df.loc[i] = [episode, url, timestamp, seconds, seconds, " ".join(pieces[1:]), ""]
#
#             try:
#                 df.loc[i - 1, 'end'] = df.loc[i, 'start']
#             except:
#                 print(f"skipping row {i} because there is no previous row")
#             i += 1
#
#             df['end'][df['end'] < df['start']] = 0
# df.to_csv("questions.csv")

# df2 = pd.read_csv('questions.csv')
# x=0
# for links in df2["URL"].unique():
#     youtube_video_url = links
#     youtube_video = YouTube(youtube_video_url)
#
#     stream = youtube_video.streams.filter(only_audio=True).first()
#     stream.download(filename=f"video{x}.mp4")
#
#     x += 1
# video_files = os.listdir("C:/Users/gavin/PycharmProjects/PodcastAI/videos")
#
# for video_file in video_files:
#     video_path = "C:/Users/gavin/PycharmProjects/PodcastAI/videos/"+ video_file
#     result = model.transcribe(video_path)
#     text = result["text"].strip()
#     text_file = video_file[:-4] +".txt"
#     text_path = "C:/Users/gavin/PycharmProjects/PodcastAI/videos/" +text_file
#     with open(text_path, "w") as f:
#         f.write(text)
#
#     print(f"Processed {video_file} and saved transcription")

# video_files = os.listdir("C:/Users/gavin/PycharmProjects/PodcastAI/videos")
# for video_file in video_files:
#     video_path = "C:/Users/gavin/PycharmProjects/PodcastAI/videos/"+ video_file
#     print(video_path)

#output = model.transcribe("C:/Users/gavin/PycharmProjects/PodcastAI/videos")




