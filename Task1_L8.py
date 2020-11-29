import hashlib


def deli_str(a):
    b = []
    len_a = int(len(a))
    z = 0
    hash_a = hashlib.sha256(a.encode('utf-8')).hexdigest()
    hash_empty = hashlib.sha256(''.encode('utf-8')).hexdigest()
    while z < len_a:
        z += 1
        for i in range(len_a):
            s = hashlib.sha256(a[i:z].encode('utf-8')).hexdigest()
            if s == hash_empty or s == hash_a or s in b:
                continue
            else:
                b.append(s)

    return f"Количество различных подстрок в строке {a} = {len(b)}"


# print(deli_str(input("Введи строку для поиска кол-ва подстрок в ней: ")))
print(deli_str("sova"))
