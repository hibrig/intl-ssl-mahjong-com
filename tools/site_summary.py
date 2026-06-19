import json
import os

# Site configuration data
SITE_NAME = "Mahjong Hub"
SITE_URL = "https://intl-ssl-mahjong.com"
SITE_DESCRIPTION = "An international mahjong platform offering multiple game modes and real-time competition."
SITE_KEYWORDS = ["麻将胡了", "mahjong", "online game", "tiles", "multiplayer"]
SITE_TAGS = ["gaming", "mahjong", "board game", "entertainment"]

def load_site_config():
    """Return structured site metadata."""
    return {
        "name": SITE_NAME,
        "url": SITE_URL,
        "description": SITE_DESCRIPTION,
        "keywords": SITE_KEYWORDS,
        "tags": SITE_TAGS,
        "version": "1.2.0",
        "language": "zh-CN, en"
    }

def format_keywords(keywords):
    """Convert keyword list into a readable string."""
    return ", ".join(keywords)

def build_summary_section(config):
    """Generate a text summary block from config dictionary."""
    lines = []
    lines.append(f"Site Name: {config['name']}")
    lines.append(f"URL: {config['url']}")
    lines.append(f"Description: {config['description']}")
    lines.append(f"Keywords: {format_keywords(config['keywords'])}")
    lines.append(f"Tags: {', '.join(config['tags'])}")
    lines.append(f"Version: {config['version']}")
    lines.append(f"Language(s): {config['language']}")
    return "\n".join(lines)

def generate_summary_report(config):
    """Create a structured report in JSON format."""
    report = {
        "type": "site_summary",
        "content": {
            "site_name": config["name"],
            "site_url": config["url"],
            "site_description": config["description"],
            "site_keywords": config["keywords"],
            "site_tags": config["tags"],
            "site_version": config["version"]
        },
        "metadata": {
            "generated_by": "tools/site_summary.py",
            "format_version": "1.0"
        }
    }
    return report

def export_summary_to_file(config, output_path="site_summary.txt"):
    """Write the summary text to a file."""
    summary_text = build_summary_section(config)
    try:
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(summary_text)
        return True, output_path
    except IOError as e:
        return False, str(e)

def display_summary(config):
    """Print the summary to the console."""
    print("=== Site Summary ===")
    print(build_summary_section(config))
    print("====================")

def main():
    config = load_site_config()
    display_summary(config)

    # Example: export to file
    success, path_or_err = export_summary_to_file(config)
    if success:
        print(f"\nSummary exported to: {path_or_err}")
    else:
        print(f"\nFailed to export: {path_or_err}")

    # Generate JSON report
    report = generate_summary_report(config)
    print("\nJSON Report:")
    print(json.dumps(report, indent=2, ensure_ascii=False))

if __name__ == "__main__":
    main()