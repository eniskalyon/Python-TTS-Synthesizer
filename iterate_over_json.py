import os
import json
from ttsmms import TTS

# JSON files and corresponding directories
json_files = ['translatedBeginner.json', 'translatedIntermediate.json', 'translatedUpperIntermediate.json', 'translatedAdvanced.json']
level_dirs = ['beginner', 'intermediate', 'upperIntermediate', 'advanced']

# Directories for each language
lang_dirs = {'en': 'eng', 'fa': 'persian', 'ku': 'kurdish (sorani)', 'kmr': 'kurdish (kurmanci)', 'tr': 'turkish', 'ar': 'arabic'}

# Data paths for each language
data_paths = {'en': r'C:\Users\enisk\Desktop\tts\data\eng', 'fa': r'C:\Users\enisk\Desktop\tts\data\fas', 'ku': r'C:\Users\enisk\Desktop\tts\data\kmr-script_arabic', 'kmr': r'C:\Users\enisk\Desktop\tts\data\kmr-script_latin', 'tr': r'C:\Users\enisk\Desktop\tts\data\tur', 'ar': r'C:\Users\enisk\Desktop\tts\data\ara'}

# Base directory
base_dir = 'audios'

# Iterate over each JSON file
for json_file, level_dir in zip(json_files, level_dirs):
    # Load JSON file
    with open(json_file, 'r') as f:
        data = json.load(f)

    # For each level directory, generate and save the audio files
    for item in data[level_dir]:
        for sentence_index in item.keys():
            # Load the TTS model for English
            tts = TTS(data_paths['en'])
            
            # Sentence to be converted to speech
            text = item[sentence_index]['sentence']
            
            # Create directory if it doesn't exist
            os.makedirs(os.path.join(base_dir, 'en', level_dir), exist_ok=True)
            
            # Synthesize the speech and save the English audio file
            tts.synthesis(text, wav_path=os.path.join(base_dir, 'en', level_dir, f'{sentence_index}.wav'))

            # Then proceed with other languages
            for lang_code in data_paths.keys():
                # Skip English since we've already processed it
                if lang_code == 'en':
                    continue
                
                # Load the TTS model for the current language
                tts = TTS(data_paths[lang_code])
                
                # Sentence to be converted to speech
                text = item[sentence_index]['languages'][lang_code]['sentence']

                # Create directory if it doesn't exist
                os.makedirs(os.path.join(base_dir, lang_dirs[lang_code], level_dir), exist_ok=True)
                
                # Synthesize the speech and save the audio file
                tts.synthesis(text, wav_path=os.path.join(base_dir, lang_dirs[lang_code], level_dir, f'{sentence_index}.wav'))
