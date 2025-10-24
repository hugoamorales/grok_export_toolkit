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
#  File: grok_to_llmexplorer.py
#  Version: 1.0.0
#  Author: Dynnovators Studio — AI Systems Division
#  Assistant: Lyra Magilla
# ─────────────────────────────────────────────────────────────

"""
Converts an xAI Grok conversation export (e.g., prod-grok-backend.json)
into a ChatGPT-compatible JSON format for use with LLM Explorer tools
such as ChatGPT Archive Viewer or LLM Chat Explorer.
"""

import json
import sys
from pathlib import Path

__version__ = "1.0.2"

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
    python3 grok_to_llmexplorer.py <input_file.json> [output_file.json]

DESCRIPTION:
    Converts a Grok export (from xAI) into a ChatGPT-compatible JSON format.
    The result can be imported into viewers like LLM Explorer, ChatGPT Archive Viewer,
    or LLM Chat Explorer.

EXAMPLES:
    python3 grok_to_llmexplorer.py prod-grok-backend.json
    python3 grok_to_llmexplorer.py input.json converted_output.json

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


def convert_grok_to_chatgpt(grok_data):
    """Converts Grok export structure to ChatGPT-style schema."""
    converted = {"conversations": []}

    for item in grok_data.get("conversations", []):
        conv = item.get("conversation", {})
        responses = item.get("responses", [])
        conv_id = conv.get("id", "unknown")
        title = conv.get("title", "Untitled Conversation")
        create_time = conv.get("create_time", "")
        date_str = str(create_time).split("T")[0] if create_time else ""

        new_conv = {
            "id": conv_id,
            "title": title,
            "create_time": date_str,
            "mapping": {},
        }

        message_counter = 0
        for r in responses:
            msg = r.get("response", {})
            if not msg:
                continue

            sender = msg.get("sender", "unknown").lower()
            role = "user" if sender == "human" else "assistant"
            content = msg.get("message", "").strip()
            message_id = f"{conv_id}-{message_counter}"

            new_conv["mapping"][message_id] = {
                "id": message_id,
                "message": {
                    "author": {"role": role},
                    "create_time": msg.get("create_time", {}).get("$date", {}).get("$numberLong", ""),
                    "content": {"parts": [content]},
                },
            }
            message_counter += 1

        converted["conversations"].append(new_conv)

    return converted


def main():
    if len(sys.argv) < 2 or sys.argv[1] in ("-h", "--help"):
        print(HELP_TEXT)
        sys.exit(0)

    input_path = Path(sys.argv[1])
    output_path = Path(sys.argv[2]) if len(sys.argv) > 2 else input_path.with_name("grok_converted_for_llmexplorer.json")

    print(BANNER)
    print(f"📂 Loading Grok export: {input_path}")

    grok_data = load_json(input_path)
    print("🔄 Converting to ChatGPT-compatible schema...")

    converted = convert_grok_to_chatgpt(grok_data)

    print(f"💾 Saving output to: {output_path}")
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(converted, f, indent=2, ensure_ascii=False)

    print("✅ Conversion complete! You can now import this file into your LLM viewer.")
    print("──────────────────────────────────────────────")


if __name__ == "__main__":
    main()
