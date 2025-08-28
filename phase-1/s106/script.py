import glob, subprocess, os.path, time

for image in sorted(glob.glob("page-*.png")):
    out = image.replace(".png", ".md")
    if os.path.exists(out):
        continue
    text = subprocess.check_output(
        [
            "llm",
            "prompt",
            "-a",
            image,
            "extract the text from this pdf. use markdown formatting. do not say anything else, or surround your output with a code block.",
        ],
        encoding="utf8",
    )
    open(out, "w").write(text)
    print(f'processed {image}')
    time.sleep(5)
