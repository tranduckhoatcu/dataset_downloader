import argparse
import requests
from nordvpn_switcher import initialize_VPN,rotate_VPN

def download(list_urls, image_name='firesmoke_new'):
    # instructions = initialize_VPN(area_input=['Vietnam','Hong Kong','Singapore','Thailand'], skip_settings=1)
    # rotate_VPN(instructions)
    for i, j in enumerate(list_urls):
        # if (i % 300 == 0):
            # rotate_VPN(instructions)
        image_data = requests.get(j)
        try:
            image_data.raise_for_status()
        except Exception as e:
            print('There is a problem with this image: ' + e)

        image_file = open('dataset/'+image_name+'_'+str(i)+'.jpg', 'wb')
        for chunk in image_data.iter_content(100000):
            image_file.write(chunk)
        image_file.close()
        print(image_name+'_'+str(i)+' downloaded!', end='\n\n')

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--txt-path', type=str, default = "image_url_list_full.txt")
    args = parser.parse_args()

    with open(args.txt_path) as f:
        print('Working with '+args.txt_path+' file...')
        lines = [line.rstrip() for line in f]
    download(lines)
    