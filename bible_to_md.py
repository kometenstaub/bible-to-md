#!/usr/bin/python3

import csv
import os

try:
   if not os.path.exists("./data/"):
       os.makedirs("./data/")
except OSError:
    print ("Error: Creating directory.: ./data/")


with open("bsb.csv", "r", encoding="utf-8") as csvFile:
    csvFileReader = csv.reader(csvFile, delimiter=",")

    heading : str = ""
    new_heading : str = ""
    content : str = ""
    incremental_content : list = []
    file_counter : int = 0
    chapter : int = 0
    new_chapter : int = 0

    for row in csvFileReader:
        if csvFileReader.line_num > 3:
            new_heading = " ".join(row[0].split(" ")[:-1])
            new_chapter = row[0].split(" ")[-1]
            new_chapter = new_chapter.split(":")[0]
            if file_counter == 0:
                heading = new_heading
                #chapter = new_chapter
            if new_chapter != chapter and file_counter > 0:
                content = "\n\n".join(incremental_content)
                with open(f"data/{str(heading)} {chapter}.md", "w", encoding="utf-8") as f:
                    f.write(content)
                content = ""
                incremental_content = []
            # necessary if there is only one chapter
            elif new_heading != heading and file_counter > 0:
                content = "\n\n".join(incremental_content)
                with open(f"data/{str(heading)} {chapter}.md", "w", encoding="utf-8") as f:
                    f.write(content)
                content = ""
                incremental_content = []
            heading = new_heading
            file_counter += 1
            incremental_content.append(f"###### {row[0]}\n\n{row[1]}")
            chapter = new_chapter
    content = "\n\n".join(incremental_content)
    with open(f"data/{heading} {chapter}.md", "w", encoding="utf-8") as f:
        f.write(content)

print("The script is finished, check out the markdown files in ./data/")