from fastapi import FastAPI
import streamlit as st
import subprocess
import streamlit
import re
import sys
from streamlit.cli import _main_run

app = FastAPI()
st.write("hello")

if __name__ == "__main__":
    subprocess.call("uvicorn run main:app --reload")
    file_path = 'main.py'
    args = ['streamlit', 'run', file_path]
    _main_run(args)