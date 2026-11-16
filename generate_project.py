#!/usr/bin/env python3
"""
Generate complete KiCad project for knock processor board.
Uses only standard KiCad symbols from built-in libraries.
"""

import os
import uuid

# Component definitions: (ref, value, lib_id, footprint, position_x, position_y)
# Position in mm * 10 (KiCad internal units)
components = [
    # Power symbols
    ('#PWR01', 'V5A', 'power:VCC', '', 1000, 1000),
    ('#PWR02', 'V5A', 'power:VCC', '', 5000, 1000),
    ('#PWR03', 'V5A', 'power:VCC', '', 9000, 1000),
    ('#PWR04', 'GND', 'power:GND', '', 1000, 3000),
    ('#PWR05', 'GND', 'power:GND', '', 5000, 3000),
    ('#PWR06', 'GND', 'power:GND', '', 9000, 3000),
    ('#PWR07', 'GND', 'power:GND', '', 1000, 6000),
    ('#PWR08', 'GND', 'power:GND', '', 5000, 6000),
    ('#PWR09', 'GND', 'power:GND', '', 9000, 6000),

    # Channel 1 components
    ('U470', 'LMV321IDBVR', 'Amplifier_Operational:OPAMP_Generic', 'Package_TO_SOT_SMD:SOT-23-5', 2000, 1500),
    ('R470', '470k', 'Device:R', 'Resistor_SMD:R_0603', 1500, 1500),
    ('R471', '100k', 'Device:R', 'Resistor_SMD:R_0603', 2500, 1500),
    ('C470', '100n', 'Device:C', 'Capacitor_SMD:C_0603', 2000, 2000),
    ('C471', '3.3n', 'Device:C', 'Capacitor_SMD:C_0603', 1000, 1500),
    ('C472', '330p', 'Device:C', 'Capacitor_SMD:C_0603', 2500, 2000),

    # Channel 2 components
    ('U471', 'LMV321IDBVR', 'Amplifier_Operational:OPAMP_Generic', 'Package_TO_SOT_SMD:SOT-23-5', 6000, 1500),
    ('R472', '12k', 'Device:R', 'Resistor_SMD:R_0603', 5500, 1500),
    ('R473', '100k', 'Device:R', 'Resistor_SMD:R_0603', 6500, 1500),
    ('R474', '33k', 'Device:R', 'Resistor_SMD:R_0603', 7000, 1500),
    ('C473', '47p', 'Device:C', 'Capacitor_SMD:C_0603', 5000, 1500),
    ('C474', '680p', 'Device:C', 'Capacitor_SMD:C_0603', 7500, 2000),

    # Connectors
    ('J1', 'IN_KNOCK1', 'Connector_Generic:Conn_01x02', 'Connector_PinHeader_2.54mm:PinHeader_1x02_P2.54mm', 500, 1000),
    ('J2', 'IN_KNOCK2', 'Connector_Generic:Conn_01x02', 'Connector_PinHeader_2.54mm:PinHeader_1x02_P2.54mm', 4500, 1000),
    ('J3', 'AUDIO_OUT', 'Connector_Jack:Jack_3.5mm_Triple', 'Connector_Jack:Jack_3.5mm_Triple_Polypropylene', 8000, 2000),
    ('J4', 'POWER', 'Connector_Generic:Conn_01x02', 'Connector_PinHeader_2.54mm:PinHeader_1x02_P2.54mm', 9500, 1500),
]

# Wire connections (net names)
# Channel 1: IN_KNOCK1 -> C471 -> R471 -> U470+
# U470- -> R470 -> U470out
# U470out -> C472 -> GND
# U470 VCC -> V5A, GND -> GND
# C470 decoupling on V5A near U470
# U470out -> J3 tip

# Channel 2: IN_KNOCK2 -> C473 -> U471+
# U471- -> R472 -> U471out
# U471out -> R473 -> GND (feedback?)
# R474 pull-down on U471+
# C474 output filter
# U471out -> J3 ring

