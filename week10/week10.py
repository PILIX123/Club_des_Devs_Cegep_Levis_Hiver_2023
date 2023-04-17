def XOR(chunk0, chunk1):
    return bytes(a ^ b for a, b in zip(chunk0, chunk1))


open('week10/disk1new.bin', 'wb').close()
open('week10/newImage.png', 'wb').close()
with open("week10/disk0.bin", mode="rb") as disk0, open("week10/disk2.bin", mode="rb") as disk2:
    chunk0 = disk0.read(256)
    chunk2 = disk2.read(256)
    while chunk0 and chunk2:
        with open("week10/disk1new.bin", "ab") as newPart1:
            val = newPart1.write(XOR(chunk0, chunk2))
        chunk0 = disk0.read(256)
        chunk2 = disk2.read(256)


with open("week10/disk0.bin", mode="rb") as disk0, open("week10/disk1new.bin", mode="rb") as disk1, open("week10/disk2.bin", mode="rb") as disk2:
    layers = 0
    chunk0 = disk0.read(256)
    chunk1 = disk1.read(256)
    chunk2 = disk2.read(256)
    while chunk0 and chunk1 and chunk2:
        if (layers % 3 == 0):
            with open("week10/newImage.png", "ab") as newImage:
                newImage.write(chunk0+chunk1)

        if (layers % 3 == 1):
            with open("week10/newImage.png", "ab") as newImage:
                newImage.write(chunk0+chunk2)

        if (layers % 3 == 2):
            with open("week10/newImage.png", "ab") as newImage:
                newImage.write(chunk1+chunk2)

        chunk0 = disk0.read(256)
        chunk1 = disk1.read(256)
        chunk2 = disk2.read(256)
        layers += 1
print("done")
