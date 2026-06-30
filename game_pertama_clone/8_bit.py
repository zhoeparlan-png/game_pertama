from pydub import AudioSegment

# 1. Load lagu aslinya
song = AudioSegment.from_file("hellfire.mp3", format="mp3")

# 2. Turunin Sample Rate (Biar suaranya pecah khas retro)
# 8000Hz itu standar telepon lama / game jadul
song_8bit = song.set_frame_rate(8000)

# 3. Ubah jadi Mono (biar makin ringan di RAM)
song_8bit = song_8bit.set_channels(1)

# 4. Export jadi file baru
song_8bit.export("hellfire_8bit.wav", format="wav")

print("GACOR! Musik 8-bit lu udah jadi: hellfire_8bit.wav")