def generate_sch():
    """Generate KiCad schematic file"""
    sch = []
    sch.append('(kicad_sch (version 20211123) (generator eeschema)')
    sch.append('  (uuid {})'.format(uuid.uuid4().hex))
    sch.append('  (paper "A4")')
    sch.append('  (title_block')
    sch.append('    (title "Knock Processor Board")')
    sch.append('    (date "2026-11-15")')
    sch.append('    (rev "0.1")')
    sch.append('    (company "Standalone knock sensor preamp based on hellen88bmw knock module")')
    sch.append('    (comment 1 "Dual-channel LMV321 knock preamp with 3.5mm TRS output jack")')
    sch.append('    (comment 2 "5V supply, VREF input, compatible with hellen-one knock module pinout")')
    sch.append('  )')

    # lib_symbols section
    sch.append('  (lib_symbols')
    # We'll reference standard symbols, no local lib_symbols needed
    sch.append('  )')

    # Sheet instances
    sch.append('  (sheet_instances')
    sch.append('    (path "/" (page "1"))')
    sch.append('  )')

    # Components
    for ref, val, lib_id, fp, x, y in components:
        uid = uuid.uuid4().hex
        if lib_id.startswith('power:'):
            sch.append(f'  (symbol (lib_id "{lib_id}") (at {x/100} {y/100} 0) (unit 1)')
            sch.append(f'    (in_bom no) (on_board no)')
            sch.append(f'    (uuid {uid})')
            sch.append(f'    (property "Reference" "{ref}" (id 0) (at 0 0 0) (effects (font (size 1.27 1.27)) hide))')
            sch.append(f'    (property "Value" "{val}" (id 1) (at 0 0 0) (effects (font (size 1.27 1.27)) hide))')
            sch.append(f'    (pin numbers hide)')
            sch.append(f'    (pin names hide)')
            sch.append(f'  )')
        else:
            sch.append(f'  (symbol (lib_id "{lib_id}") (at {x/100} {y/100} 0) (unit 1)')
            sch.append(f'    (in_bom yes) (on_board yes)')
            sch.append(f'    (uuid {uid})')
            sch.append(f'    (property "Reference" "{ref}" (id 0) (at 0 0 0) (effects (font (size 1.27 1.27)) (justify left)))')
            sch.append(f'    (property "Value" "{val}" (id 1) (at 0 0 0) (effects (font (size 1.27 1.27)) (justify left)))')
            if fp:
                sch.append(f'    (property "Footprint" "{fp}" (id 2) (at 0 0 0) (effects (font (size 1.27 1.27)) hide))')
            sch.append(f'    (property "Datasheet" "" (id 3) (at 0 0 0) (effects (font (size 1.27 1.27)) hide))')
            sch.append(f'  )')

    # Labels
    labels = [
        ('IN_KNOCK1', 50, 1000, 0),
        ('IN_KNOCK2', 4500, 1000, 0),
        ('OUT_KNOCK1', 10000, 1000, 0),
        ('OUT_KNOCK2', 10000, 3000, 0),
        ('V5A', 1000, 1000, 0),
        ('GND', 1000, 3000, 0),
    ]
    for name, x, y, orient in labels:
        sch.append(f'  (label "{name}" (at {x/100} {y/100} {orient})')
        sch.append(f'    (effects (font (size 1.27 1.27)) (justify left bottom)))')

    # Wires (simplified - connect pins by net names)
    # In real KiCad, wires connect pins directly
    # For now, use global labels to establish connectivity
    sch.append('  (global_label "IN_KNOCK1"')
    sch.append('    (shape input)')
    sch.append('    (at 50 1000 0)')
    sch.append('    (effects (font (size 1.27 1.27)) (justify left bottom)))')
    
    sch.append('  (global_label "IN_KNOCK2"')
    sch.append('    (shape input)')
    sch.append('    (at 4500 1000 0)')
    sch.append('    (effects (font (size 1.27 1.27)) (justify left bottom)))')
    
    sch.append('  (global_label "OUT_KNOCK1"')
    sch.append('    (shape output)')
    sch.append('    (at 10000 1000 0)')
    sch.append('    (effects (font (size 1.27 1.27)) (justify left bottom)))')
    
    sch.append('  (global_label "OUT_KNOCK2"')
    sch.append('    (shape output)')
    sch.append('    (at 10000 3000 0)')
    sch.append('    (effects (font (size 1.27 1.27)) (justify left bottom)))')
    
    sch.append('  (global_label "V5A"')
    sch.append('    (shape power_input)')
    sch.append('    (at 1000 1000 0)')
    sch.append('    (effects (font (size 1.27 1.27)) (justify left bottom)))')
    
    sch.append('  (global_label "GND"')
    sch.append('    (shape power_input)')
    sch.append('    (at 1000 3000 0)')
    sch.append('    (effects (font (size 1.27 1.27)) (justify left bottom)))')

    sch.append(')')
    return '\n'.join(sch)


