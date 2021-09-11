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

    for row in csvFileReader:
        #print(row)
        new_heading = " ".join(row[0].split(" ")[:-1])
        #content = "\n\n".join(incremental_content)
        incremental_content.append(f"###### {row[0]}\n\n{row[1]}")
        # this is never true
        if new_heading != heading:
            content = "\n\n".join(incremental_content)
            with open(f"data/{str(new_heading)}.md", "w", encoding="utf-8") as f:
                f.write(content)
            file_counter += 1
            content = ""
            incremental_content = []
        heading = new_heading
        #incremental_content.append(f"###### {row[0]}\n\n{row[1]}")
    content = "\n\n".join(incremental_content)
    with open(f"data/{new_heading}.md", "w", encoding="utf-8") as f:
        f.write(content)

