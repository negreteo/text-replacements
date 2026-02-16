import os

# Your specific replacements
replacements = {
    'á': 'a', 'é': 'e', 'í': 'i', 'ó': 'o', 'ú': 'u',
    '¡': 'A', '¿': '', '{\\an8}': '', 'Ì': 'i', '·': 'a',
    'Ò': 'n', 'øt˙': '', 'ø': '', 'È': 'e', 'Û': 'o',
    '°': '', '˙': 'u', '∫': '', '…': 'E', '<i>': '', '</i>': ''
}

input_folder = 'source_files'
output_folder = 'updated_files'

if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Supported extensions - you can add more to this list
valid_extensions = ('.srt', '.txt', '.vtt')

files_processed = 0

for filename in os.listdir(input_folder):
    if filename.lower().endswith(valid_extensions):
        file_path = os.path.join(input_folder, filename)
        content = None

        # --- ENCODING STRATEGY ---
        # Try UTF-8 first, fall back to Latin-1 if it fails
        for encoding_type in ['utf-8-sig', 'latin-1']:
            try:
                with open(file_path, 'r', encoding=encoding_type) as f:
                    content = f.read()
                break # If successful, stop trying encodings
            except UnicodeDecodeError:
                continue

        if content is None:
            print(f"Skipping {filename}: Unknown encoding.")
            continue

        # Apply replacements
        for old, new in replacements.items():
            content = content.replace(old, new)

        # Save the new version as clean UTF-8
        output_path = os.path.join(output_folder, filename)
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(content)

        print(f"Successfully cleaned: {filename}")
        files_processed += 1

print(f"\nDone! {files_processed} files are waiting for you in '{output_folder}'.")