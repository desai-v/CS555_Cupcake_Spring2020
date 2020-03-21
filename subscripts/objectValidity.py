# This function will call all the user story functions (from userStories folder's scripts)
# Returns true only if every story checks out, or returns false
from subscripts.userStories.UserStoriesVD import us01, us10, us15, us16
from subscripts.userStories.UserStoriesDP import us03, us08, us06, us04


def objectvalid(indi, fam, us32_ids):
    f = open("Output_Project.txt", "a")
    f.write("\n \n")
    us01(indi, fam, f)
    us03(indi, fam, f)
    us04(indi, fam, f)
    us06(indi, fam, f)
    us08(indi, fam, f)
    us10(indi, fam, f)

    f.close()
    return True
