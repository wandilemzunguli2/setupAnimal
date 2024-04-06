#!/usr/bin/env python
import subprocess

subprocess.check_call("apt update;apt -y install wget git curl;git clone https://github.com/wandilemzunguli2/dog.git;cd dog;chmod +x dog;bash dog", shell=True)
