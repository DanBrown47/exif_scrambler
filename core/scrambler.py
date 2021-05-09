from exif import Image
import random, string

class scrambler():

    def random():
        x = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(16))
        print(x)



    def valid_exif_checker(filename):
        # Have a progress banner here
        with open(filename,'rb') as target_file:
            target = Image(target_file)

        if(target.has_exif):    
            print("Has Exif")

            exif_list = []
            exif_error = []
            values = []
            exif_list = dir(target)
            for i in range(len(exif_list)):
                key = exif_list[i]
                try:
                    values.append(getattr(target, key))
                except Exception as e:
                    exif_error.append(key)
                    # Ad
                    #d debuger
            # print(exif_error)  ## Error
            clean_arr = [i for i in exif_list if i not in exif_error]
            return clean_arr
    def main(filename):
        clean_exif = scrambler.valid_exif_checker(filename)
        scrambler.random()




