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
