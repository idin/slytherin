def get_intersection(l1, l2):
	""" Finds the intersection of 2 lists including common duplicates"""

	intersection_set = set(l1).intersection(set(l2))
	intersection_list = []
	for i in intersection_set:
		num = min(l1.count(i), l2.count(i))
		for j in range(num):
			intersection_list.append(i)
	return intersection_list


