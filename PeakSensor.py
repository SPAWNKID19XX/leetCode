'''
Problem: Count Peaks in Sensor Values

Description:
You are given a list of decimal numbers values, representing the radioactivity measured by a sensor every second.
A value is considered a peak if it meets one of the following conditions:

Top peak: The value is at least 5 units higher than both of its immediate neighbors.

Bottom peak: The value is at least 5 units lower than both of its immediate neighbors.

Return the total number of peaks in the list.

Notes:

The first and last elements of the list can never be peaks.

The list values always contains between 0 and 20 elements.

Each value is between 0 and 100.

Example 1

Input:
values = [1, 10, 1]

Output:
1

Explanation:
10 is a top peak because it is at least 5 units greater than its neighbors (1 and 1).

Example 2

Input:
values = [20, 10, 20]

Output:
1

Explanation:
10 is a bottom peak because it is at least 5 units lower than its neighbors (20 and 20).

Example 3

Input:
values = [5, 10, 5, 10, 5]

Output:
2

Explanation:

The second value (10) is a top peak.

The fourth value (10) is also a top peak.

Example 4

Input:
values = [5, 6, 5]

Output:
0

Explanation:
The difference between neighbors is less than 5, so no peaks.
'''


class SolutionPeak():
    def check_peaks(self, data_list: list) -> tuple:
        top_peak = 0
        bottom_peak = 0
        for i in range(1, len(data_list) - 1):
            left = data_list[i-1]
            current =data_list[i]
            right = data_list[i+1]
            if current >= left+5 and current >= right+5:
                top_peak += 1

            if current <= left-5 and current <= right-5:
                bottom_peak += 1

        res = top_peak + bottom_peak
        return (data_list, top_peak + bottom_peak, top_peak, bottom_peak)


values1 = [3, 9, 2, 15, 10, 20, 12, 25, 18, 5, 10]
values2 = [50, 52, 49, 51, 50, 52, 51, 50, 49, 52, 51]
values3 = [10, 20, 10, 20, 10, 20, 10, 20, 10, 20, 10]
values4 = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55]

a = SolutionPeak()
print(type(a.check_peaks(values1)))
print(f'A data list {a.check_peaks(values1)[0]} has {a.check_peaks(values1)[1]}.\n\tTop Peak: {a.check_peaks(values1)[2]}\n\tBottom Peak: {a.check_peaks(values1)[3]}')
print(f'A data list {a.check_peaks(values2)[0]} has {a.check_peaks(values2)[1]}.\n\tTop Peak: {a.check_peaks(values2)[2]}\n\tBottom Peak: {a.check_peaks(values2)[3]}')
print(f'A data list {a.check_peaks(values3)[0]} has {a.check_peaks(values3)[1]}.\n\tTop Peak: {a.check_peaks(values3)[2]}\n\tBottom Peak: {a.check_peaks(values3)[3]}')
print(f'A data list {a.check_peaks(values4)[0]} has {a.check_peaks(values4)[1]}.\n\tTop Peak: {a.check_peaks(values4)[2]}\n\tBottom Peak: {a.check_peaks(values4)[3]}')
