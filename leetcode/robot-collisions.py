class Solution(object):
    def survivedRobotsHealths(self, positions, healths, directions):
        robots = []
        for i in range(len(positions)):
            robots.append([positions[i], healths[i], directions[i], i])

        robots.sort()
        stack = []

        for robot in robots:
            if robot[2] == 'R':
                stack.append(robot)
            else:
                while stack and robot[1] > 0:
                    if stack[-1][1] < robot[1]:
                        robot[1] -= 1
                        stack[-1][1] = 0
                        stack.pop()
                    elif stack[-1][1] == robot[1]:
                        stack[-1][1] = 0
                        robot[1] = 0
                        stack.pop()
                        break
                    else:
                        stack[-1][1] -= 1
                        robot[1] = 0
                        break

        survivors = []
        for robot in sorted(robots, key=lambda x: x[3]):
            if robot[1] > 0:
                survivors.append(robot[1])

        return survivors