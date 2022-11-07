# Nama  : i'in mardhiana
# Nim   : 222410102007

# tugas 1
from codecs import ascii_encode

print("-"*29)
print("| \t  TUGAS 1\t\t|")
print("-"*29,"\n")

inp1 = input("masukkan nama mu : ") 
inp2 = input("masukkan nama dia : ")
a = [ord(c) for c in inp1] 
b = [ord(c) for c in inp2] 


#badan inp1
print(f"\nHasil cek [{inp1}] :")
for i in range(0,len(a)-1):
    x=a[i]
    y=a[i+1]
    if x<y:
        selisih=y-x
        print(f"{inp1[i]} kurang dari {inp1[i+1]}, selisihnya ialah {selisih}")
    elif x>y:
        selisih=x-y
        print(f"{inp1[i]} lebih dari {inp1[i+1]}, selisihnya ialah {selisih}")


#badan inp2
print(f"\nHasil cek [{inp2}] :")
for i in range(0,len(b)-1):
    x=a[i]
    y=a[i+1]
    if x<y:
        selisih=y-x
        print(f"{inp2[i]} kurang dari {inp2[i+1]}, selisihnya ialah {selisih}")
    elif x>y:
        selisih=x-y
        print(f"{inp2[i]} lebih dari {inp2[i+1]}, selisihnya ialah {selisih}")


