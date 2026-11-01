class FoodRatings:
    class pqdata:
        def __init__(self, name, rating):
            self.name = name
            self.rating = rating

    def __init__(self, foods: list[str], cuisines: list[str], ratings: list[int]):
        self.hm1 = {}
        for i in range(len(foods)):
            self.hm1[foods[i]] = ratings[i]

        self.hm2 = {}
        for i in range(len(foods)):
            self.hm2[foods[i]] = cuisines[i]
        
        self.hm3 = {}
        for i in range(len(foods)):
            if cuisines[i] not in self.hm3:
                self.hm3[cuisines[i]] = []

            heapq.heappush(self.hm3[cuisines[i]], (-ratings[i], foods[i]))

    def changeRating(self, food: str, newRating: int) -> None:
        self.hm1[food] = newRating
        cat = self.hm2[food]
        
        heapq.heappush(self.hm3[cat], (-newRating, food))


    def highestRated(self, cuisine: str) -> str:
        pq = self.hm3[cuisine]

        while len(pq)>0:
            rating, itemName = pq[0]

            if self.hm1[itemName] != -rating:
                heapq.heappop(pq)
            else:
                return itemName

        return ""



# Your FoodRatings object will be instantiated and called as such:
# obj = FoodRatings(foods, cuisines, ratings)
# obj.changeRating(food,newRating)
# param_2 = obj.highestRated(cuisine)