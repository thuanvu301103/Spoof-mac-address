import macaddr

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Python Windows MAC changer")
    parser.add_argument("-r", "--random", action="store_true", help="Whether to generate a random MAC address")
    parser.add_argument("-m", "--mac", help="The new MAC you want to change to")
    args = parser.parse_args()
    if args.random:
        # if random parameter is set, generate a random MAC
        new_mac_address = macaddr.get_random_mac_address()
    elif args.mac:
        # if mac is set, use it after cleaning
        new_mac_address = macaddr.clean_mac(args.mac)
    
    connected_adapters_mac = macaddr.get_connected_adapters_mac_address()
    old_mac_address, target_transport_name = macaddr.get_user_adapter_choice(connected_adapters_mac)
    print("[*] Old MAC address:", old_mac_address)
    adapter_index = macaddr.change_mac_address(target_transport_name, new_mac_address)
    print("[+] Changed to:", new_mac_address)
    macaddr.disable_adapter(adapter_index)
    print("[+] Adapter is disabled")
    macaddr.enable_adapter(adapter_index)
    print("[+] Adapter is enabled again")
