import argparse
import os
from typing import List

parser = argparse.ArgumentParser()
parser.add_argument("chapter", type=int)
chapter = parser.parse_args().chapter

if chapter >= 4:
    os.system("cp overwrite/build-elf.rs ../os/build.rs")
else:
    os.system("cp overwrite/build-bin.rs ../os/build.rs")

if chapter <= 6:
    os.system("cp overwrite/Makefile-ch3 ../os/Makefile")
else:
    os.system("cp overwrite/Makefile-ch7 ../os/Makefile")
if chapter == 7:
    os.system("cp overwrite/easy-fs-fuse.rs ../easy-fs-fuse/src/main.rs")

def do_replace(lines: List[str]):
    for line in lines:
        line.replace(' git = "https://github.com/rcore-os/riscv"', 'path = "../user/riscv"')

with open("../os/Cargo.toml", 'w+') as f:
    lines = f.readlines()
    for line in lines:
        line.replace(' git = "https://github.com/rcore-os/riscv"', ' path = "../user/riscv" ')
    f.writelines(lines)