# python script to read the .env file from config

config_file = r'config/CONFIG.env'
timestamp_key = 'timestamp'

if __name__ == "__main__":
    try:
        with open(config_file, 'r') as f:
            for line in f:
                entry = line.strip().split('=')
                if entry[0] == timestamp_key:
                    print(f'--{entry[1]}')
                    break
    except FileNotFoundError:
        print(f'{config_file} does not exist')