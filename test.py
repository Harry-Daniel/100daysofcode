def solution(heights):
    heights_replica=heights
    # Adding a replica so when items are removed the pointers dont mess up
    highlightOrder=[]
    while True:
        highlights=[]
        for index in range(len(heights_replica)):
            if index == 0:
                if heights_replica[index]>heights_replica[index+1]:
                    highlights.append(heights_replica[index])
                    heights.remove(heights_replica[index])
            elif index+1 == len(heights_replica)-1:
                if heights_replica[index-1]<heights_replica[index]:
                    highlights.append(heights_replica[index])
                    heights.remove(heights_replica[index])
            elif not index+1 >= len(heights_replica):
                if heights_replica[index-1]<heights_replica[index]>heights_replica[index+1]:
                    highlights.append(heights_replica[index])
                    heights.remove(heights_replica[index])
        
        print(min(highlights))
        # highlightOrder.append(smallest)
    return highlightOrder

print(solution([1,5,4,6,2,9]))