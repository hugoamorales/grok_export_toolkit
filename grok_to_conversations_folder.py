#!/usr/bin/env python3
# ─────────────────────────────────────────────────────────────
#  Dynnovators presents:
#  The Grok Export Toolkit v1.0.0
#  © 2025 Dynnovators Studio — MIT License
#  Website: https://dynnovators.com
#  Contact: hello@dynnovators.com
#  Grok™ is a registered trademark of xAI Corp.
#  This is an independent, open-source utility
#  not affiliated with or endorsed by xAI.
# ─────────────────────────────────────────────────────────────
#  File: grok_to_conversations_folder.py
#  Version: 1.0.0
#  Author: Dynnovators Studio — AI Systems Division
#  Assistant: Lyra Magilla
# ─────────────────────────────────────────────────────────────

"""
Splits an xAI Grok backend export (e.g., prod-grok-backend.json)
into individual JSON files per conversation, ready for use with
LLM Chat Explorer or similar tools. Generates an INDEX.json summary.
"""

import json
import sys
from pathlib import Path

__version__ = "1.0.0"

BANNER = f"""
──────────────────────────────────────────────
Dynnovators presents:
The Grok Export Toolkit v{__version__}
© 2025 Dynnovators Studio
https://dynnovators.com | hello@dynnovators.com
──────────────────────────────────────────────
Grok™ is a registered trademark of xAI Corp.
This tool is an independent, open-source utility.
──────────────────────────────────────────────
"""

HELP_TEXT = f"""{BANNER}
USAGE:
    python3 grok_to_conversations_folder.py <input_file.json> [output_folder]

DESCRIPTION:
    Splits an xAI Grok export into individual JSON conversation files,
    creating a structured folder and an INDEX.json summary file.

EXAMPLES:
    python3 grok_to_conversations_folder.py prod-grok-backend.json
    python3 grok_to_conversations_folder.py input.json ./exports/

VERSION:
    {__version__}
"""


def load_json(path: Path):
    """Loads a JSON file safely."""
    try:
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"❌ Error: File not found -> {path}")
        sys.exit(1)
    except json.JSONDecodeError as e:
        print(f"❌ Error: Invalid JSON format in {path}: {e}")
        sys.exit(1)


def sanitize_filename(name: str) -> str:
    """Cleans conversation titles for safe filenames."""
    invalid_chars = '<>:"/\\|?*'
    for ch in invalid_chars:
        name = name.replace(ch, "_")
    return name.strip().replace(" ", "_")


def save_conversation(conv: dict, responses: list, output_dir: Path):
    """Saves a single conversation as JSON."""
    conv_id = conv.get("id", "unknown")
    title = conv.get("title", f"Conversation_{conv_id}")
    filename = f"{sanitize_filename(title)}.json"
    path = output_dir / filename

    export_data = {
        "conversation_id": conv_id,
        "title": title,
        "create_time": conv.get("create_time", ""),
        "responses": responses,
    }

    with open(path, "w", encoding="utf-8") as f:
        json.dump(export_data, f, indent=2, ensure_ascii=False)

    return {"id": conv_id, "title": title, "file": filename, "messages": len(responses)}


def main():
    if len(sys.argv) < 2 or sys.argv[1] in ("-h", "--help"):
        print(HELP_TEXT)
        sys.exit(0)

    input_path = Path(sys.argv[1])
    output_dir = Path(sys.argv[2]) if len(sys.argv) > 2 else input_path.parent / "grok_conversations_exported"

    print(BANNER)
    print(f"📂 Loading Grok export: {input_path}")

    grok_data = load_json(input_path)

    output_dir.mkdir(parents=True, exist_ok=True)
    print("🔄 Splitting into individual conversations...")

    index = []
    for item in grok_data.get("conversations", []):
        conv = item.get("conversation", {})
        responses = item.get("responses", [])
        meta = save_conversation(conv, responses, output_dir)
        index.append(meta)

    index_path = output_dir / "INDEX.json"
    with open(index_path, "w", encoding="utf-8") as f:
        json.dump(index, f, indent=2, ensure_ascii=False)

    print(f"✅ Export complete! {len(index)} conversations saved in: {output_dir}")
    print("🗂️ Index file created: INDEX.json")
    print("──────────────────────────────────────────────")


if __name__ == "__main__":
    main()
