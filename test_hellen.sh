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
# Test with a known-good schematic from hellen88bmw
result = subprocess.run(['kicad-cli', 'sch', 'erc', '/work/src/../hellen88bmw/hellen88bmw.kicad_sch', '--output', '/work/out/erc_test.rpt'], capture_output=True, text=True, timeout=60)
print('STDOUT:', result.stdout)
print('STDERR:', result.stderr)
print('Return code:', result.returncode)
"