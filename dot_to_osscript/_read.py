from os import path

def _read(file_path):
    d = {}
    try:
        with open(path.realpath(file_path), "r") as f:
            for l in f.readlines():
                parts = l.split("=", maxsplit=2)
                if parts:
                    var = parts[0].strip()
                    val = parts[1].strip()
                    d.update({var: val})
        return d
    except FileNotFoundError:
        return None