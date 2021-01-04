class Facebook:
    Username = ''
    setOfFollowers = set()
    numOfPosts = 0
    numOfLikes = 0
    def __init__(self, Username, setOfFollowers, numOfPosts, numOfLikes):
        self.Username = Username
        self.setOfFollowers = setOfFollowers
        self.numOfPosts = numOfPosts
        self.numOfLikes = numOfLikes

class Twitter:
    Username = ''
    setOfFollowers = set()
    numOfPostsG = 0
    numOfLikesG = 0
    def __init__(self, Username, setOfFollowers, numOfPosts, numOfLikes):
        self.Username = Username
        self.setOfFollowers = setOfFollowers
        self.numOfPosts = numOfPosts
        self.numOfLikes = numOfLikes

followersetL = set({"Bronny", "Anthony Davis", "Dwayne Wade", "Luka Doncic"})
Lebron = Facebook('kingjames', followersetL, 243, 898)
followersetG = set({"Bucks", "Lebron", "Luka Doncic", "Bronny", "Kawhi Leonard"})
Giannis = Twitter('superman', followersetG, 946, 1145)

print("In total, " , followersetL|followersetG , "Follow either lebron or Giannis, Lebron and Giannis have " , followersetL&followersetG , "following them")
print("Together, Lebron and Giannis have " , Lebron.numOfPosts + Giannis.numOfPosts , "posts.")
print("Together, Lebron and Giannis have ", Lebron.numOfLikes + Giannis.numOfLikes , "posts.")
print("Lebron's username is " , Lebron.Username , "." , sep = '')
print("Giannis's username is " , Giannis.Username , "." , sep = '')
