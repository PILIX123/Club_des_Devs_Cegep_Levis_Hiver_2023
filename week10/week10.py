import time


def XOR(chunk0, chunk1):
    return bytes(a ^ b for a, b in zip(chunk0, chunk1))


with open("week10/disk0.bin", mode="rb") as disk0, open("week10/disk1.bin", mode="rb") as disk1, open("week10/disk2.bin", mode="rb") as disk2:
    print(len(disk0.read()))
    print(len(disk1.read()))
    print(len(disk2.read()))

with open("week10/disk0.bin", mode="rb") as disk0, open("week10/disk2.bin", mode="rb") as disk2:
    chunk0 = disk0.read(256)
    chunk2 = disk2.read(256)

    disk1ok = 0
    disk0ok = 0
    disk2ok = 0
    layers = 0
    while chunk0 and chunk2:
        print("fixing")
        with open("week10/disk1new.bin", "ab") as newPart1:
            val = newPart1.write(XOR(chunk0, chunk2))
            print(val)
        chunk0 = disk0.read(256)
        chunk2 = disk2.read(256)
        layers += 1
print(layers)
layers = 0
print("using new disk")
with open("week10/disk0.bin", mode="rb") as disk0, open("week10/disk1new.bin", mode="rb") as disk1, open("week10/disk2.bin", mode="rb") as disk2:
    print(len(disk0.read()))
    print(len(disk1.read()))
    print(len(disk2.read()))

with open("week10/disk0.bin", mode="rb") as disk0, open("week10/disk1new.bin", mode="rb") as disk1, open("week10/disk2.bin", mode="rb") as disk2:
    chunk0 = disk0.read(256)
    chunk1 = disk1.read(256)
    chunk2 = disk2.read(256)
    while chunk0 and chunk1 and chunk2:
        if (layers % 3 == 0):
            print("chunk0+1")
            with open("week10/newImage.png", "ab") as newImage:
                newImage.write(chunk0)
            with open("week10/newImage.png", "ab") as newImage:
                newImage.write(chunk1)

        if (layers % 3 == 1):
            print("chunk0+2")
            with open("week10/newImage.png", "ab") as newImage:
                newImage.write(chunk0)
            with open("week10/newImage.png", "ab") as newImage:
                newImage.write(chunk2)

        if (layers % 3 == 2):
            print("chunk1+2")
            with open("week10/newImage.png", "ab") as newImage:
                newImage.write(chunk1)
            with open("week10/newImage.png", "ab") as newImage:
                newImage.write(chunk2)

        chunk0 = disk0.read(256)
        chunk1 = disk1.read(256)
        chunk2 = disk2.read(256)
        layers += 1
print("done")
