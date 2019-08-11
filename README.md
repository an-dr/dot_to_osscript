# dot_to_osscript
Generate script based on .env and .var files, so it could be imported to the current process

## Usage
Usage: `python -m dot_to_osscript [OPTIONS]`

Options:
  `-p`, `--powershell`     Generate .env.ps1
  `-s`, `--shell`          Generate .env.sh
  `-e`, `--env-file TEXT`  Input file  [default: ./.env]
  `-a`, `--path-append`    Appent to existing Path variable

## Example
A typical usage bellow

1. We have some directory (./) with `.env` file:

```
MSYSTEM=mingw32
TEST_var="TEST VAL"
PATH=/my_app/bin
```

2. We execute:

`python -m dot_to_osscript -psa`

and get

.env.ps1:
```
Set-Variable -Name 'MSYSTEM' -Value 'mingw32'
Set-Variable -Name 'TEST_var' -Value '"TEST VAL"'
Set-Variable -Name 'Path' -Value '$env:Path;/my_app/bin'
```

.env.sh:
```
MSYSTEM='mingw32'
TEST_var='"TEST VAL"'
PATH='$PATH:/my_app/bin'
```

3. We import it to the current command line process:

For PowerShell: `. .env.ps1`
For bash: `source .env.sh`

## Tip
The best idea is to use oneliners.

Powershell:
`python -m dot_to_osscript -pa; . .env.ps1; Remove-Item .env.ps1`

bash:
`python -m dot_to_osscript -pa; source .env.sh; rm ./.env.sh`

It generate ps1/sh file, import it and remove the file.