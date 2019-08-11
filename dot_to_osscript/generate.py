import re
from os import path, environ
from ._read import _read
from ._write import _write


def _concat_values(value_a, value_b, unix_var=True):
    """

    Parameters
    ----------
    value_a : str
    value_b : str
    unix_var : bool

    Returns
    -------
    str
    """
    if unix_var:
        return value_a + ":" + value_b
    else:
        return value_a + ";" + value_b


def _alias_sh(_dict):
    """
    Parameters
    ----------
    _dict : dict
    """
    text = ""
    for k, v in _dict.items():
        text += "alias " + k + " = \'" + v + "'\n"
    return text


def _alias_ps(_dict):
    """
    Parameters
    ----------
    _dict : dict
    """
    text = ""
    for k, v in _dict.items():
        text += "Set-Alias" + \
                " -Name \'" + k + "\'" + \
                " -Value \'" + v + "\'\n"
    return text


def _env_sh(_dict, path_append=True):
    """
    Parameters
    ----------
    _dict : dict

    Returns
    -------
    str
    """
    text = ""
    for k, v in _dict.items():
        if path_append and k == "PATH":
            text += k + "=\'" + "$PATH:" + v + "'\n"
        else:
            text += k + "=\'" + v + "'\n"
    return text


def _env_ps(_dict, path_append=True):
    """
    Parameters
    ----------
    _dict : dict

    Returns
    -------
    str
    """
    text = ""
    for k, v in _dict.items():
        if path_append and re.search('path', k, re.IGNORECASE):
            text += "Set-Variable" + \
                    " -Name \'" + "Path" + "\'" + \
                    " -Value \'" + "$env:Path;" + v + "\'\n"
        else:
            text += "Set-Variable" + \
                    " -Name \'" + k + "\'" + \
                    " -Value \'" + v + "\'\n"

    return text


def dotenv(_dir=".", ps=False, sh=False):
    d = _read(path.join(_dir, ".env"))
    if d:
        if ps:
            _write(
                path.join(path.dirname(_dir), ".env.ps1"),
                _env_ps(d))
        if sh:
            _write(
                path.join(path.dirname(_dir), ".env.sh"),
                _env_sh(d))


def dotalias(_dir=".", ps=False, sh=False):
    d = _read(path.join(_dir, ".alias"))
    if d:
        if ps:
            _write(
                path.join(path.dirname(_dir), ".alias.ps1"),
                _alias_ps(d))
        if sh:
            _write(
                path.join(path.dirname(_dir), ".alias.sh"),
                _alias_sh(d))
