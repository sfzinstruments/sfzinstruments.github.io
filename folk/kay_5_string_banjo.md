---
title:  "Kay 5-String Banjo"
layout: "sfz/instrument"
---
## Details

This version of the FlameStudios Kay 5-String Banjo was converted from the
original GigaSampler version by [S. Christian Collins]. The accompanying PDF file
(FS Kay 5-String Banjo presets list.pdf) describes the behavior of the original
GigaSampler version. While most of the information presented there still applies
to the SFZ conversion, a few changes have been made when creating the SFZ version:

* In "FS KayBanjo (release mw1).sfz", a key switch has been added on notes C2
  and D2 (middle C = C4):
  - **C2** (default): The banjo's note range is C3 through E6 with note G4 being
    the string 5 sample. String 5 is the short string that is usually played
    with the thumb, alternating between the other fingers for that classic banjo
    sound. This sample assignment causes G4 to have a different tone than the
    neighboring notes, which are using string 1 samples.
  - **D2**: In this keyswitch, note G4 uses the string 1 sample, similar to its
    neighboring notes. The string 5 G4 sample is placed both below (F2-A2) and
    above (F6-A6) the normal banjo note range to facilitate an alternating-hand
    play style with one hand on the string 5 sample and the other playing the
    other four strings spread from C3 through E6. The string 5 sample normally
    only provides the pitch G4, but I have stretched it a whole step in each
    direction to cover notes F through A.
* In "FS KayBanjo (release mw1).sfz", the white keys C7 through A7 feature
  various harmonics and muted string effects that were included in the original
  GigaSampler file but never mapped to any keys.
* All samples have been edited to reduce noise and distortion.
  You can still hear distortion on a few samples due to the significant clipping
  on the originals. Other noises are occasionally present due to the recording
  having been made in a noisy environment. Despite these flaws, the audio quality
  has been greatly improved from the original version.

## Requirements

This SFZ instrument was developed for use with the ARIA engine, freely available
in the [Plogue Sforzando VSTi]. I don't know how well it will work with other
SFZ samplers such as LinuxSampler or sfizz. Your mileage may vary.

[S. Christian Collins]:  http://www.schristiancollins.com
[Plogue Sforzando VSTi]: https://www.plogue.com/products/sforzando.html
