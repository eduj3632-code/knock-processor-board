# Standalone Hellen-One Knock Processor Board

Dual-channel knock sensor pre-amplifier board based on rusefi/hellen-miata-NB2 design.

## Specifications
- **Channels**: 2 independent knock pre-amp circuits
- **Op-amps**: LMV321IDBVR (SOT-23-5) × 2 per channel
- **Input**: 2x 2-pin header (IN_KNOCK1, IN_KNOCK2 + GND)
- **Output**: 3.5mm TRS audio jack (Tip=CH1, Ring=CH2, Sleeve=GND)
- **Power**: 5V analog supply (V5A), GNDA
- **Board size**: 60mm x 40mm

## Circuit Topology per Channel
```
IN_KNOCK → C_coupling → R_input → OpAmp conditioning
                                    ↓
                              OUT_KNOCK → Jack tip/ring
```

## Bill of Materials

| Ref | Value | Footprint | LCSC | Description |
|-----|-------|-----------|------|-------------|
| U470 | LMV321IDBVR | SOT-23-5 | C7972 | Op-amp channel 1 |
| U471 | LMV321IDBVR | SOT-23-5 | C7972 | Op-amp channel 2 |
| R470 | 470k | R_0603 | C23178 | Feedback resistor ch1 |
| R471 | 100k | R_0603 | C25803 | Input resistor ch1 |
| C470 | 100n | C_0603 | C14663 | Decoupling capacitor |
| C471 | 3.3n | C_0603 | C1613 | Input coupling ch1 |
| C472 | 330p | C_0603 | C1664 | Feedback cap ch1 |
| R472 | 12k | R_0603 | C22790 | Series resistor ch2 |
| R473 | 100k | R_0603 | C25803 | Feedback resistor ch2 |
| R474 | 33k | R_0603 | C4216 | Pull-down ch2 |
| C473 | 47p | C_0603 | C1671 | Input filter ch2 |
| C474 | 680p | C_0603 | C1630 | Output filter ch2 |
| J1 | PinHeader_1x02 | PinHeader_1x02_P2.54mm | - | CH1 input |
| J2 | PinHeader_1x02 | PinHeader_1x02_P2.54mm | - | CH2 input |
| J3 | Jack_3.5mm | Jack_3.5mm_Triple | - | Audio output |
| J4 | PinHeader_1x02 | PinHeader_1x02_P2.54mm | - | Power input |

## References
- Source: rusefi/hellen-miata-NB2 (hellen1-knock.kicad_sch)
- Module symbol: hellen-one/modules/knock/0.1/
- Platform: Hellen-One by rusEFI
