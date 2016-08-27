
import open_file
import sendfile

def generate(filepath, in_fd='r6', out_fd=4):
    """cat a file like UNIX Command

    Args: 
        filepath (str)  : target file name
        in_fd  (int/str): in  file descriptor (default: 'r6' indicates a file descriptor)
        out_fd (int/str): out file descriptor (default: 4)
    """
    sc  = open_file.generate(filepath)
    sc += sendfile.generate(in_fd, out_fd)
    return sc
