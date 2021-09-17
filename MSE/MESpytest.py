import os.path

save_path = "C:/Users/daich/Desktop/nandeck/wargame/MSE"
file_name = "MSEpytest.txt"
full_path = os.path.join(save_path, file_name)

cards = 1311

current = 1

f = open(full_path, "w")

f.write("\n1.0\n")

for i in range(cards):
    f.write("\nnormal\n")
    f.write(str(current)+"/"+str(cards)+"\n")
    f.write(str(0)+"\ncommon\n"
            +"blu_"+str(current).zfill(4)+"\n" # name of card "blu_0001"
            +"colorless"
            +"\n\n\n\n\n\n\n\n\n"
            +"colorless"
            +"\n\n\n\n\n\n\n\n"
            +"===========")
    current = current + 1

f.close()