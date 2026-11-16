#!/usr/bin/env python3
"""
Generate a proper KiCad schematic for knock processor board based on hellen88bmw knock module.
"""

import uuid

# Component definitions: (ref, value, lib_id, footprint, x, y, unit)
# Positions in mm * 100 (KiCad internal units - 0.01mm)
components = [
    # Power symbols
    ('#PWR01', 'V5A', 'power:VCC', '', 1000, 500, 1),
    ('#PWR02', 'V5A', 'power:VCC', '', 5000, 500, 1),
    ('#PWR03', 'V5A', 'power:VCC', '', 9000, 500, 1),
    ('#PWR04', 'GND', 'power:GND', '', 1000, 3500, 1),
    ('#PWR05', 'GND', 'power:GND', '', 5000, 3500, 1),
    ('#PWR06', 'GND', 'power:GND', '', 9000, 3500, 1),

    # Channel 1 - U470 (LMV321 op-amp)
    ('U470', 'LMV321IDBVR', 'Amplifier_Operational:OPAMP_Generic', 'Package_TO_SOT_SMD:SOT-23-5', 2000, 1500, 1),
    ('R470', '470k', 'Device:R', 'Resistor_SMD:R_0603', 2500, 1500, 1),
    ('R471', '100k', 'Device:R', 'Resistor_SMD:R_0603', 1500, 1500, 1),
    ('C470', '100n', 'Device:C', 'Capacitor_SMD:C_0603', 2000, 2000, 1),
    ('C471', '3.3n', 'Device:C', 'Capacitor_SMD:C_0603', 1000, 1500, 1),
    ('C472', '330p', 'Device:C', 'Capacitor_SMD:C_0603', 2500, 2000, 1),

    # Channel 2 - U471 (LMV321 op-amp)
    ('U471', 'LMV321IDBVR', 'Amplifier_Operational:OPAMP_Generic', 'Package_TO_SOT_SMD:SOT-23-5', 6000, 1500, 1),
    ('R472', '12k', 'Device:R', 'Resistor_SMD:R_0603', 5500, 1500, 1),
    ('R473', '100k', 'Device:R', 'Resistor_SMD:R_0603', 6500, 1500, 1),
    ('R474', '33k', 'Device:R', 'Resistor_SMD:R_0603', 7000, 1500, 1),
    ('C473', '47p', 'Device:C', 'Capacitor_SMD:C_0603', 5000, 1500, 1),
    ('C474', '680p', 'Device:C', 'Capacitor_SMD:C_0603', 7500, 2000, 1),

    # Connectors
    ('J1', 'IN_KNOCK1', 'Connector_Generic:Conn_01x02', 'Connector_PinHeader_2.54mm:PinHeader_1x02_P2.54mm', 500, 1000, 1),
    ('J2', 'IN_KNOCK2', 'Connector_Generic:Conn_01x02', 'Connector_PinHeader_2.54mm:PinHeader_1x02_P2.54mm', 4500, 1000, 1),
    ('J3', 'AUDIO_OUT', 'Connector_Jack:Jack_3.5mm_Triple', 'Connector_Jack:Jack_3.5mm_Triple_Polypropylene', 8000, 2000, 1),
    ('J4', 'POWER', 'Connector_Generic:Conn_01x02', 'Connector_PinHeader_2.54mm:PinHeader_1x02_P2.54mm', 9500, 1500, 1),
]

