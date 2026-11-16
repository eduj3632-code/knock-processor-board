#!/usr/bin/env python3
"""
Generate a KiCad PCB file with minimal footprint to satisfy LoadBoard().
"""

import uuid

def generate_pcb():
    """Generate PCB with a minimal footprint"""
    pcb_uuid = uuid.uuid4().hex
    
    pcb = []
    pcb.append(f'(kicad_pcb (version 20211014) (generator pcbnew)')
    pcb.append(f'  (generator_version "8.0")')
    pcb.append(f'  (uuid {pcb_uuid})')
    pcb.append(f'  (general')
    pcb.append(f'    (thickness 1.6)')
    pcb.append(f'  )')
    pcb.append(f'  (paper "A4")')
    pcb.append(f'  (title_block')
    pcb.append(f'    (title "Knock Processor Board")')
    pcb.append(f'    (date "2026-11-16")')
    pcb.append(f'    (rev "0.1")')
    pcb.append(f'    (company "Standalone knock sensor preamp")')
    pcb.append(f'  )')
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
    pcb.append(f'    (stackup')
    pcb.append(f'      (layer "F.SilkS" (type "Top Silk Screen") (color "White"))')
    pcb.append(f'      (layer "F.Paste" (type "Top Solder Paste"))')
    pcb.append(f'      (layer "F.Mask" (type "Top Solder Mask") (color "Green") (thickness 0.01))')
    pcb.append(f'      (layer "F.Cu" (type "copper") (thickness 0.035))')
    pcb.append(f'      (layer "dielectric 1" (type "core") (thickness 1.53) (material "FR4") (epsilon_r 4.5) (loss_tangent 0.02))')
    pcb.append(f'      (layer "B.Cu" (type "copper") (thickness 0.035))')
    pcb.append(f'      (layer "B.Mask" (type "Bottom Solder Mask") (color "Green") (thickness 0.01))')
    pcb.append(f'      (layer "B.Paste" (type "Bottom Solder Paste"))')
    pcb.append(f'      (layer "B.SilkS" (type "Bottom Silk Screen") (color "White"))')
    pcb.append(f'      (copper_finish "None")')
    pcb.append(f'      (dielectric_constraints no)')
    pcb.append(f'    )')
    pcb.append(f'    (pad_to_mask_clearance 0)')
    pcb.append(f'    (aux_axis_origin 0 0)')
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
    
    # Add a minimal footprint (test pad on GND net)
    fp_uuid = uuid.uuid4().hex
    pcb.append(f'  (footprint "TestPoint:TestPoint_Pad_D1.0mm"')
    pcb.append(f'    (layer "F.Cu")')
    pcb.append(f'    (at 5 5 0)')
    pcb.append(f'    (property "Reference" "TP1" (at 0 0 0) (layer "F.SilkS")')
    pcb.append(f'      (effects (font (size 1 1) (thickness 0.15)))')
    pcb.append(f'    )')
    pcb.append(f'    (property "Value" "GND" (at 0 0 0) (layer "F.Fab")')
    pcb.append(f'      (effects (font (size 1 1) (thickness 0.15)) hide)')
    pcb.append(f'    )')
    pcb.append(f'    (uuid {fp_uuid})')
    pcb.append(f'    (pad "1" thru_hole circle (at 0 0 0) (size 1.5 1.5) (drill 0.8) (layers "*.Cu" "*.Mask") (net 6 "GND"))')
    pcb.append(f'  )')
    
    # GND zone on F.Cu
    pcb.append(f'  (zone (net 6) (net_name "GND") (layer "F.Cu")')
    pcb.append(f'    (uuid {uuid.uuid4().hex})')
    pcb.append(f'    (hatch edge 0.508)')
    pcb.append(f'    (priority 0)')
    pcb.append(f'    (connect_pads (clearance 0.254))')
    pcb.append(f'    (min_thickness 0.254)')
    pcb.append(f'    (filled_polygon')
    pcb.append(f'      (pts')
    pcb.append(f'        (xy 0 0)')
    pcb.append(f'        (xy 60 0)')
    pcb.append(f'        (xy 60 40)')
    pcb.append(f'        (xy 0 40)')
    pcb.append(f'      )')
    pcb.append(f'    )')
    pcb.append(f'  )')
    
    # V5A zone on B.Cu
    pcb.append(f'  (zone (net 5) (net_name "V5A") (layer "B.Cu")')
    pcb.append(f'    (uuid {uuid.uuid4().hex})')
    pcb.append(f'    (hatch edge 0.508)')
    pcb.append(f'    (priority 0)')
    pcb.append(f'    (connect_pads (clearance 0.254))')
    pcb.append(f'    (min_thickness 0.254)')
    pcb.append(f'    (filled_polygon')
    pcb.append(f'      (pts')
    pcb.append(f'        (xy 0 0)')
    pcb.append(f'        (xy 60 0)')
    pcb.append(f'        (xy 60 40)')
    pcb.append(f'        (xy 0 40)')
    pcb.append(f'      )')
    pcb.append(f'    )')
    pcb.append(f'  )')
    
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
    print(f"Generated PCB v4 (with test footprint): {len(pcb_content)} chars")

if __name__ == '__main__':
    import os
    main()
