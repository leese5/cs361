if __name__ == '__main__':
    while True:
        data_file = 'data.txt'

        f = open('input.txt', 'r')
        line = f.readline()
        f.close()
        if line != '':
            data = line.strip('n')
            data = data.split(',')
            zip = data[0]
            model = data[1]
            year = data[2]
            

            with open(data_file, 'r') as f:
                for line in f.readlines():
                    data = line.strip('n')
                    data = data.split(',')

                    if data[0] == zip:
                        if data[1] == model:
                            if data[2] == year:
                                g = open('pipe.txt', 'w')
                                print(data[3])
                                g.write(f"{data[3]}" + "\n")
                                g.close()
        f = open('input.txt', 'w')
        f.write('')
        f.close()
                    

        