import random
def convert_to_binary(num):
    result=""
    while num!=0:
        remainder=num%2
        num=num//2
        result=str(remainder)+result
    while len(result)!=8:
        result="0"+result  
    return result

def xor_operation(val1,val2):
    result=""
    val1=convert_to_binary(val1)
    val2=convert_to_binary(val2)
    for i in range(0,len(val1)):
        if val1[i]==val2[i]:
            result+="0"
        else:
            result+="1"
    return convert_to_decimal(result)

def convert_to_decimal(binary_str):
    length = len(binary_str)
    result = 0
    power = 0
    for i in range(length-1, -1, -1): 
        result += int(binary_str[i]) * 2**power
        power += 1
    return result

def encrypt_data(seed_value, input_text):
    input_text = list(str(input_text))
    random.seed(seed_value)       
    key_list = []
    encrypted_text = ""
    for i in range(0, len(input_text)):
        key_list.append(random.randint(0, 255))  
        encrypted_text+=chr(xor_operation(ord(input_text[i]), key_list[i]))
    return encrypted_text 

def decrypt_data(seed_value, encrypted_text):
    encrypted_text = list(str(encrypted_text))
    random.seed(seed_value)       
    key_list = []
    decrypted_text = ""
    for i in range(0, len(encrypted_text)):
        key_list.append(random.randint(0, 255))  
        decrypted_text+=chr(xor_operation(ord(encrypted_text[i]), key_list[i]))
    return decrypted_text
```