from pathlib import Path
import urllib.request

BASE_URL = "https://huggingface.co/microsoft/OmniParser-v2.0/resolve/main"

FILES = {
    "icon_detect": [
        "train_args.yaml",
        "model.pt",
        "model.yaml",
    ],
    "icon_caption_florence": [
        ("config.json", "icon_caption/config.json"),
        ("generation_config.json", "icon_caption/generation_config.json"),
        ("model.safetensors", "icon_caption/model.safetensors"),
    ],
}

weights_dir = Path("weights")
weights_dir.mkdir(exist_ok=True)

# icon_detect
icon_detect_dir = weights_dir / "icon_detect"
icon_detect_dir.mkdir(exist_ok=True)

for filename in FILES["icon_detect"]:
    url = f"{BASE_URL}/icon_detect/{filename}"
    dest = icon_detect_dir / filename

    print(f"Baixando {filename}...")
    urllib.request.urlretrieve(url, dest)
    print(f"OK -> {dest}")

# icon_caption -> icon_caption_florence
caption_dir = weights_dir / "icon_caption_florence"
caption_dir.mkdir(exist_ok=True)

for local_name, remote_path in FILES["icon_caption_florence"]:
    url = f"{BASE_URL}/{remote_path}"
    dest = caption_dir / local_name

    print(f"Baixando {local_name}...")
    urllib.request.urlretrieve(url, dest)
    print(f"OK -> {dest}")

print("\nDownload concluído!")