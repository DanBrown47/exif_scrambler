from exif import Image

class scrambler():
    def random(filename):
        # Have a progress banner here
        with open(filename,'rb') as target_file:
            target = Image(target_file)

        if(target.has_exif):    
            print("Has Exif")

            exif_list = []
            exif_list = dir(target)
            for i in range(len(exif_list)):
                user_comment = exif_list[i]
                print(type(target))
            # for i in range(20):
            #     head = exif_list[i]
            #     print(head)
            #     # print(target.x)
        else:
            print("Dosent have exif")