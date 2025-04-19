import json

def format_timestamp(seconds):
    h = int(seconds // 3600)
    m = int((seconds % 3600) // 60)
    s = int(seconds % 60)
    ms = int((seconds - int(seconds)) * 1000)
    return f"{h:02}:{m:02}:{s:02},{ms:03}"

def json_to_srt(json_path, srt_path):
    with open(json_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    segments = data["segments"]
    srt_lines = []

    for i, segment in enumerate(segments):
        start = format_timestamp(segment["start"])
        end = format_timestamp(segment["end"])
        
        # Either full segment text:
        text = segment["text"].strip()

        # OR word-by-word version (uncomment below to use it)
        # words = segment.get("words", [])
        # text = " ".join([w["word"] for w in words if "start" in w])

        srt_lines.append(f"{i+1}")
        srt_lines.append(f"{start} --> {end}")
        srt_lines.append(text)
        srt_lines.append("")

    with open(srt_path, 'w', encoding='utf-8') as f:
        f.write("\n".join(srt_lines))

    print(f"SRT file saved to: {srt_path}")
    
def word_level_json_to_srt(json_path, srt_path):
    with open(json_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    words = data.get("word_segments", [])
    srt_lines = []

    index = 1
    for word in words:
        if "start" in word and "end" in word:
            start = format_timestamp(word["start"])
            end = format_timestamp(word["end"])
            text = word["word"].strip()

            srt_lines.append(str(index))
            srt_lines.append(f"{start} --> {end}")
            srt_lines.append(text)
            srt_lines.append("")
            index += 1

    with open(srt_path, "w", encoding="utf-8") as f:
        f.write("\n".join(srt_lines))

    print(f"✅ Word-level SRT saved to: {srt_path}")
    
    
def word_level_json_to_srt2(json_path, srt_path, nb_words: int = 2):
    with open(json_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    words = [w for w in data.get("word_segments", []) if "start" in w and "end" in w]
    srt_lines: List[str] = []

    index = 1
    for i in range(0, len(words), nb_words):
        chunk = words[i:i + nb_words]
        start = format_timestamp(chunk[0]["start"])
        end = format_timestamp(chunk[-1]["end"])
        text = " ".join(w["word"].strip() for w in chunk)

        srt_lines.append(str(index))
        srt_lines.append(f"{start} --> {end}")
        srt_lines.append(text)
        srt_lines.append("")
        index += 1

    with open(srt_path, "w", encoding="utf-8") as f:
        f.write("\n".join(srt_lines))

    print(f"✅ Grouped word-level SRT saved to: {srt_path}")
# Example usage:
word_level_json_to_srt2("output2/poison.json", "output2/subwd2.srt")