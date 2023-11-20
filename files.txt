def exsit(b, f):
    """
    Function to check if current line exist in file
    :param b: the line we want
    :param f:the file name
    :return: True if the line  was found and False if not
    """
    for line in f:
        line = line.split()

        if line[0] == b:
            res = line[1]
            return res


