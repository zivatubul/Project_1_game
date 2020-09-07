import os.path
import os
import Utils
def add_score(points):
    score_file = Utils.SCORES_FILE_NAME
    # if os.path.isfile(score_file ):
    #     file = open(score_file )
    #     number = int(file.read())
    #     new_points = number + points
    #     file.open(score_file , "w+")
    #     file.write(str(new_points))
    # else:
    #     file = open(score_file , "w")
    #     file.write(str(points))



    if os.path.exists(score_file):
        score_file_txt = open(score_file, 'r+')
        score_file_txt.write(str(points))
    else:
        score_file_txt = open(score_file, 'w')
        score_file_txt.write(str(points))
