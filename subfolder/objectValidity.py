# This function will call all the user story functions (from userStories folder's scripts)
# Returns true only if every story checks out, or returns false
from subfolder.userStories.UserStoriesVD import DatebeforeCurrentDate
from subfolder.userStories.UserStoriesVD import MarriageAfter14
from subfolder.userStories.UserStoriesDP import us2
from subfolder.userStories.UserStoriesDP import us8



def objectvalid(indi, fam):
    DatebeforeCurrentDate(indi, fam)
    MarriageAfter14(indi, fam)
    us2(indi, fam)
    us8(indi, fam)
    return True
