# Grok Export Toolkit

[![GitHub release (latest by date)](https://img.shields.io/github/v/release/hugoamorales/grok_export_toolkit?logo=github)](https://github.com/hugoamorales/grok_export_toolkit/releases/latest)
[![GitHub all releases](https://img.shields.io/github/downloads/hugoamorales/grok_export_toolkit/total?logo=github)](https://github.com/hugoamorales/grok_export_toolkit/releases)
[![GitHub license](https://img.shields.io/github/license/hugoamorales/grok_export_toolkit)](https://github.com/hugoamorales/grok_export_toolkit/blob/main/LICENSE)
[![Maintenance](https://img.shields.io/maintenance/yes/2025?color=brightgreen)](https://github.com/hugoamorales/grok_export_toolkit/commits/main)
[![GitHub contributors](https://img.shields.io/github/contributors/hugoamorales/grok_export_toolkit)](https://github.com/hugoamorales/grok_export_toolkit/graphs/contributors)
[![Made with JavaScript](https://img.shields.io/badge/Made%20with-Python-blue)](#)

### © 2025 Dynnovators Studio — MIT License  
**Dynnovators Studio, a Personal Brand of Hugo Morales**  
**Prepared by Dynnovators Studio — AI Systems Division**  
*Assistant: Lyra Magilla*  
🌐 [https://dynnovators.com](https://dynnovators.com) · ✉️ hello@dynnovators.com

---

## 🧠 Overview

The **Grok Export Toolkit** is an independent open-source utility designed to transform, clean, and organize **xAI Grok™ conversation exports** into readable, structured formats.

It provides two command-line tools to help developers, analysts, and researchers navigate Grok conversation archives and convert them into formats compatible with visualization or data-processing tools such as **LLM Chat Explorer**, **ChatGPT Archive Viewer**, or custom JSON pipelines.

> ⚠️ *This project is not affiliated with xAI. “Grok” is a registered trademark of xAI Corp.*

---

## ⚙️ Features

- Convert Grok exports (`prod-grok-backend.json`) into ChatGPT-compatible format.  
- Split a full Grok export into **individual conversation files**.  
- Generate an **index file** (`INDEX.json`) summarizing all conversations.  
- Add clear CLI help, version information, and user-friendly error messages.  
- 100% offline — no API keys, no dependencies beyond Python 3.8+.  

---

## 📦 Installation

No dependencies required.

```bash
git clone https://github.com/dynnovators/grok-export-toolkit.git
cd grok-export-toolkit
```

---

## 🧩 Included Tools

### 1️⃣ `grok_to_llmexplorer.py`

**Purpose:**  
Converts an entire Grok backend export into a single file compatible with LLM viewers (e.g., ChatGPT Archive Viewer, LLM Chat Explorer).

**Usage:**
```bash
python3 grok_to_llmexplorer.py prod-grok-backend.json
```

**Output:**
```
grok_converted_for_llmexplorer.json
```

---

### 2️⃣ `grok_to_conversations_folder.py`

**Purpose:**  
Split a Grok export into a folder of JSON files, one per conversation, plus an index.

**Usage:**
```bash
python3 grok_to_conversations_folder.py prod-grok-backend.json
```

**Output Structure:**
```
./grok_conversations_exported/
├── Conversation_1.json
├── Conversation_2.json
├── ...
└── INDEX.json
```

---

## 🧾 Example

Run the following command in your export directory:

```bash
python3 grok_to_conversations_folder.py prod-grok-backend.json
```

Expected console output:

```
──────────────────────────────────────────────
Dynnovators presents:
The Grok Export Toolkit v1.0.0
© 2025 Dynnovators Studio
──────────────────────────────────────────────
📂 Loading Grok export: prod-grok-backend.json
🔄 Splitting into individual conversations...
✅ Export complete! 5 conversations saved in: ./grok_conversations_exported
🗂️ Index file created: INDEX.json
──────────────────────────────────────────────
Grok is a registered trademark of xAI.
This tool is an independent, open-source utility.
──────────────────────────────────────────────
```

---

## 🧰 File Structure

```
grok-export-toolkit/
│
├── LICENSE
├── README.md
├── CHANGELOG.md
├── pyproject.toml
├── setup.cfg
├── grok_to_llmexplorer.py
└── grok_to_conversations_folder.py

```

---

## 🧾 Changelog

See [`CHANGELOG.md`](CHANGELOG.md) for version history and updates.

---

## ⚖️ License

This project is distributed under the **MIT License**.  
See [`LICENSE`](LICENSE) for details.  
© 2025 Dynnovators Studio. All rights reserved.

---

## 🙏 Acknowledgments

- **xAI** for developing *Grok*, whose export format inspired this toolkit.  
- **levysogt (Antonio)** for creating [LLM Chat Explorer](https://github.com/levysoft/llm-chat-explorer),  
  the visualization tool that inspired and validated this conversion format.  
- **OpenAI**, **Anthropic**, and the wider LLM community for setting the foundation for structured AI dialogue analysis.  
- Built with care by **Dynnovators Studio**, the personal brand of **Hugo Morales**,  
  to empower creators, researchers, and developers exploring the frontier between AI and human narrative.

---

> *“Code is memory, structure is story.”* — Dynnovators Studio
