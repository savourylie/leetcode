class Solution:
    def canVisitAllRooms(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: bool
        """

        key_set = set([0])
        _ = self.find_keys(rooms, key_set, 0)

        return True if len(key_set) == len(rooms) else False

    def find_keys(self, rooms, key_set, room_num):
        if not rooms[room_num]:
            return

        while len(rooms[room_num]) > 0:
            key = rooms[room_num][0]
            key_set.add(key)
            rooms[room_num].pop(0)
            _ = self.find_keys(rooms, key_set, key)

        return