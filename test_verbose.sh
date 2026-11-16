#!/bin/bash
docker run --rm \
  -v /mnt/data/projects/knock-processor-board:/work/src:ro \
  -v /mnt/data/projects/pcb-projects/tools:/work/tools:ro \
  -v /mnt/data/projects/pcb-projects/libraries:/work/libs:ro \
  -v /mnt/data/projects/pcb-projects/runs/test:/work/out:rw \
  --user $(id -u):$(id -g) \
  --network none \
  --memory 4g \
  --cpus 2 \
  kicad-runner:1.0.0 \
  python3 -c "
import subprocess
# Try with verbose/debug output
result = subprocess.run(['kicad-cli', '--verbose', 'sch', 'erc', '/work/src/src.kicad_sch', '--output', '/work/out/erc.rpt'], capture_output=True, text=True, timeout=60)
print('STDOUT:', result.stdout)
print('STDERR:', result.stderr)
print('Return code:', result.returncode)
"