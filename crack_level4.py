from level4 import pos_pw_list, hash_pw, correct_pw_hash

for pos in pos_pw_list:
    pos_hash = hash_pw(pos)
    if pos_hash==correct_pw_hash:
        print(pos)
