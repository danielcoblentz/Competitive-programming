def make_adjacency_list(rooms: list, connections: list) -> list[list]:
    adj = [[] for _ in range(26)]

    for conn in connections:
        # Turn alphabetic values to numbers with 'A' = 0,
        # 'B' = 1, ..., 'Z' = 25
        p1 = ord(conn[0]) - ord('A')
        p2 = ord(conn[1]) - ord('A')

        # Each index contains the list of connected rooms and
        # their respective collapse steps
        adj[p1].append(rooms[p2])
        adj[p2].append(rooms[p1])

    return adj


def escape(cave):
    rooms, connections = cave
    adj = make_adjacency_list(rooms, connections)

    path = escape_helper(rooms, adj, rooms[0], 0, "")
    if path == "":
        print("There is no escape!")
    else:
        print(f"Montana can escape: {path}")


def escape_helper(rooms: list[tuple], adj: list[list],
                  current_room: tuple, step: int, path: str) -> str:
    # Get letter and collapse step of current room
    room_letter, collapse_step = current_room
    room_ord = ord(room_letter) - ord('A')

    # Add current room's letter to path
    path += room_letter

    if step >= collapse_step:
        # Montana has entered a caved-in room - turn back
        return ""
    elif current_room == rooms[-1]:
        # Montana has escaped
        return path
    else:
        # Recurse through the connecting rooms
        for connection in adj[room_ord]:
            potential_path = escape_helper(rooms, adj, connection,
                                           step + 1, path)
            if potential_path != "":
                return potential_path

        return ""


if __name__ == "__main__":
    n = int(input())  # number of cave systems
    caves: list[tuple[list[tuple[str, int]], list[str]]] = []

    for _ in range(n):
        num_rooms = int(input())  # number of rooms in cave system
        rooms = []

        # Get all rooms from input
        for _ in range(num_rooms):
            letter, number = input().split()

            # Each room is a tuple of (letter, collapse_step)
            rooms.append((letter, int(number)))

        num_connections = int(input())
        connections = []

        # Get all connections from input
        for _ in range(num_connections):
            conn = input()
            connections.append(conn)

        # Each item in `caves` is a tuple of rooms and connections
        caves.append((rooms, connections))

    # Iterate through all caves
    for cave in caves:
        escape(cave)
