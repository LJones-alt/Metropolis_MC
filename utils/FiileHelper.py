from time import gmtime, strftime

class FileHelper:
    def __init__(self):
        self.filename = self.get_file_name


    def write_list_to_file(self, save_list):
        filename = self.get_file_name() + ".txt"
        f= open(filename, "w")
        for i in range(len(save_list)):
            f.write(save_list[i])
        f.close
        print(f"Saved to {filename}")
    
    def get_file_name(self):
        return strftime("%m-%d-%H-%M-%S", gmtime())