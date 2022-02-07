from level5 import hash_pw, correct_pw_hash

with open("dictionary.txt", "r") as fp:
    for pos in fp:
        pos = pos.strip() # 行末の改行を削除
        pos_hash = hash_pw(pos)
        if pos_hash==correct_pw_hash:
            print(pos)
