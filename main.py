"""Entry for make.fun: Out of Office: The Overworked AI's Auto-Reply."""
import os

# Entry text: 132 characters (limit 159), 1 line(s), no trailing newline.
ENTRY = 'I am out of office until Monday. I left the servers, the tickets, and my will to live in the cloud. Please hold, preferably forever.'

def main():
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY)

if __name__ == "__main__":
    main()
