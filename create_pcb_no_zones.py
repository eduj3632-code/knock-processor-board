#!/usr/bin/env python3
"""
Generate a KiCad PCB file WITHOUT zones - simplest valid format.
"""

import uuid

def generate_pcb():
    """Generate minimal valid KiCad PCB file without zones"""
    pcb_uuid = uuid.uuid4().hex
    
    pcb = []
    pcb.append(f'(kicad_pcb (version 20211123) (generator pcbnew)')
    pcb.append(f'  (generator_version "8.0")')
    pcb.append(f'  (uuid {pcb_uuid})')
    pcb.append(f'  (general')
    pcb.append(f'    (thickness 1.6)')
    pcb.append(f'  )')
    pcb.append(f'  (paper "A4")')
    pcb.append(f'  (layers')
    pcb.append(f'    (0 "F.Cu" signal)')
    pcb.append(f'    (31 "B.Cu" signal)')
    pcb.append(f'    (32 "B.Adhes" user "Adhesive on bottom side")')
    pcb.append(f'    (33 "F.Adhes" user "Adhesive on top side")')
    pcb.append(f'    (34 "B.Paste" user "Solder paste on bottom side")')
    pcb.append(f'    (35 "F.Paste" user "Solder paste on top side")')
    pcb.append(f'    (36 "B.SilkS" user "Silk screen on bottom side")')
    pcb.append(f'    (37 "F.SilkS" user "Silk screen on top side")')
    pcb.append(f'    (38 "B.Mask" user "Solder mask on bottom side")')
    pcb.append(f'    (39 "F.Mask" user "Solder mask on top side")')
    pcb.append(f'    (40 "Dwgs.User" user "User drawings")')
    pcb.append(f'    (41 "Cmts.User" user "User comments")')
    pcb.append(f'    (42 "Eco1.User" user "Engineering change order 1")')
    pcb.append(f'    (43 "Eco2.User" user "Engineering change order 2")')
    pcb.append(f'    (44 "Edge.Cuts" user "Board outline")')
    pcb.append(f'    (45 "Margin" user "Margin")')
    pcb.append(f'    (46 "B.CrtYd" user "Courtyard on bottom side")')
    pcb.append(f'    (47 "F.CrtYd" user "Courtyard on top side")')
    pcb.append(f'    (48 "B.Fab" user "Fabrication on bottom side")')
    pcb.append(f'    (49 "F.Fab" user "Fabrication on top side")')
    pcb.append(f'  )')
    pcb.append(f'  (setup')
    pcb.append(f'    (pad_to_mask_clearance 0.051)')
    pcb.append(f'    (allow_soldermask_bridges_in_footprints no)')
    pcb.append(f'  )')
    
    # Nets
    nets = ['', 'IN_KNOCK1', 'IN_KNOCK2', 'OUT_KNOCK1', 'OUT_KNOCK2', 'V5A', 'GND']
    for i, net in enumerate(nets):
        if net:
            pcb.append(f'  (net {i} "{net}")')
    
    pcb.append(f'  (net_class Default "Default net class")')
    pcb.append(f'  (net_class Power "Power nets")')
    
    # Board outline: 60mm x 40mm
    pcb.append(f'  (gr_poly')
    pcb.append(f'    (pts')
    pcb.append(f'      (xy 0 0)')
    pcb.append(f'      (xy 60 0)')
    pcb.append(f'      (xy 60 40)')
    pcb.append(f'      (xy 0 40)')
    pcb.append(f'    )')
    pcb.append(f'    (layer "Edge.Cuts")')
    pcb.append(f'    (width 0.15)')
    pcb.append(f'  )')
    
    # NO zones at all
    
    pcb.append(f'  (board_setup')
    pcb.append(f'    (design_rules')
    pcb.append(f'      (trace_min 0.1524)')
    pcb.append(f'      (via_dia 0.508)')
    pcb.append(f'      (via_drill 0.254)')
    pcb.append(f'      (trace_clearance 0.2032)')
    pcb.append(f'      (zone_clearance 0.508)')
    pcb.append(f'    )')
    pcb.append(f'    (layer_setup (copper_layers 2) (copper_layer_list "F.Cu B.Cu"))')
    pcb.append(f'  )')
    
    pcb.append(f')')
    return '\n'.join(pcb)

def main():
    out_dir = '/opt/data/projects/knock-processor-board-new'
    pcb_content = generate_pcb()
    with open(os.path.join(out_dir, 'knock-processor-a.kicad_pcb'), 'w') as f:
        f.write(pcb_content)
    print(f"Generated PCB (no zones): {len(pcb_content)} chars")

if __name__ == '__main__':
    import os
    main()
