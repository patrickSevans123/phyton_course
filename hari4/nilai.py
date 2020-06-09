def classed(dictionary):
    for key.val in dictionary.items():
        print('{} : {}'), format(key,val)
    
students=[]

while True:
    student = {}

    nama = input ("Masukan nama")
    nilai = int(input("Masukan nilai:"))

    if nilai >=90:
        grade_kamu = "A"
    
    elif nilai >=80 and nilai <90:
        grade_kamu = "B"
    
    elif nilai>=70 and nilai <80:
        grade_kamu = "C"
    
    else:
        grade_kamu = "F"

    student['nama'] = nama
    student['nilai'] = nilai
    student['grade'] = grade_kamu
    
    graddes.append(student)

    another = input("Ada yang mau ditambahkan? (yes/no")

    if another == 'yes':
        continue
    else:
        break