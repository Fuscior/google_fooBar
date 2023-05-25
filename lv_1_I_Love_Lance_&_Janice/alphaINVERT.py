#"vmxibkgrlm"", when decoded, would become ""encryption"".

def solution(s):
    alphabet="abcdefghijklmnopqrstuvwxyz"
    alphabet_reversed="abcdefghijklmnopqrstuvwxyz"[::-1]
    decrypted=""

    length_encrypted= len(s)

    for i in range(length_encrypted):
        ascii_val= ord(s[i])

        if ascii_val > 96:
            decrypted= decrypted + alphabet_reversed[ascii_val - 97]
        else:
            decrypted= decrypted + s[i]

    return decrypted


s= "Yvzs! I xzm'g yvorvev Lzmxv olhg srh qly zg gsv xlolmb!!"

print(solution(s))    
