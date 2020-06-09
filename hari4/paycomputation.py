
def pay_computation(jam_kerja, gaji_per_jam):
    
    if jam_kerja > 40:
        bonus = (jam_kerja - 40) * gaji_per_jam * 1.5
        return 40 * gaji_per_jam + bonus
    else:
        return jam_kerja * gaji_per_jam

print(pay_computation(40, 100000)) 