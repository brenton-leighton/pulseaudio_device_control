# pulseaudio_device_control

A simple script to control PulseAudio devices.
Mainly this is to easily cycle the default sink or source.

## Installation

pulseaudio\_device\_control depends on [pulsectl](https://github.com/mk-fg/python-pulse-control).

This package can be installed using [pipx](https://pipx.pypa.io/stable/installation/):

```bash
pipx install pulseaudio_device_control
```

## Usage

```bash
pulseaudio_device_control OPERATION DEVICE_TYPE
```

Where:

- `OPERATION` is `raise`, `lower`, `mute`, or `next`
- `DEVICE_TYPE` is `sink` or `source`

When using `next` any device name ending with `monitor` is skipped.

## Configuration

pulseaudio_device_control can be configured with a file located at `~/.config/pulseaudio_device_control/config.ini`,
e.g.

```ini
[next]
# Ignore devices from the next command (devices ending in "monitor" are always ignored)
sink_ignore = ["sink_name1", "sink_name2"]
source_ignore = ["source_name1", "source_name2"]
```

The names of PulseAudio sink/source devices can be printed with:

```python
import pulsectl

pulse = pulsectl.Pulse()
print([sink.name for sink in pulse.sink_list()])
print([source.name for source in pulse.source_list()])
```
