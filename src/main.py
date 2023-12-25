from usc import UniShiftCipher as usc
import argparse
import time

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--message', '--m',  help='This is the message to be encrypted')
    parser.add_argument('--shift','--s', type=int, default=19, help='This is the integer value The integer value representing the shift for the UniShiftCipher. Choose a positive integer between 1 and 26 for encryption or decryption. For example, --shift 3 would shift the alphabet characters by 3 positions in an increasing order.')
    parser.add_argument('--mode', choices=['encrypt', 'decrypt'], help='Specify whether to encrypt or decrypt the message.')
    parser.add_argument('--output', '-o ', help='Specify the output file for the result.')
    parser.add_argument('--verbose', '-v', action='store_true', help='Enable verbose output')
    parser.add_argument('--rotation', type=int, default=0, help='Specify the starting position of the alphabet.')
    parser.add_argument('--keyfile', help='Specify the path to the keyfile.')
    parser.add_argument('--output-format', choices=['plaintext', 'hex', 'base64'])
    args = parser.parse_args()

    if args.message and args.shift and args.mode:
        cipher = usc()

        if args.keyfile:
            pass
        if args.mode == 'encrypt':
            result = cipher.encrypt(args.message, args.shift, args.rotation, args.output, args.output_format)
        elif args.mode == 'decrypt':
            result= cipher.decrypt(args.message, args.shift, args.rotation, args.output, args.output_format)
       
        if args.output:
            with open(args.output, 'w') as output_file:
                output_file.write(result)
        else:
            print(result)
        
        if args.verbose:
            print(f'Mode: {args.mode}')
            print(f'Shift: {args.shift}')
            print(f'Rotation: {args.rotation}')
            print(f'Keyfile: {args.keyfile}')

            start_time = time.time()
        # ... perform encryption or decryption ...
            end_time = time.time()
            print(f'Time Taken: {end_time - start_time} seconds')
    else:
        print("Missing on required arguments. Please provide all 3 correctly (Message, Mode and Shift)")

    
if __name__== "__main__":
    main()  