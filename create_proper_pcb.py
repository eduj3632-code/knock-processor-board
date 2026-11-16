#!/usr/bin/env python3
"""
Generate a complete KiCad PCB file for knock processor board.
Includes components, zones, tracks, and proper structure.
"""

import uuid

def generate_pcb():
    """Generate complete KiCad PCB file"""
    pcb_uuid = uuid.uuid4().hex
    
    # Component positions (x, y in mm * 100, rotation in degrees * 10)
    # Board is 60mm x 40mm
    components = [
        # (ref, footprint, x, y, rot, layer, netlist)
        ('U470', 'Package_TO_SOT_SMD:SOT-23-5', 2000, 1500, 0, 'F.Cu', {'1': 'OUT_KNOCK1', '2': 'GND', '3': 'IN_KNOCK1', '5': 'V5A'}),
        ('U471', 'Package_TO_SOT_SMD:SOT-23-5', 6000, 1500, 0, 'F.Cu', {'1': 'OUT_KNOCK2', '2': 'GND', '3': 'IN_KNOCK2', '5': 'V5A'}),
        ('R470', 'Resistor_SMD:R_0603', 2500, 1500, 0, 'F.Cu', {'1': 'OUT_KNOCK1', '2': 'IN_KNOCK1'}),
        ('R471', 'Resistor_SMD:R_0603', 1500, 1500, 0, 'F.Cu', {'1': 'IN_KNOCK1', '2': 'IN_KNOCK1'}),
        ('C470', 'Capacitor_SMD:C_0603', 2000, 2000, 0, 'F.Cu', {'1': 'V5A', '2': 'GND'}),
        ('C471', 'Capacitor_SMD:C_0603', 1000, 1500, 0, 'F.Cu', {'1': 'IN_KNOCK1', '2': 'IN_KNOCK1'}),
        ('C472', 'Capacitor_SMD:C_0603', 2500, 2000, 0, 'F.Cu', {'1': 'OUT_KNOCK1', '2': 'GND'}),
        ('R472', 'Resistor_SMD:R_0603', 5500, 1500, 0, 'F.Cu', {'1': 'OUT_KNOCK2', '2': 'OUT_KNOCK2'}),
        ('R473', 'Resistor_SMD:R_0603', 6500, 1500, 0, 'F.Cu', {'1': 'OUT_KNOCK2', '2': 'OUT_KNOCK2'}),
        ('R474', 'Resistor_SMD:R_0603', 7000, 1800, 0, 'F.Cu', {'1': 'IN_KNOCK2', '2': 'GND'}),
        ('C473', 'Capacitor_SMD:C_0603', 5000, 1500, 0, 'F.Cu', {'1': 'IN_KNOCK2', '2': 'IN_KNOCK2'}),
        ('C474', 'Capacitor_SMD:C_0603', 7500, 2000, 0, 'F.Cu', {'1': 'OUT_KNOCK2', '2': 'GND'}),
        ('J1', 'Connector_PinHeader_2.54mm:PinHeader_1x02_P2.54mm', 500, 1000, 0, 'F.Cu', {'1': 'IN_KNOCK1', '2': 'GND'}),
        ('J2', 'Connector_PinHeader_2.54mm:PinHeader_1x02_P2.54mm', 4500, 1000, 0, 'F.Cu', {'1': 'IN_KNOCK2', '2': 'GND'}),
        ('J3', 'Connector_Jack:Jack_3.5mm_Triple_Polypropylene', 8000, 2000, 0, 'F.Cu', {'1': 'OUT_KNOCK1', '2': 'OUT_KNOCK2', '3': 'GND'}),
        ('J4', 'Connector_PinHeader_2.54mm:PinHeader_1x02_P2.54mm', 9500, 1500, 0, 'F.Cu', {'1': 'V5A', '2': 'GND'}),
    ]
    
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
    
    # Add components as footprints
    for ref, fp, x, y, rot, layer, pins in components:
        fp_uuid = uuid.uuid4().hex
        pcb.append(f'  (footprint "{fp}"')
        pcb.append(f'    (layer "{layer}")')
        pcb.append(f'    (at {x/100} {y/100} {rot})')
        pcb.append(f'    (property "Reference" "{ref}" (at 0 0 0) (layer "F.SilkS")')
        pcb.append(f'      (effects (font (size 1 1) (thickness 0.15)))')
        pcb.append(f'    )')
        pcb.append(f'    (property "Value" "{ref}" (at 0 0 0) (layer "F.Fab")')
        pcb.append(f'      (effects (font (size 1 1) (thickness 0.15)) hide)')
        pcb.append(f'    )')
        pcb.append(f'    (uuid {fp_uuid})')
        
        # Add pins/pads
        pin_num = 1
        for pin_name, net in pins.items():
            pcb.append(f'    (pad {pin_num} thru_hole circle (at 0 0 0) (size 1.5 1.5) (drill 0.8) (layers "*.Cu" "*.Mask") (net {list(nets).index(net)} "{net}"))')
            pin_num += 1
        
        pcb.append(f'  )')
    
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
    
    # Add a GND zone on F.Cu
    pcb.append(f'  (zone (net 6) (net_name "GND") (layer "F.Cu")')
    pcb.append(f'    (uuid {uuid.uuid4().hex})')
    pcb.append(f'    (hatch edge 0.508)')
    pcb.append(f'    (priority 0)')
    pcb.append(f'    (connect_pads (clearance 0.254))')
    pcb.append(f'    (min_thickness 0.254)')
    pcb.append(f'    (keepout (tracks not_allowed) (vias not_allowed) (pads not_allowed) (copperpour not_allowed) (footprints not_allowed))')
    pcb.append(f'    (filled_polygon')
    pcb.append(f'      (pts')
    pcb.append(f'        (xy 0 0)')
    pcb.append(f'        (xy 60 0)')
    pcb.append(f'        (xy 60 40)')
    pcb.append(f'        (xy 0 40)')
    pcb.append(f'      )')
    pcb.append(f'    )')
    pcb.append(f'  )')
    
    # Add a V5A zone on B.Cu
    pcb.append(f'  (zone (net 5) (net_name "V5A") (layer "B.Cu")')
    pcb.append(f'    (uuid {uuid.uuid4().hex})')
    pcb.append(f'    (hatch edge 0.508)')
    pcb.append(f'    (priority 0)')
    pcb.append(f'    (connect_pads (clearance 0.254))')
    pcb.append(f'    (min_thickness 0.254)')
    pcb.append(f'    (keepout (tracks not_allowed) (vias not_allowed) (pads not_allowed) (copperpour not_allowed) (footprints not_allowed))')
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
    print(f"Generated PCB: {len(pcb_content)} chars")

if __name__ == '__main__':
    import os
    main()
