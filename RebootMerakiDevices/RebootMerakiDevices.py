#! /usr/bin/env python

"""
This is a small script to reboot Meraki devices in a CSV file with fields of: serial number.
"""

import os
import csv
import meraki


def load_data(csv_file):
    """
    Load the CSV file and return a list
    :param csv_file:
    :return: return_list
    :rtype: list
    """
    print("Enter load_data")
    return_list = []
    with open(csv_file, 'r') as data:
        for line in csv.DictReader(data):
            print(line)
            return_list.append(line)
    return return_list

def reboot_device(device_list: list, dashboard_object: object) -> object:
    """
    Reboot the devices in the device_list in the dashboard instance dashboard_object.
    rtype: None
    """
    print("Enter reboot_device")
    for line in device_list:
        dashboard.devices.rebootDevice(
            serial=line['Serial']
            )
    return

if __name__ == '__main__':
    dashboard = meraki.DashboardAPI(api_key=os.environ.get('API-KEY'))
    reboot_device(load_data("sample_bulk_network_creator.csv"), dashboard)