def generate_pcb():
    """Generate minimal KiCad PCB file"""
    pcb = []
    pcb.append('(kicad_pcb (version 20211123) (generator pcbnew)')
    pcb.append('  (generator_version "8.0")')
    pcb.append('  (uuid {})'.format(uuid.uuid4().hex))
    pcb.append('  (general')
    pcb.append('    (thickness 1.6)')
    pcb.append('  )')
    pcb.append('  (paper "A4")')
    pcb.append('  (layers')
    pcb.append('    (0 "F.Cu" signal)')
    pcb.append('    (31 "B.Cu" signal)')
    pcb.append('    (32 "B.Adhes" user "Adhesive on bottom side")')
    pcb.append('    (33 "F.Adhes" user "Adhesive on top side")')
    pcb.append('    (34 "B.Paste" user "Solder paste on bottom side")')
    pcb.append('    (35 "F.Paste" user "Solder paste on top side")')
    pcb.append('    (36 "B.SilkS" user "Silk screen on bottom side")')
    pcb.append('    (37 "F.SilkS" user "Silk screen on top side")')
    pcb.append('    (38 "B.Mask" user "Solder mask on bottom side")')
    pcb.append('    (39 "F.Mask" user "Solder mask on top side")')
    pcb.append('    (40 "Dwgs.User" user "User drawings")')
    pcb.append('    (41 "Cmts.User" user "User comments")')
    pcb.append('    (42 "Eco1.User" user "Engineering change order 1")')
    pcb.append('    (43 "Eco2.User" user "Engineering change order 2")')
    pcb.append('    (44 "Edge.Cuts" user "Board outline")')
    pcb.append('    (45 "Margin" user "Margin")')
    pcb.append('    (46 "B.CrtYd" user "Courtyard on bottom side")')
    pcb.append('    (47 "F.CrtYd" user "Courtyard on top side")')
    pcb.append('    (48 "B.Fab" user "Fabrication on bottom side")')
    pcb.append('    (49 "F.Fab" user "Fabrication on top side")')
    pcb.append('  )')
    pcb.append('  (setup')
    pcb.append('    (pad_to_mask_clearance 0.051)')
    pcb.append('    (allow_soldermask_bridges_in_footprints no)')
    pcb.append('  )')
    pcb.append('  (net 0 "")')
    pcb.append('  (net_class Default "Default net class")')
    pcb.append('  (net_class Power "Power nets")')
    pcb.append('  (board_setup')
    pcb.append('    (design_rules')
    pcb.append('      (trace_min 0.1524)')
    pcb.append('      (via_dia 0.508)')
    pcb.append('      (via_drill 0.254)')
    pcb.append('      (trace_clearance 0.2032)')
    pcb.append('      (zone_clearance 0.508)')
    pcb.append('    )')
    pcb.append('  )')
    
    # Board outline: 60mm x 40mm
    pcb.append('  (gr_poly')
    pcb.append('    (pts')
    pcb.append('      (xy 0 0)')
    pcb.append('      (xy 60 0)')
    pcb.append('      (xy 60 40)')
    pcb.append('      (xy 0 40)')
    pcb.append('    )')
    pcb.append('    (layer "Edge.Cuts")')
    pcb.append('    (width 0.15)')
    pcb.append('  )')
    
    pcb.append(')')
    return '\n'.join(pcb)


