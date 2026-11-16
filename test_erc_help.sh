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
# Try with --help to see options
result = subprocess.run(['kicad-cli', 'sch', 'erc', '--help'], capture_output=True, text=True, timeout=30)
print('ERC Help:')
print(result.stdout)
print(result.stderr)
"