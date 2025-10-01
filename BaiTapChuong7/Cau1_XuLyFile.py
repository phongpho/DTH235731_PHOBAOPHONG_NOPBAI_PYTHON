def LuuFile(path, data):
    with open(path, 'a', encoding='utf-8') as file:
        file.writelines(data)
        file.writelines("\n")

def DocFile(path):
    arrProduct = []
    with open(path, 'r', encoding='utf-8') as file:
        for line in file:
            data = line.strip()
            if data:  
                arr = data.split(';')
                arr[2] = float(arr[2])
                arrProduct.append(arr)
    return arrProduct