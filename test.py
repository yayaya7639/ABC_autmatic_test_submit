## python test.py abc000 a でabc000のa.pyをテストケースに通して全部OKならsubmitする

import os
import sys
import argparse
import subprocess

def main():
    parser = argparse.ArgumentParser()

    parser.add_argument("contestID", type=str)
    parser.add_argument("task", type=str)
    args = parser.parse_args()

    cmd = f"oj t -c 'python3 {args.contestID}/{args.task}/{args.task}.py' -d {args.contestID}/{args.task}/tests"
    subprocess.run(cmd, shell=True)
    proc = subprocess.Popen(cmd,
                            shell=True,
                            stdout=subprocess.PIPE,
                            stderr=subprocess.STDOUT)
    
    end_output = ""
    while True:
        line = proc.stdout.readline()

        if proc.poll() is not None:
            break
        end_output = line
    
    if str(end_output).split(" ")[0].lstrip("b'") == "[SUCCESS]":
        print("success!! submitting...")
        os.chdir(f"./{args.contestID}/{args.task}")
        cmd = f"acc submit {args.task}.py"
        subprocess.run(cmd, shell=True)
    else:
        print("failed... you can not submit")

if __name__ == "__main__":
    main()