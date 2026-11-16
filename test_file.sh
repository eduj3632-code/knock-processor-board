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
# Test if file exists and is readable
import os
f = '/work/src/src.kicad_sch'
print('File exists:', os.path.exists(f))
print('File size:', os.path.getsize(f) if os.path.exists(f) else 'N/A')
# Try to read first 100 chars
if os.path.exists(f):
    with open(f) as fp:
        print('First 200 chars:', fp.read(200))
"