# Wire connections: list of (x1, y1, x2, y2) in KiCad internal units
wires = [
    # Channel 1 input path: J1 -> C471 -> R471 -> U470 pin 3 (IN+)
    (500, 1000, 1000, 1000),  # J1 to C471
    (1000, 1000, 1000, 1500),  # C471 to R471
    (1000, 1500, 1500, 1500),  # R471 to wire junction
    (1500, 1500, 1800, 1500),  # to U470
    
    # Channel 1 feedback: U470 pin 1 (OUT) -> R470 -> U470 pin 2 (IN-)
    (2200, 1500, 2500, 1500),  # U470 OUT to R470
    (2500, 1500, 2200, 1500),  # R470 to U470 IN- (same point, feedback loop)
    
    # Channel 1 decoupling: C470 between V5A and GND near U470
    (2000, 500, 2000, 1500),   # V5A to C470
    (2000, 1500, 2000, 2000),  # C470 to C470 pin 2
    (2000, 2000, 2000, 3500),  # C470 to GND
    
    # Channel 1 output: U470 OUT -> C472 -> GND (filter)
    (2200, 1500, 2500, 1500),  # U470 OUT to C472
    (2500, 1500, 2500, 2000),  # C472 to C472 pin 2
    (2500, 2000, 2500, 3500),  # C472 to GND
    
    # Channel 1 output to J3 tip (simplified - J3 pin 1)
    (2200, 1500, 8000, 1500),  # U470 OUT to J3
    
    # Channel 2 input path: J2 -> C473 -> U471 pin 3 (IN+)
    (4500, 1000, 5000, 1000),  # J2 to C473
    (5000, 1000, 5000, 1500),  # C473 to U471 IN+
    (5000, 1500, 5800, 1500),  # to U471
    
    # Channel 2: R472 from U471 OUT to ... (series resistor)
    (6200, 1500, 6500, 1500),  # U471 OUT to R472
    (6500, 1500, 6800, 1500),  # R472 to wire
    
    # Channel 2 feedback: R473 from U471 IN- to U471 OUT
    (6500, 1500, 6200, 1500),  # R473 feedback
    
    # Channel 2 pull-down: R474 from U471 IN+ to GND
    (5000, 1500, 5000, 1800),  # U471 IN+ down to R474
    (5000, 1800, 7000, 1800),  # R474 horizontal
    (7000, 1800, 7000, 3500),  # R474 to GND
    
    # Channel 2 output filter: C474 from U471 OUT to GND
    (6200, 1500, 7500, 1500),  # U471 OUT to C474
    (7500, 1500, 7500, 2000),  # C474 vertical
    (7500, 2000, 7500, 3500),  # C474 to GND
    
    # Channel 2 output to J3 ring
    (6200, 1500, 8000, 1800),  # U471 OUT to J3 ring
    
    # Power rails
    (1000, 500, 9000, 500),    # V5A horizontal rail
    (1000, 3500, 9000, 3500),  # GND horizontal rail
    
    # Power to U470
    (2000, 500, 2000, 1300),   # V5A to U470 VCC
    (2000, 1700, 2000, 3500),  # U470 GND to GND
    
    # Power to U471
    (6000, 500, 6000, 1300),   # V5A to U471 VCC
    (6000, 1700, 6000, 3500),  # U471 GND to GND
    
    # Power to J4
    (9500, 500, 9500, 1500),   # V5A to J4
    (9500, 3500, 9500, 1500),  # GND to J4
]

# Junctions: (x, y)
junctions = [
    (1500, 1500),  # CH1 input junction
    (2200, 1500),  # CH1 U470 OUT junction
    (2500, 1500),  # CH1 R470/C472 junction
    (2000, 1500),  # CH1 V5A/GND junction
    (2000, 2000),  # CH1 C470 junction
    (2500, 2000),  # CH1 C472 junction
    (5000, 1500),  # CH2 U471 IN+ junction
    (6200, 1500),  # CH2 U471 OUT junction
    (6500, 1500),  # CH2 R472/R473 junction
    (5000, 1800),  # CH2 R474 junction
    (7000, 1800),  # CH2 R474/GND junction
    (7500, 1500),  # CH2 C474 junction
    (7500, 2000),  # CH2 C474 pin2 junction
]

