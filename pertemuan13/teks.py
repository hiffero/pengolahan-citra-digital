def compress_rle(text):
    compressed_text = ""
    count = 1

    # Iterasi melalui teks dari indeks 1 hingga akhir
    for i in range(1, len(text)):
        # Jika karakter saat ini sama dengan karakter sebelumnya, tambahkan ke hitungan kemunculan
        if text[i] == text[i - 1]:
            count += 1
        else:
            # Jika karakter saat ini berbeda, tambahkan pasangan karakter dan hitungan kemunculannya ke teks hasil kompresi
            compressed_text += text[i - 1] + str(count)
            count = 1

    # Menambahkan pasangan karakter terakhir dan hitungan kemunculannya
    compressed_text += text[-1] + str(count)

    return compressed_text

input_text = "CCCCCHAEEEEEL"
compressed_text = compress_rle(input_text)
print("Teks hasil kompresi: " + compressed_text)
