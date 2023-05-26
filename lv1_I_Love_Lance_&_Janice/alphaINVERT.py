#"vmxibkgrlm"", when decoded, would become ""encryption"".

def solution(x):
    alphabet="abcdefghijklmnopqrstuvwxyz"
    alphabet_reversed="abcdefghijklmnopqrstuvwxyz"[::-1]
    decrypted=""

    length_encrypted= len(x)

    for i in range(length_encrypted):
        ascii_val= ord(x[i])

        if ascii_val > 96:
            decrypted= decrypted + alphabet_reversed[ascii_val - 97]
        else:
            decrypted= decrypted + x[i]

    return decrypted


s= "wrw blf hvv ozhg mrtsg'h vkrhlwv?"

print(solution(s))    
