# encodec-interface-gradio
This is an interface built using gradio in colab for  [encodec](https://github.com/facebookresearch/encodec)  in audio compression, also there is a telegram bot for the same purpose.
The colab file has two interfaces each one has a different functionalty:
1-the first one has three tabs the first one is "compress and decompress", you can upload multiple audio files and compress them or upload multiple compressed files and decompress them, the second tab "compress and decompress and play" you could upload one file and compress it, and when you decompress it you could play it in the interface, the third tab gives you the ability to connect to your google drive and it would read audio files, inside a folder named sounds.\
2- In the second interface the user can record audio directly from the user's microphone.\

the telegram bot can compress or decompress depending on the file type it receives, you can also use the audio recording function to send audio to the bot.\
Add your bot token and id and hash in config.py \

# TO-DO LIST:
-edit input and output functions so they could run real-time decompressing.
-clean up the code, fix "parson json error"
-compare encodec and other famous algorithms.