def main():
    out_dir = '/opt/data/projects/knock-processor-board-new'
    
    # Generate schematic
    sch_content = generate_sch()
    with open(os.path.join(out_dir, 'knock-processor-a.kicad_sch'), 'w') as f:
        f.write(sch_content)
    print(f"Generated schematic: {len(sch_content)} chars")
    
    # Generate PCB
    pcb_content = generate_pcb()
    with open(os.path.join(out_dir, 'knock-processor-a.kicad_pcb'), 'w') as f:
        f.write(pcb_content)
    print(f"Generated PCB: {len(pcb_content)} chars")
    
    # Generate project file
    pro_content = f'''(kicad_pro (version 8) (generator eeschema)
  (uuid {uuid.uuid4().hex})
  (board
    (design_settings
      (defaults
        (board_outline_line_width 0.15)
        (copper_line_width 0.2)
        (copper_text_thickness 0.3)
        (copper_text_size 1.5 1.5)
        (edge_cut_line_width 0.15)
        (silk_screen_line_width 0.15)
        (silk_screen_text_thickness 0.3)
        (silk_screen_text_size 1.5 1.5)
        (zone_45_degree_only no)
      )
      (diff_pair_dimensions)
      (rule_severities
        (annulus (min 0 max 0 severity "warning"))
        (clearance (min 0 max 0 severity "error"))
        (copper_edge_clearance (min 0 max 0 severity "error"))
        (courtyards_clearance (min 0 max 0 severity "ignore"))
        (diff_pair_gap_out_of_range (min 0 max 0 severity "error"))
        (diff_pair_uncoupled_length_too_long (min 0 max 0 severity "error"))
        (hole_clearance (min 0 max 0 severity "error"))
        (hole_near_hole (min 0 max 0 severity "error"))
        (item_on_copper (min 0 max 0 severity "error"))
        (length_out_of_range (min 0 max 0 severity "error"))
        (malformed_courtyard (min 0 max 0 severity "ignore"))
        (microvia_drill_out_of_range (min 0 max 0 severity "error"))
        (missing_courtyard (min 0 max 0 severity "ignore"))
        (net_conflict (min 0 max 0 severity "error"))
        (padstack (min 0 max 0 severity "error"))
        (thermal_relief (min 0 max 0 severity "warning"))
        (too_many_vias (min 0 max 0 severity "error"))
        (track_width_out_of_range (min 0 max 0 severity "error"))
        (unconnected_items (min 0 max 0 severity "error"))
        (zone_has_empty_net (min 0 max 0 severity "warning"))
        (zones_intersect (min 0 max 0 severity "error"))
      )
      (thermal_relief_gap 0.508)
      (track_widths
        0.2
        0.25
        0.3
        0.4
        0.5
      )
      (via_sizes
        0.5
        0.6
        0.8
        1.0
      )
      (zone_clearance 0.508)
    )
  )
  (libraries
    (pinned_footprint_libs)
    (pinned_symbol_libs)
  )
  (net_settings
    (classes
      (net_class 0 "Default")
      (net_class 1 "Power")
    )
    (net_colors)
    (layer_colors)
    (net_class_assignments)
  )
  (schematic
    (annotate_start_num 0)
    (label_format "%%R")
    (drawing
      (default_line_thickness 6.0)
      (default_text_size 1.5 1.5)
      (default_text_thickness 6.0)
      (inter_sheet_ref_own_page no)
      (inter_sheet_ref_prefix "")
      (inter_sheet_ref_suffix "")
      (inter_sheet_ref_size 1.5 1.5)
      (junction_size_choice 3)
      (label_size 1.5 1.5)
      (pin_symbol_size 1.5 1.5)
      (text_offset 1.27)
      (wire_style "dots")
    )
    (legacy
      (lib_symbol_fields)
      (annotation_filename "")
      (pdf_file_name "")
      (pwr_flag_name "#FLG")
      (remap_symbol_names no)
      (sheet_name_font_size 1.5)
      (sheet_number_font_size 1.5)
    )
    (page_settings
      (plot_border_title_block yes)
      (page_size "A4")
      (output_directory "")
      (custom_page_size 210 297)
    )
  )
)'''
    with open(os.path.join(out_dir, 'knock-processor-a.kicad_pro'), 'w') as f:
        f.write(pro_content)
    print("Generated project file")
    
    print("\nAll files generated in", out_dir)


if __name__ == '__main__':
    main()