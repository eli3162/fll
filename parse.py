import os, sys, textwrap
from pathlib import Path
from collections import deque

def parse(data):
    marker = "#path.fll-DATA"

    idx = data.find(marker)
    if idx != -1:
        data = data[:idx].rstrip("\r\n")

    data = data.replace("#PATH-POINTS-START Path", "")

    data = str(data)

    lines = data.splitlines()

    lines = [ln for ln in lines if ln.strip() != ""]

    wrapped = []
    for i, ln in enumerate(lines):
        parts = [p.strip() for p in ln.split(',') if p.strip() != '']
        if len(parts) > 3:
            parts = parts[:3]
        if len(parts) >= 3:
            try:
                v = float(parts[2])
                v = v / 120.0
                if v.is_integer():
                    parts[2] = str(int(v))
                else:
                    parts[2] = ('%f' % v).rstrip('0').rstrip('.')
            except Exception:
                pass
        elem_content = ','.join(parts)
        elem = '[' + elem_content + ']'
        if i != len(lines) - 1:
            elem += ','
        wrapped.append(elem)

    data = textwrap.indent("\n".join(wrapped), "    ")

    data = '[\n' + data + '\n]'

    data = textwrap.indent(data, "    ")

    data = '{"path": ' + '\n' + data + '\n}'
    return data

