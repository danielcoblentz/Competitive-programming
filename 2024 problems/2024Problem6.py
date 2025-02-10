# Constants
speed_human = 4   # meters / second
speed_wolf  = 10  # meters / second
door_human  = 1   # seconds
door_wolf   = 8   # seconds
transform   = 5   # seconds

# When currently in front of a door, ninimum distance to the next door 
# at which it is optimal to stay as a wolf rather than transform into a 
# human to open the door.
# i.e., any lower distance than this means it will be more optimal to
# turn into a human before opening the door
door_cutoff = 40/3  # meters

# After a door, minimum distance to the next door at which it is
# optimal to transform into a wolf and run to the door rather than
# remain as a human
# i.e., any lower than this distance means it will be more optimal to
# remain human and just run to the door
run_cutoff = 100/3  # meters

def calculate(hall: dict) -> tuple[float, int]:
    def run(dist: float, pos: float, door_positions: list, is_wolf: bool, 
            time: float, transformations: int) -> tuple[float, int]:
        # Base case
        if not door_positions:
            # No doors left, check if it would be faster to transform now
            dont_transform = (dist - pos) / (speed_wolf if is_wolf else speed_human)
            do_transform = (dist - pos) / (speed_human if is_wolf else speed_wolf) + transform

            if dont_transform < do_transform:
                # Not transforming is faster
                return time + dont_transform, transformations
            else:
                # Transforming is faster
                return time + do_transform, transformations + 1
        
        dist_to_next_door = door_positions[0] - pos
        if len(door_positions) > 1:
            dist_to_door_after = door_positions[1] - door_positions[0]
        else:
            dist_to_door_after = dist - door_positions[0]

        if not is_wolf:
            if dist_to_next_door > run_cutoff:
                if dist_to_door_after > door_cutoff:
                    # Transform into a wolf, run, open door as wolf
                    return run(dist, pos + dist_to_next_door,
                               door_positions[1:], not is_wolf,
                               time + transform + dist_to_next_door/speed_wolf + door_wolf,
                               transformations + 1)
                else:
                    # Transform into a wolf, run, transform into human, open door as human
                    return run(dist, pos + dist_to_next_door,
                               door_positions[1:], is_wolf,
                               time + transform*2 + dist_to_next_door/speed_wolf + door_human,
                               transformations + 2)
            else:
                # Remain human, run, open door as human
                return run(dist, pos + dist_to_next_door,
                           door_positions[1:], is_wolf,
                           time + dist_to_next_door/speed_human + door_human,
                           transformations)
        else:
            if dist_to_next_door > run_cutoff:
                # Remain as wolf, run, open door as wolf
                return run(dist, pos + dist_to_next_door,
                           door_positions[1:], is_wolf,
                           time + dist_to_next_door/speed_wolf + door_wolf,
                           transformations)
            else: 
                # Remain as wolf, run, transform into human, open door as human
                return run(dist, pos + dist_to_next_door,
                           door_positions[1:], not is_wolf,
                           time + dist_to_next_door/speed_wolf + transform + door_human,
                           transformations + 1)


    door_positions = hall["door_positions"]
    dist = hall["dist"]
    return run(dist, 0, door_positions, False, 0, 0)


if __name__ == "__main__":
    num_halls = int(input())  # number of halls being calculated
    halls = []

    for hall in range(num_halls):
        dist = float(input())  # get distance to be traveled

        num_doors = int(input())  # get number of doors

        if num_doors == 0:
            halls.append({"dist": dist, "door_positions": []})
            continue

        # get list of positions of doors
        door_positions = list(map(float, input().split(" ")))

        # append a dictionary to `halls`
        halls.append({"dist": dist, "door_positions": door_positions})

    for hall in halls:
        time, transformations = calculate(hall)
        print(f"{time:.2f} {transformations}")