def generate_sch():
    sch = []
    sch.append('(kicad_sch (version 20211123) (generator eeschema)')
    sch.append('  (uuid {})'.format(uuid.uuid4().hex))
    sch.append('  (paper "A4")')
    sch.append('  (title_block')
    sch.append('    (title "Knock Processor Board")')
    sch.append('    (date "2026-11-16")')
    sch.append('    (rev "0.1")')
    sch.append('    (company "Standalone knock sensor preamp based on hellen88bmw knock module")')
    sch.append('    (comment 1 "Dual-channel LMV321 knock preamp with 3.5mm TRS output jack")')
    sch.append('    (comment 2 "5V supply, compatible with hellen-one knock module pinout")')
    sch.append('  )')
    sch.append('  (lib_symbols)')
    
    # Standard symbols from libraries - no local lib_symbols needed
    sch.append('  )')
    sch.append('  (sheet_instances')
    sch.append('    (path "/" (page "1"))')
    sch.append('  )')

    # Components
    for ref, val, lib_id, fp, x, y, unit in components:
        uid = uuid.uuid4().hex
        if lib_id.startswith('power:'):
            sch.append(f'  (symbol (lib_id "{lib_id}") (at {x/100} {y/100} 0) (unit {unit})')
            sch.append(f'    (in_bom no) (on_board no)')
            sch.append(f'    (uuid {uid})')
            sch.append(f'    (property "Reference" "{ref}" (id 0) (at 0 0 0) (effects (font (size 1.27 1.27)) hide))')
            sch.append(f'    (property "Value" "{val}" (id 1) (at 0 0 0) (effects (font (size 1.27 1.27)) hide))')
            sch.append(f'    (pin numbers hide)')
            sch.append(f'    (pin names hide)')
            sch.append(f'  )')
        else:
            sch.append(f'  (symbol (lib_id "{lib_id}") (at {x/100} {y/100} 0) (unit {unit})')
            sch.append(f'    (in_bom yes) (on_board yes)')
            sch.append(f'    (uuid {uid})')
            sch.append(f'    (property "Reference" "{ref}" (id 0) (at 0 0 0) (effects (font (size 1.27 1.27)) (justify left)))')
            sch.append(f'    (property "Value" "{val}" (id 1) (at 0 0 0) (effects (font (size 1.27 1.27)) (justify left)))')
            if fp:
                sch.append(f'    (property "Footprint" "{fp}" (id 2) (at 0 0 0) (effects (font (size 1.27 1.27)) hide))')
            sch.append(f'    (property "Datasheet" "" (id 3) (at 0 0 0) (effects (font (size 1.27 1.27)) hide))')
            sch.append(f'  )')

    # Labels (global labels for nets)
    labels = [
        ('IN_KNOCK1', 50, 1000, 0, 'input'),
        ('IN_KNOCK2', 4500, 1000, 0, 'input'),
        ('OUT_KNOCK1', 9000, 1500, 0, 'output'),
        ('OUT_KNOCK2', 9000, 1800, 0, 'output'),
    ]
    for name, x, y, orient, shape in labels:
        sch.append(f'  (global_label "{name}"')
        sch.append(f'    (shape {shape})')
        sch.append(f'    (at {x/100} {y/100} {orient})')
        sch.append(f'    (effects (font (size 1.27 1.27)) (justify left bottom)))')

    # Wires
    for x1, y1, x2, y2 in wires:
        sch.append(f'  (wire')
        sch.append(f'    (pts')
        sch.append(f'      (xy {x1/100} {y1/100})')
        sch.append(f'      (xy {x2/100} {y2/100})')
        sch.append(f'    )')
        sch.append(f'    (stroke (width 0) (type default) (color 0 0 0 0))')
        sch.append(f'  )')

    # Junctions
    for x, y in junctions:
        sch.append(f'  (junction (at {x/100} {y/100}) (diameter 1.016) (color 0 0 0 0))')

    sch.append(')')
    return '\n'.join(sch)

def main():
    out_dir = '/opt/data/projects/knock-processor-board-new'
    sch_content = generate_sch()
    with open(os.path.join(out_dir, 'knock-processor-a.kicad_sch'), 'w') as f:
        f.write(sch_content)
    print(f"Generated schematic: {len(sch_content)} chars")

if __name__ == '__main__':
    import os
    main()
