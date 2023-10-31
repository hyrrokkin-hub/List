my_list = []

while True:
    print("Menu:\n1. Buat List\n2. Lihat List\n3. Edit List\n4. Hapus List\n5. Keluar")
    choice = input("Pilih menu (1/2/3/4/5): ")

    if choice == "1":
        my_list.append(input("Elemen: "))
        print("Elemen ditambahkan ke list.")

    elif choice == "2":
        if my_list: [print(f"{i}. {item}") for i, item in enumerate(my_list, 1)]
        else: print("List kosong.")

    elif choice == "3":
        if my_list: 
            index = int(input("Indeks elemen yang ingin diubah: "))
            if 1 <= index <= len(my_list): my_list[index - 1] = input("Elemen baru: "); print("Elemen diubah.")
            else: print("Indeks tidak valid.")
        else: print("List kosong. Tidak ada yang bisa diubah.")

    elif choice == "4":
        if my_list: 
            index = int(input("Indeks elemen yang ingin dihapus: "))
            if 1 <= index <= len(my_list): removed_item = my_list.pop(index - 1); print(f"Elemen '{removed_item}' dihapus.")
            else: print("Indeks tidak valid.")
        else: print("List kosong. Tidak ada yang bisa dihapus.")

    elif choice == "5":
        print("Keluar dari program."); break

    else: print("Pilihan tidak valid. Silakan pilih menu yang sesuai.")
