#!/usr/bin/env python3


import sys
from enum import Enum
import pulsectl


class Operation(Enum):
    RAISE = 1
    LOWER = 2
    MUTE = 3
    NEXT = 4


class DeviceType(Enum):
   SINK = 1
   SOURCE = 2


def print_usage():
  print("Usage: pulseaudio_device_control OPERATION DEVICE_TYPE")
  print("    OPERATION: \"raise\", \"lower\", \"mute\", or \"next\"")
  print("    DEVICE_TYPE: \"sink\" or \"source\"\n")


# Parse arguments and return "operation" and "device type"
def parse_arguments():

    if len(sys.argv) != 3:
        print("Incorrect number of arguments\n")
        print_usage()
        sys.exit(1)

    operation = None

    match sys.argv[1]:
        case "raise":
            operation = Operation.RAISE
        case "lower":
          operation = Operation.LOWER
        case "mute":
          operation = Operation.MUTE
        case "next":
          operation = Operation.NEXT
        case _:
          print("Unknown operation " + sys.argv[1] + "\n")
          print_usage()
          sys.exit(1)

    device_type = None

    match sys.argv[2]:
        case "sink":
            device_type = DeviceType.SINK
        case "source":
            device_type = DeviceType.SOURCE
        case _:
            print("Unknown device type " + sys.argv[2] + "\n")
            print_usage()
            sys.exit(1)

    return operation, device_type


def raise_volume(pulse, device):

  if device.mute:
    pulse.mute(device, False)

    if device.volume.value_flat != 0.:
        return

  pulse.volume_change_all_chans(device, 0.06)


def lower_volume(pulse, device):

    pulse.volume_change_all_chans(device, -0.06)

    if device.volume.value_flat == 0.:
        pulse.mute(device)


def toggle_mute(pulse, device):

    pulse.mute(device, not device.mute)


def next_device(pulse, device_list, default_device_name):

    if len(device_list) == 1:
        return

    next_idx = 0

    # Find the default device
    for idx, device in enumerate(device_list):
        if device.name == default_device_name:
            # Save the index of the next device
            next_idx = idx + 1
            break

    # Wrap around
    if next_idx >= len(device_list):
        next_idx = 0

    # Set the default device
    pulse.default_set(device_list[next_idx])


def main():

    operation, device_type = parse_arguments()

    with pulsectl.Pulse('pulseaudio_device_control', threading_lock=True) as pulse:

        device_list = pulse.sink_list() if device_type == DeviceType.SINK \
            else pulse.source_list()

        default_device_name = pulse.server_info().default_sink_name if device_type == DeviceType.SINK \
            else pulse.server_info().default_source_name

        if operation == Operation.NEXT:
            next_device(pulse, device_list, default_device_name)

        else:  # raise, lower, or mute

            # Find the default device
            for device in device_list:
                if device.name == default_device_name:
                    match operation:
                        case Operation.RAISE:
                            raise_volume(pulse, device)
                        case Operation.LOWER:
                            lower_volume(pulse, device)
                        case Operation.MUTE:
                            toggle_mute(pulse, device)


if __name__ == '__main__':
    main()
