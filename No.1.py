#Recursive
def tampilkanAngka (batas, i = 1):
  print(f'Perulangan ke {i}')

  if (i < batas):
    tampilkanAngka(batas, i + 1)

tampilkanAngka(10)


#Function
def my_function(fname):
  print(fname + " tugas_uas")

my_function("Luthfi Kristianto")
my_function("20210801240")
my_function("Teknik Informatika")
