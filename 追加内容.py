


with open(r"log.txt",mode="ab")as f:
    f.write("xxx转账100元\n".encode("utf-8"))
    print(f.tell())
