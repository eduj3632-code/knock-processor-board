import subprocess
result = subprocess.run(['kicad-cli', 'sch', 'erc', '/work/src/src.kicad_sch', '--output', '/work/out/erc.rpt'], capture_output=True, text=True, timeout=60)
print('STDOUT:', result.stdout)
print('STDERR:', result.stderr)
print('Return code:', result.returncode)