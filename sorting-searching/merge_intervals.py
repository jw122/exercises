def merge(intervals):
    """
    :type intervals: List[Interval]
    :rtype: List[Interval]
    """
    final = []
    # if the first element in current interval is smaller than the second element in the previous, merge
    for i in range(1, len(intervals)):
    	currInterval = intervals[i]
    	prevInterval = intervals[i-1]
    	# print currInterval
    	if currInterval[0] < prevInterval[1]:
    		prevInterval.append(currInterval[0])
    		prevInterval.append(currInterval[1])

    		prevInterval.sort()
    		final.append([prevInterval[0], prevInterval[-1]])
    		print final

    	else:
    		final.append(currInterval)
    return final

intervals = [[1,10],[2,6],[8,20],[15,18]]
merge(intervals)