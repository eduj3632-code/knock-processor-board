import sys

def check_parens(filename):
    with open(filename) as f:
        content = f.read()
    depth = 0
    for i, ch in enumerate(content):
        if ch == '(':
            depth += 1
        elif ch == ')':
            depth -= 1
            if depth < 0:
                print(f'ERROR: Unmatched ) at position {i}')
                print(content[max(0,i-50):i+50])
                return False
    if depth != 0:
        print(f'ERROR: Unbalanced, depth={depth} at end')
        depth = 0
        for i, ch in enumerate(content):
            if ch == '(':
                depth += 1
            elif ch == ')':
                depth -= 1
            if depth < 0:
                print(f'First negative at {i}')
                break
        return False
    print('OK')
    return True

check_parens('src.kicad_pcb')
check_parens('src.kicad_sch')
check_parens('src.kicad_pro')