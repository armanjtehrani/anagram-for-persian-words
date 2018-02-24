output_file = open("db/database", "w")
ad_file = open("db/Adjectives", "r")
moi_file = open("db/Moin_Key_Words", "r")
verb_file = open("db/Persian Verbs List", "r")
know_file = open("db/to know", "r")
wc1_file = open("db/Word_collection_1", "r")
wwa_file = open("db/Words with a", "r")
wwv_file = open("db/Words with v", "r")
wrong_file = open("db/wrong", "r")

ad = ad_file.read()
moi = moi_file.read()
verb = verb_file.read()
know = know_file.read()
wc1 = wc1_file.read()
wwa = wwa_file.read()
wwv = wwv_file.read()
wrong = wrong_file.read()
final = ad + '\n' + \
        moi + '\n' + \
        verb + '\n' + \
        know + '\n' + \
        wc1 + '\n' + \
        wwa + '\n' + \
        wwv + '\n' + \
        wrong
output_file.write(final)
