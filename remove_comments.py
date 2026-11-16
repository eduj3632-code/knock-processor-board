with open('src.kicad_pcb') as f:
    lines = f.readlines()
# Remove lines that are just comments (start with # after whitespace)
filtered = [l for l in lines if not l.lstrip().startswith('#')]
with open('src.kicad_pcb', 'w') as f:
    f.writelines(filtered)
print(f'Removed {len(lines) - len(filtered)} comment lines')