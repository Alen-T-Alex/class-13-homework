book_list=[]
for i in range(4):
    book=input(f"what movie do u plan on watching?? {i+1} :")
    book_list.append(book)
print(book_list)
book_read=input("what books have you read so far")
book_list.remove(book_read)
print(book_list)
for i in book_list:
    print(i)