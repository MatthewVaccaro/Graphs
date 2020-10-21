import random

class User:
    def __init__(self, name):
        self.name = name

class SocialGraph:
    def __init__(self):
        self.last_id = 0
        self.users = {}
        self.friendships = {}

    def add_friendship(self, user_id, friend_id):
        """
        Creates a bi-directional friendship
        """
        if user_id == friend_id:
            return -1
        elif friend_id in self.friendships[user_id] or user_id in self.friendships[friend_id]:
            return -1
        else:
            self.friendships[user_id].add(friend_id)
            self.friendships[friend_id].add(user_id)

    def add_user(self, name):
        """
        Create a new user with a sequential integer ID
        """
        self.last_id += 1  # automatically increment the ID to assign the new user
        self.users[self.last_id] = User(name)
        self.friendships[self.last_id] = set()

    def populate_graph(self, num_users, avg_friendships):
        """
        Takes a number of users and an average number of friendships
        as arguments

        Creates that number of users and a randomly distributed friendships
        between those users.

        The number of users must be greater than the average number of friendships.
        """
        # Reset graph
        self.last_id = 0
        self.users = {}
        self.friendships = {}
        
        for i in range(num_users):
            self.add_user(f'Person {i}')

        #  Loop over all users
        for user in range(1, num_users):
            # Get a num of friends (avg)
            friendShipAmount = random.randint(0, (avg_friendships * 2))
            # Loop number of friendships to add to the user
            for i in range(1, friendShipAmount):
                newFriend = random.randint(1, num_users)
                if self.add_friendship(user, newFriend) == -1:
                    friendShipAmount += 1
                else:
                    self.add_friendship(user, newFriend)


    def get_all_social_paths(self, user_id):
        """
        Takes a user's user_id as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """
        visited = {} 
        # Use a queue to keep track of future lists to check
        queue = [[user_id]]
        # Continue looping until everything has been checked
        while len(queue) > 0:
            # Remove from the queue be keep the value
            currentPath = queue.pop(0) 
            # Grab the most recent item
            currentVertex = currentPath[-1]
            # Add an key/value pair if it has been added
            if currentVertex not in visited:
                visited[currentVertex] = currentPath
                # Go through each item, make make path
                for n in self.friendships[currentVertex]:
                    pathCopy = currentPath.copy()
                    pathCopy.append(n)
                    queue.append(pathCopy)
        return visited

        


if __name__ == '__main__':
    sg = SocialGraph()
    sg.populate_graph(10, 2)
    print("->", sg.friendships)
    connections = sg.get_all_social_paths(1)
    print("----->", connections)
