def rle_compress(text):
    compressed_text = ""
    count = 1
    n = len(text)
    
    for i in range(1, n + 1):
        if i < n and text[i] == text[i - 1]:
            count += 1
        else:
            compressed_text += text[i - 1] + str(count)
            count = 1
    
    return compressed_text


def rle_decompress(compressed_text):
    decompressed_text = ""
    n = len(compressed_text)
    i = 0
    
    while i < n:
        char = compressed_text[i]
        i += 1
        
        count = ""
        while i < n and compressed_text[i].isdigit():
            count += compressed_text[i]
            i += 1
        
        decompressed_text += char * int(count)
    
    return decompressed_text


text = "AKUUUUUPACARRRRJIMIIIIINN"

# Kompresi teks
compressed_text = rle_compress(text)
print("Teks terkompresi:", compressed_text)

# Dekompresi teks
decompressed_text = rle_decompress(compressed_text)
print("Teks terdekompresi:", decompressed_text)
