import os

mp3files = [x for x in os.listdir("clips") if x.endswith(".mp3")]

print(mp3files)

for f in mp3files:
	f_id = f.replace(" ", "_").replace(".mp3","")
	f_txt = f.replace(".mp3","")
	print("<div id='" + f_id + "' class='text_container' onclick='play(this.id)'>" + f_txt + "</div>")

for f in mp3files:
	f_audio_id = f.replace(" ", "_").replace(".mp3","") + "_audio"
	f_src = f
	print("<audio id='" + f_audio_id +"' src='" + f_src + "'></audio>")
