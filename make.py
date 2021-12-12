## python make.py abc000 でテストケースをダウンロードしてコードを書いていくファイルはsnipet.pyのコピーとする

import os
import shutil
import argparse
import subprocess

def main():
    parser = argparse.ArgumentParser()

    parser.add_argument("contestID", type=str)
    args = parser.parse_args()

    cmd = f"acc new {args.contestID}"
    proc = subprocess.Popen(cmd,
                            shell=True,
                            stdout=subprocess.PIPE,
                            stderr=subprocess.STDOUT)

    line = proc.stdout.readline()

    if str(line).split(" ")[0].lstrip("b'") != "failed":

        taskID = ["a","b","c","d","e","f"]

        for id in taskID:
            os.makedirs(f"{args.contestID}/{id}", exist_ok=True)
            shutil.copy("snipet.py", f"{args.contestID}/{id}/{id}.py")
    else:
        print(str(line).lstrip("b'").rstrip("\\n'"))
    
if __name__ == "__main__":
    main()